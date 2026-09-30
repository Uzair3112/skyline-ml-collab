"""Smoke train — a fast end-to-end slice of the real pipeline for CI.

Reads the raw CSV (a committed sample in CI, the DVC dataset locally),
normalises, encodes, splits, fits the parameter-driven pipeline and scores
it. Exits non-zero if the pipeline throws or any metric is NaN/inf, so a
broken training path turns every pull request red.
"""

from __future__ import annotations

import argparse
import sys

import numpy as np
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score

from ml_skyline.common import load_params, repo_path, set_seed
from ml_skyline.pipeline import build_pipeline
from ml_skyline.prepare import (
    EXPECTED_COLUMNS,
    build_splits,
    drop_ids,
    encode_target,
    read_raw,
)

DEFAULT_ROWS = 300
METRIC_NAMES = ("accuracy", "precision", "recall", "f1", "roc_auc")
REPORT_HEADER = "| metric | value |"


def run_smoke(data_path: str, *, rows: int = DEFAULT_ROWS, params: dict | None = None) -> dict:
    """Fit the full pipeline on a slice of ``data_path`` and return metrics."""
    params = params or load_params()
    seed = int(params["seed"])
    set_seed(seed)
    target = params["data"]["target"]

    path = repo_path(data_path)
    if not path.exists():
        raise FileNotFoundError(
            f"{data_path} not found — run `dvc pull` or pass --data tests/fixtures/sample.csv"
        )

    df = encode_target(drop_ids(read_raw(path)), target)
    missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"data is missing expected columns: {missing}")

    n = min(int(rows), len(df))
    if n < 20:
        raise ValueError(f"smoke slice too small: --rows {rows} on {len(df)} rows")
    df = df.sample(n=n, random_state=seed).reset_index(drop=True)

    train_df, test_df = build_splits(
        df,
        target=target,
        test_size=float(params["split"]["test_size"]),
        seed=seed,
    )

    pipeline = build_pipeline(train_df, params)
    X_train, y_train = train_df.drop(columns=[target]), train_df[target]
    X_test, y_test = test_df.drop(columns=[target]), test_df[target]
    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    metrics = {
        "accuracy": float(accuracy_score(y_test, y_pred)),
        "precision": float(precision_score(y_test, y_pred, zero_division=0)),
        "recall": float(recall_score(y_test, y_pred, zero_division=0)),
        "f1": float(f1_score(y_test, y_pred, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_test, pipeline.predict_proba(X_test)[:, 1])),
        "n_train": int(len(train_df)),
        "n_test": int(len(test_df)),
        "rows": n,
        "model": params["train"]["model"],
        "seed": seed,
    }
    return metrics


def check_metrics(metrics: dict) -> list[str]:
    """Return one message per metric that is NaN/inf/absurd."""
    problems = []
    for name in METRIC_NAMES:
        value = metrics.get(name)
        if value is None or not np.isfinite(value):
            problems.append(f"{name} is not finite: {value!r}")
        elif not 0.0 <= value <= 1.0:
            problems.append(f"{name} outside 0..1: {value!r}")
    return problems


def format_report(metrics: dict) -> str:
    lines = [
        REPORT_HEADER,
        "|---|---|",
        *(f"| {name} | {metrics[name]!r} |" for name in METRIC_NAMES),
        f"| n_train | {metrics['n_train']} |",
        f"| n_test | {metrics['n_test']} |",
        f"| model | {metrics['model']} |",
        f"| seed | {metrics['seed']} |",
    ]
    return "\n".join(lines) + "\n"


def is_smoke_report(path) -> bool:
    """True when *path* already holds a smoke report, i.e. is safe to overwrite."""
    try:
        head = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False
    return head.startswith(REPORT_HEADER)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--rows",
        type=int,
        default=DEFAULT_ROWS,
        help="size of the random slice to train on",
    )
    parser.add_argument(
        "--data",
        default=None,
        help="CSV to smoke on (default: params data.raw_train)",
    )
    parser.add_argument("--params", default=None, help="path to a params.yaml")
    parser.add_argument("--report", default=None, help="write a metrics markdown table here")
    args = parser.parse_args(argv)

    try:
        params = load_params(args.params) if args.params else None
        data = args.data or (params or load_params())["data"]["raw_train"]
        metrics = run_smoke(data, rows=args.rows, params=params)
    except Exception as exc:  # noqa: BLE001 - CI gate: any pipeline error must fail the job
        print(f"smoke-train FAILED: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1

    problems = check_metrics(metrics)
    if problems:
        print("smoke-train FAILED — invalid metrics:", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        return 1

    for name in METRIC_NAMES:
        print(f"{name}: {metrics[name]:.6f}")
    print(f"rows: {metrics['rows']} (train={metrics['n_train']}, test={metrics['n_test']})")

    if args.report:
        report_path = repo_path(args.report)
        if report_path.exists() and not is_smoke_report(report_path):
            print(
                f"smoke-train FAILED - refusing to overwrite {args.report}: "
                "it is not a smoke report (on case-insensitive filesystems "
                "`--report report.md` resolves to REPORT.md)",
                file=sys.stderr,
            )
            return 2
        report_path.write_text(format_report(metrics), encoding="utf-8")
        print(f"report: {args.report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
