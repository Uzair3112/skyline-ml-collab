"""Feature helpers promoted out of the EDA notebook (Module 05).

The notebook imports these instead of redefining them, so the cleaning step
used during exploration is exactly the one unit-tested here.
"""

from __future__ import annotations

import pandas as pd

from ml_skyline.prepare import drop_ids, encode_target

#: Service-quality ratings the airline survey scores 0–5.
SERVICE_COLUMNS: tuple[str, ...] = (
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
)

DELAY_COLUMN = "Arrival Delay in Minutes"


def fill_arrival_delay(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing ``Arrival Delay in Minutes`` with the column median.

    The raw export leaves a few hundred rows without a value (310 in
    ``train.csv``); the median (0 minutes for this dataset) is robust to the
    long right tail of delays.
    """
    if DELAY_COLUMN not in df.columns:
        return df
    out = df.copy()
    median = out[DELAY_COLUMN].median()
    out[DELAY_COLUMN] = out[DELAY_COLUMN].fillna(median)
    return out


def add_service_score(df: pd.DataFrame) -> pd.DataFrame:
    """Add ``Service Score``: the row-wise mean of the 0–5 service ratings."""
    present = [c for c in SERVICE_COLUMNS if c in df.columns]
    if not present:
        return df
    out = df.copy()
    out["Service Score"] = out[present].mean(axis=1)
    return out


def build_features(df: pd.DataFrame, *, target: str | None = None) -> pd.DataFrame:
    """Return an EDA-ready frame: ids dropped, delays imputed, score added.

    Parameters
    ----------
    df:
        Raw (or already header-repaired) survey frame.
    target:
        Name of the label column. When given and the labels are still strings,
        it is binarised with :data:`ml_skyline.common.TARGET_MAP`
        (``satisfied`` -> 1, ``neutral or dissatisfied`` -> 0).
    """
    out = fill_arrival_delay(drop_ids(df))
    out = add_service_score(out)
    # pandas 3 gives strings the dedicated ``str`` dtype, so test for *numeric*
    # rather than ``dtype == object`` to decide whether labels need mapping.
    if (
        target is not None
        and target in out.columns
        and not pd.api.types.is_numeric_dtype(out[target])
    ):
        out = encode_target(out, target)
    return out
