import pandas as pd
import pytest

from ml_skyline.common import load_params
from ml_skyline.pipeline import (
    MODELS,
    build_model,
    build_pipeline,
    build_preprocessor,
    split_feature_types,
)

TARGET = "satisfaction"

TRAIN_FRAME = pd.DataFrame(
    {
        "Gender": ["Male", "Female", "Male", "Female", "Male", "Female"],
        "Class": ["Business", "Eco", "Eco Plus", "Business", "Eco", "Eco Plus"],
        "Age": [30, 41, 50, 22, 35, 61],
        "Flight Distance": [100, 2500, 800, 1500, 300, 4000],
        TARGET: [1, 0, 1, 0, 1, 0],
    }
)


def _params(**train_overrides):
    params = load_params()
    params["train"].update(train_overrides)
    return params


def test_split_feature_types_separates_numeric_and_categorical():
    categorical, numeric = split_feature_types(TRAIN_FRAME, TARGET)
    assert set(categorical) == {"Gender", "Class"}
    assert set(numeric) == {"Age", "Flight Distance"}
    assert TARGET not in categorical + numeric


def test_every_declared_model_can_be_built():
    for name in MODELS:
        params = _params(model=name)
        assert build_model(params) is not None


def test_unknown_model_raises():
    params = _params(model="not_a_model")
    with pytest.raises(ValueError, match="unknown model"):
        build_model(params)


def test_pipeline_fits_and_predicts_on_unseen_categories():
    """The one-hot encoder must ignore categories absent from the training split."""
    params = _params(model="random_forest", n_estimators=10, max_depth=3)
    pipeline = build_pipeline(TRAIN_FRAME, params)
    pipeline.fit(TRAIN_FRAME.drop(columns=[TARGET]), TRAIN_FRAME[TARGET])

    unseen = pd.DataFrame(
        {
            "Gender": ["Other"],
            "Class": ["Space"],
            "Age": [40],
            "Flight Distance": [777],
        }
    )
    predictions = pipeline.predict(unseen)
    assert len(predictions) == 1


def test_preprocessor_is_part_of_the_pipeline_so_it_cannot_leak():
    """Fitting must happen through the Pipeline, never on the full dataset."""
    params = _params(model="logreg")
    pipeline = build_pipeline(TRAIN_FRAME, params)
    assert set(pipeline.named_steps) == {"prep", "model"}
    assert build_preprocessor(TRAIN_FRAME, TARGET) is not None
