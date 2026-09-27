"""Stage 2 — fit the pipeline on the processed training split and persist it."""

from __future__ import annotations

import argparse

import joblib
import pandas as pd

from ml_skyline.common import load_params, repo_path, set_seed
from ml_skyline.pipeline import build_pipeline


def run(params: dict | None = None) -> float:
    params = params or load_params()
    seed = int(params["seed"])
    set_seed(seed)

    target = params["data"]["target"]
    processed_dir = repo_path(params["data"]["processed_dir"])
    train_path = processed_dir / "train.csv"

    df = pd.read_csv(train_path)
    X, y = df.drop(columns=[target]), df[target]

    pipeline = build_pipeline(df, params)
    pipeline.fit(X, y)

    model_path = repo_path(params["paths"]["model"])
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, model_path)

    train_accuracy = float(pipeline.score(X, y))
    print(f"model:   {params['train']['model']} (seed={seed})")
    print(f"saved:   {model_path}")
    print(f"train accuracy: {train_accuracy:.4f}")
    return train_accuracy


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--params", default=None, help="path to a params.yaml")
    args = parser.parse_args(argv)
    run(load_params(args.params) if args.params else None)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
