"""Model architecture: preprocessing + estimator, both parameter driven.

The imputer/scaler/encoder are built here and fit inside the sklearn Pipeline,
so they only ever see the training split — no leakage.
"""

from __future__ import annotations

from typing import Any

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier

#: Estimators selectable via ``params.yaml -> train.model``.
MODELS = ("random_forest", "logreg", "decision_tree", "knn")


def split_feature_types(df: pd.DataFrame, target: str) -> tuple[list[str], list[str]]:
    """Return (categorical, numeric) feature column names for ``df``."""
    features = [c for c in df.columns if c != target]
    categorical = [c for c in features if not pd.api.types.is_numeric_dtype(df[c])]
    numeric = [c for c in features if pd.api.types.is_numeric_dtype(df[c])]
    return categorical, numeric


def build_preprocessor(df: pd.DataFrame, target: str) -> ColumnTransformer:
    categorical, numeric = split_feature_types(df, target)
    transformers = []
    if numeric:
        transformers.append(
            (
                "num",
                Pipeline(
                    steps=[
                        ("impute", SimpleImputer(strategy="median")),
                        ("scale", StandardScaler()),
                    ]
                ),
                numeric,
            )
        )
    if categorical:
        transformers.append(
            (
                "cat",
                Pipeline(
                    steps=[
                        ("impute", SimpleImputer(strategy="most_frequent")),
                        ("onehot", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                categorical,
            )
        )
    return ColumnTransformer(transformers=transformers, remainder="drop")


def build_model(params: dict[str, Any]):
    """Instantiate the estimator named by ``params['train']['model']``."""
    cfg = params["train"]
    seed = int(params["seed"])
    name = cfg["model"]
    n_estimators = int(cfg.get("n_estimators", 100))
    max_depth = int(cfg.get("max_depth", 6))

    if name == "random_forest":
        return RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=seed,
            n_jobs=-1,
        )
    if name == "logreg":
        return LogisticRegression(max_iter=1000, random_state=seed)
    if name == "decision_tree":
        return DecisionTreeClassifier(max_depth=max_depth, random_state=seed)
    if name == "knn":
        return KNeighborsClassifier(n_neighbors=10)
    raise ValueError(f"unknown model {name!r}; expected one of {MODELS}")


def build_pipeline(df: pd.DataFrame, params: dict[str, Any]) -> Pipeline:
    """Full preprocessing + estimator pipeline for the given frame."""
    return Pipeline(
        steps=[
            ("prep", build_preprocessor(df, params["data"]["target"])),
            ("model", build_model(params)),
        ]
    )
