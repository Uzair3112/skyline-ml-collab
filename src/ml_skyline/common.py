"""Shared helpers: repository paths, parameter loading and seeding.

No function in this package may contain an absolute path; everything is
resolved against ``REPO_ROOT`` so the code runs on any teammate's machine.
"""

from __future__ import annotations

import random
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yaml

# src/ml_skyline/common.py -> parents[0]=ml_skyline, [1]=src, [2]=repo root
REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PARAMS = REPO_ROOT / "params.yaml"

#: Raw labels -> integer. Positive class (1) is "satisfied".
TARGET_MAP: dict[str, int] = {"satisfied": 1, "neutral or dissatisfied": 0}
TARGET_INV_MAP: dict[int, str] = {v: k for k, v in TARGET_MAP.items()}


def repo_path(relative: str | Path) -> Path:
    """Resolve ``relative`` against the repository root."""
    path = Path(relative)
    return path if path.is_absolute() else REPO_ROOT / path


def load_params(path: str | Path | None = None) -> dict[str, Any]:
    """Load ``params.yaml`` (or a drop-in replacement)."""
    with open(path or DEFAULT_PARAMS, encoding="utf-8") as handle:
        params: dict[str, Any] = yaml.safe_load(handle)
    return params


def set_seed(seed: int) -> None:
    """Seed every source of randomness the pipeline can touch."""
    random.seed(seed)
    np.random.seed(seed)


def normalise_text(series: pd.Series) -> pd.Series:
    """Collapse tabs/newlines introduced by a corrupted export into single spaces.

    The published ``train.csv`` has TAB characters inside column names and
    trailing tabs inside string values (``"Customer\\tType"``,
    ``"satisfied\\t\\t\\t"``). Normalising makes it compatible with the clean
    ``test.csv`` and with the label map.
    """
    if not pd.api.types.is_object_dtype(series) and not pd.api.types.is_string_dtype(series):
        return series
    return series.str.replace(r"\s+", " ", regex=True).str.strip()
