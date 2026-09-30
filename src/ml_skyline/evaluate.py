"""Stage 3 — score the held-out split and write ``metrics.json``.

The metrics file also records the seed and the commit SHA so every reported
number can be traced back to the exact code that produced it.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score

from ml_skyline.common import REPO_ROOT, load_params, repo_path


def git_sha() -> str | None:
    """Current commit, or ``None`` outside a work tree."""
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=REPO_ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def compute_metrics(y_true, y_pred, y_proba=None) -> dict[str, float]:
    metrics = {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "f1": float(f1_score(y_true, y_pred, zero_division=0)),
    }
    if y_proba is not None:
        metrics["roc_auc"] = float(roc_auc_score(y_true, y_proba))
    return metrics


def run(params: dict | None = None) -> dict[str, Any]:
    params = params or load_params()
    target = params["data"]["target"]
    processed_dir = repo_path(params["data"]["processed_dir"])
    test_df = pd.read_csv(processed_dir / "test.csv")

    pipeline = joblib.load(repo_path(params["paths"]["model"]))
    X, y_true = test_df.drop(columns=[target]), test_df[target]

    y_pred = pipeline.predict(X)
    proba = pipeline.predict_proba(X)[:, 1] if hasattr(pipeline, "predict_proba") else None

    report: dict[str, Any] = {
        **compute_metrics(y_true, y_pred, proba),
        "n_train": int(len(pd.read_csv(processed_dir / "train.csv"))),
        "n_test": int(len(test_df)),
        "seed": int(params["seed"]),
        "model": params["train"]["model"],
        "params": {"split": params["split"], "train": params["train"]},
        "commit_sha": git_sha(),
    }

    metrics_path = repo_path(params["paths"]["metrics"])
    metrics_path.parent.mkdir(parents=True, exist_ok=True)
    with open(metrics_path, "w", encoding="utf-8") as handle:
        json.dump(report, handle, indent=2, sort_keys=True)
        handle.write("\n")

    printable = {k: round(v, 4) for k, v in report.items() if isinstance(v, float)}
    print(f"metrics: {metrics_path.relative_to(Path(REPO_ROOT))}")
    print(json.dumps(printable, indent=2))
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--params", default=None, help="path to a params.yaml")
    args = parser.parse_args(argv)
    run(load_params(args.params) if args.params else None)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
