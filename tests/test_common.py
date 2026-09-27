import numpy as np
import pandas as pd

from ml_skyline.common import TARGET_INV_MAP, TARGET_MAP, load_params, normalise_text, set_seed


def test_target_map_round_trips():
    for label, code in TARGET_MAP.items():
        assert TARGET_INV_MAP[code] == label
    assert set(TARGET_MAP) == {"satisfied", "neutral or dissatisfied"}
    assert TARGET_MAP["satisfied"] == 1


def test_params_load_from_repo_root():
    params = load_params()
    assert params["seed"] == 42
    assert 0 < params["split"]["test_size"] < 1
    assert params["train"]["model"] in {"random_forest", "logreg", "decision_tree", "knn"}


def test_normalise_text_repairs_tabs_and_padding():
    series = pd.Series(["Customer\tType", "satisfied\t\t\t", " neutral  or\tdissatisfied "])
    assert list(normalise_text(series)) == [
        "Customer Type",
        "satisfied",
        "neutral or dissatisfied",
    ]


def test_normalise_text_leaves_numeric_columns_alone():
    series = pd.Series([1, 2, 3])
    assert normalise_text(series).equals(series)


def test_set_seed_is_deterministic():
    set_seed(123)
    first = np.random.rand(3)
    set_seed(123)
    second = np.random.rand(3)
    assert np.allclose(first, second)
