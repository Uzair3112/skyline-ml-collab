"""CI data gate — schema, label, range and null checks on a committed sample.

CI runners have no DagsHub credentials, so they cannot ``dvc pull`` the real
dataset. This module validates a small committed fixture
(``tests/fixtures/sample.csv``, a 500-row slice of the raw export with
end-of-line whitespace trimmed by pre-commit)
with the same normalisation the training pipeline applies, so a broken or
rotted dataset fails every pull request.
"""

from __future__ import annotations

import argparse
import sys

import pandas as pd

from ml_skyline.common import TARGET_MAP, repo_path
from ml_skyline.prepare import EXPECTED_COLUMNS, drop_ids, read_raw

#: Service ratings that must live in 0..5 (indices into EXPECTED_COLUMNS).
RATING_COLUMNS = EXPECTED_COLUMNS[6:20]
#: Numeric feature columns with their inclusive allowed range.
RANGE_RULES: dict[str, tuple[float, float]] = {
    "Age": (0, 120),
    "Flight Distance": (0, 100_000),
    "Departure Delay in Minutes": (0, 2_000),
    "Arrival Delay in Minutes": (0, 2_000),
}
#: Maximum share of nulls allowed per column (agreed threshold: 1 %).
MAX_NULL_FRACTION = 0.01
DEFAULT_SAMPLE = "tests/fixtures/sample.csv"


def run_checks(sample_path: str, *, max_null_fraction: float = MAX_NULL_FRACTION) -> list[str]:
    """Run every check against ``sample_path``; return a list of failures.

    An empty list means the data passed all checks.
    """
    failures: list[str] = []
    path = repo_path(sample_path)

    if not path.exists():
        return [f"sample file not found: {sample_path}"]

    try:
        df = drop_ids(read_raw(path))
    except Exception as exc:  # noqa: BLE001 - report any parse failure as a check failure
        return [f"could not read sample: {type(exc).__name__}: {exc}"]

    # 1. expected column names present (in order)
    missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    extra = [c for c in df.columns if c not in EXPECTED_COLUMNS]
    if missing:
        failures.append(f"missing expected columns: {missing}")
    if extra:
        failures.append(f"unexpected columns: {extra}")

    # 2. target labels within the agreed vocabulary
    target = "satisfaction"
    if target in df.columns:
        labels = set(df[target].dropna().unique())
        unknown = labels - set(TARGET_MAP)
        if unknown:
            failures.append(f"unknown {target} labels: {sorted(unknown)}")
        n_null_target = int(df[target].isna().sum())
        if n_null_target:
            failures.append(f"{target} has {n_null_target} null values")
    else:
        failures.append(f"target column {target!r} absent")

    # 3. rating columns within 0..5
    for column in RATING_COLUMNS:
        if column not in df.columns:
            continue
        values = pd.to_numeric(df[column], errors="coerce")
        if values.isna().any():
            failures.append(f"{column}: contains null/non-numeric values")
            continue
        if not ((values >= 0) & (values <= 5)).all():
            lo, hi = float(values.min()), float(values.max())
            failures.append(f"{column}: values outside 0..5 (min={lo}, max={hi})")

    # 4. numeric feature ranges
    for column, (lo, hi) in RANGE_RULES.items():
        if column not in df.columns:
            continue
        values = pd.to_numeric(df[column], errors="coerce")
        if values.isna().any():
            failures.append(f"{column}: contains null/non-numeric values")
            continue
        if not ((values >= lo) & (values <= hi)).all():
            bad = values[(values < lo) | (values > hi)]
            failures.append(
                f"{column}: {len(bad)} value(s) outside {lo}..{hi} (e.g. {float(bad.iloc[0])})"
            )

    # 5. null counts below the agreed threshold
    if len(df):
        null_share = df.isna().mean()
        for column, share in null_share[null_share > max_null_fraction].items():
            failures.append(
                f"{column}: null share {share:.2%} exceeds {max_null_fraction:.0%} threshold"
            )

    if not len(df):
        failures.append("sample contains no data rows")

    return failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sample",
        default=DEFAULT_SAMPLE,
        help="path to the committed sample CSV (relative to the repo root)",
    )
    parser.add_argument(
        "--max-null-fraction",
        type=float,
        default=MAX_NULL_FRACTION,
        help="per-column null share allowed before failing",
    )
    args = parser.parse_args(argv)

    failures = run_checks(args.sample, max_null_fraction=args.max_null_fraction)
    if failures:
        print(f"data-checks FAILED ({len(failures)}):")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print(f"data-checks passed: {args.sample}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
