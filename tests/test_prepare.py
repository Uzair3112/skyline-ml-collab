import pandas as pd
import pytest

from ml_skyline.common import REPO_ROOT, load_params, repo_path
from ml_skyline.prepare import (
    EXPECTED_COLUMNS,
    build_splits,
    drop_ids,
    encode_target,
    normalise_frame,
    read_raw,
)

CORRUPTED = pd.DataFrame(
    {
        "": [0, 1, 2, 3],
        "id": [10, 11, 12, 13],
        "Customer\tType": [
            "Loyal\tcustomer",
            "disloyal customer",
            "Loyal customer",
            "disloyal customer",
        ],
        "Age": [30, 41, 50, 22],
        "satisfaction": [
            "satisfied\t\t",
            "neutral\tor\tdissatisfied",
            "satisfied",
            "neutral or dissatisfied",
        ],
    }
)


def test_drop_ids_removes_identifier_columns():
    out = drop_ids(normalise_frame(CORRUPTED))
    assert "id" not in out.columns
    assert "" not in out.columns
    assert "Age" in out.columns


def test_encode_target_maps_both_labels():
    out = encode_target(drop_ids(normalise_frame(CORRUPTED)))
    assert set(out["satisfaction"].unique()) == {0, 1}
    assert out["satisfaction"].dtype.kind == "i"


def test_encode_target_rejects_unknown_labels():
    df = drop_ids(normalise_frame(CORRUPTED))
    df.loc[0, "satisfaction"] = "maybe"
    with pytest.raises(ValueError, match="unmapped labels"):
        encode_target(df)


def test_read_raw_repairs_tab_corrupted_headers(tmp_path):
    path = tmp_path / "corrupt.csv"
    CORRUPTED.to_csv(path, index=False)
    df = read_raw(path)
    assert "Customer Type" in df.columns
    assert "Customer\tType" not in df.columns
    assert df["Customer Type"].str.contains("\t").sum() == 0


def test_build_splits_is_deterministic_and_stratified():
    df = encode_target(drop_ids(normalise_frame(CORRUPTED)))
    params = load_params()
    a_train, a_test = build_splits(
        df, target="satisfaction", test_size=0.5, seed=int(params["seed"])
    )
    b_train, b_test = build_splits(
        df, target="satisfaction", test_size=0.5, seed=int(params["seed"])
    )
    assert list(a_train.index) == list(b_train.index)
    assert list(a_test.index) == list(b_test.index)
    assert set(a_train.index).isdisjoint(a_test.index)


def test_real_raw_data_has_expected_schema():
    """Runs only when the DVC-tracked dataset has been pulled."""
    raw = repo_path(load_params()["data"]["raw_train"])
    if not raw.exists():
        pytest.skip("data/raw/train.csv not present (run `dvc pull`)")
    df = drop_ids(read_raw(raw))
    assert tuple(df.columns) == EXPECTED_COLUMNS
    assert df["satisfaction"].isin(["satisfied", "neutral or dissatisfied"]).all()
    assert REPO_ROOT in raw.parents


def test_no_hardcoded_absolute_paths_in_source():
    """Every path in src/ must be relative to REPO_ROOT."""
    offenders = []
    for path in (REPO_ROOT / "src").rglob("*.py"):
        text = path.read_text(encoding="utf-8")
        if "/home/" in text or "/Users/" in text:
            offenders.append(path.name)
    assert not offenders, f"hardcoded absolute paths found in {offenders}"
