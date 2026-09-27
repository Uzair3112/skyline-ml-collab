"""Stage 1 — raw CSV -> clean, seeded train/test splits.

Only *non-fitting* transformations happen here (whitespace repair, column
drops, label mapping, splitting). Anything that learns statistics from data
(imputers, scalers, encoders) lives in the sklearn Pipeline built by
``ml_skyline.pipeline`` and is therefore fit on the training split only.
"""

from __future__ import annotations

import argparse

import pandas as pd
from sklearn.model_selection import train_test_split

from ml_skyline.common import (
    REPO_ROOT,
    TARGET_MAP,
    load_params,
    normalise_text,
    repo_path,
    set_seed,
)


def is_id_column(name: str) -> bool:
    """True for ``id``, a blank index header, or pandas' ``Unnamed: N``."""
    normalised = str(name).strip().lower()
    return normalised in {"", "id"} or normalised.startswith("unnamed:")


#: Names the corrupted export should produce after :func:`normalise_text`.
EXPECTED_COLUMNS = (
    "Gender",
    "Customer Type",
    "Age",
    "Type of Travel",
    "Class",
    "Flight Distance",
    "Inflight wifi service",
    "Departure/Arrival time convenient",
    "Ease of Online booking",
    "Gate location",
    "Food and drink",
    "Online boarding",
    "Seat comfort",
    "Inflight entertainment",
    "On-board service",
    "Leg room service",
    "Baggage handling",
    "Checkin service",
    "Inflight service",
    "Cleanliness",
    "Departure Delay in Minutes",
    "Arrival Delay in Minutes",
    "satisfaction",
)


def normalise_frame(df: pd.DataFrame) -> pd.DataFrame:
    """Repair tab-corrupted headers and string values in place-of-copy."""
    df = df.copy()
    df.columns = [str(c).replace("\t", " ").strip() for c in df.columns]
    for column in df.select_dtypes(include=["object", "string"]).columns:
        df[column] = normalise_text(df[column])
    return df


def read_raw(path) -> pd.DataFrame:
    """Read a raw CSV and repair the tab-corrupted headers/values."""
    return normalise_frame(pd.read_csv(path))


def drop_ids(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop(columns=[c for c in df.columns if is_id_column(c)], errors="ignore")


def encode_target(df: pd.DataFrame, target: str = "satisfaction") -> pd.DataFrame:
    unknown = set(df[target].unique()) - set(TARGET_MAP)
    if unknown:
        raise ValueError(f"unmapped labels in {target!r}: {sorted(unknown)}")
    df = df.copy()
    df[target] = df[target].map(TARGET_MAP).astype("int64")
    return df


def build_splits(
    df: pd.DataFrame,
    *,
    target: str,
    test_size: float,
    seed: int,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Stratified, seeded split. Identical inputs -> identical outputs."""
    return train_test_split(
        df,
        test_size=test_size,
        random_state=seed,
        stratify=df[target],
    )


def run(params: dict | None = None) -> tuple[pd.DataFrame, pd.DataFrame]:
    params = params or load_params()
    set_seed(int(params["seed"]))

    raw_path = repo_path(params["data"]["raw_train"])
    out_dir = repo_path(params["data"]["processed_dir"])
    target = params["data"]["target"]

    df = encode_target(drop_ids(read_raw(raw_path)), target)
    missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"raw data is missing expected columns: {missing}")

    train_df, test_df = build_splits(
        df,
        target=target,
        test_size=float(params["split"]["test_size"]),
        seed=int(params["seed"]),
    )

    out_dir.mkdir(parents=True, exist_ok=True)
    train_path = out_dir / "train.csv"
    test_path = out_dir / "test.csv"
    train_df.to_csv(train_path, index=False)
    test_df.to_csv(test_path, index=False)

    print(f"train: {train_path.relative_to(REPO_ROOT)} {train_df.shape}")
    print(f"test:  {test_path.relative_to(REPO_ROOT)} {test_df.shape}")
    return train_df, test_df


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--params", default=None, help="path to a params.yaml")
    args = parser.parse_args(argv)
    run(load_params(args.params) if args.params else None)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
