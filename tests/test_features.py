"""Unit tests for the feature helpers promoted from the EDA notebook."""

import pandas as pd

from ml_skyline.features import SERVICE_COLUMNS, add_service_score, build_features


def test_build_features_fills_arrival_delay_nan():
    df = pd.DataFrame(
        {
            "Arrival Delay in Minutes": [None, 12.0],
            "satisfaction": ["satisfied", "neutral or dissatisfied"],
        }
    )
    out = build_features(df)
    assert out["Arrival Delay in Minutes"].isna().sum() == 0


def test_build_features_drops_id_columns():
    df = pd.DataFrame(
        {
            "id": [1, 2],
            "Unnamed: 0": [0, 1],
            "": [7, 8],
            "Age": [30, 41],
            "Arrival Delay in Minutes": [0.0, 5.0],
        }
    )
    out = build_features(df)
    assert not any(c in out.columns for c in ("id", "Unnamed: 0", ""))
    assert "Age" in out.columns


def test_build_features_encodes_string_target():
    df = pd.DataFrame(
        {
            "Arrival Delay in Minutes": [1.0, 2.0],
            "satisfaction": ["satisfied", "neutral or dissatisfied"],
        }
    )
    out = build_features(df, target="satisfaction")
    assert out["satisfaction"].tolist() == [1, 0]
    assert out["satisfaction"].dtype == "int64"


def test_build_features_keeps_numeric_target_untouched():
    df = pd.DataFrame(
        {
            "Arrival Delay in Minutes": [1.0, 2.0],
            "satisfaction": [1, 0],
        }
    )
    out = build_features(df, target="satisfaction")
    assert out["satisfaction"].tolist() == [1, 0]


def test_add_service_score_is_mean_of_present_service_columns():
    ratings = {name: 5.0 for name in SERVICE_COLUMNS[:2]}
    df = pd.DataFrame([{**ratings, "Age": 30}])
    out = add_service_score(df)
    assert out["Service Score"].iloc[0] == 5.0
    # columns absent from the frame are skipped, not KeyError-ed
    assert add_service_score(pd.DataFrame({"Age": [30]})).equals(pd.DataFrame({"Age": [30]}))
