"""Tests for the Module 08 CI gates (data checks + smoke train)."""

from __future__ import annotations

import pandas as pd

from ml_skyline.common import TARGET_MAP
from ml_skyline.data_checks import main as data_checks_main
from ml_skyline.data_checks import run_checks
from ml_skyline.prepare import EXPECTED_COLUMNS
from ml_skyline.smoke import check_metrics, run_smoke
from ml_skyline.smoke import main as smoke_main

FIXTURE = "tests/fixtures/sample.csv"


def _frame_with(target: str = "satisfied") -> pd.DataFrame:
    """A tiny well-formed frame with one adjustable target label."""
    n = 10
    row = {column: 3 for column in EXPECTED_COLUMNS[6:20]}
    df = pd.DataFrame([row] * n)
    df["Gender"] = "Male"
    df["Customer Type"] = "loyal customer"
    df["Type of Travel"] = "business travel"
    df["Class"] = "Business"
    df["Age"] = 30
    df["Flight Distance"] = 1000
    df["Departure Delay in Minutes"] = 0
    df["Arrival Delay in Minutes"] = 0
    df["satisfaction"] = target
    return df[list(EXPECTED_COLUMNS)]


def test_fixture_passes_data_checks():
    assert run_checks(FIXTURE) == []


def test_data_checks_missing_file_is_reported():
    failures = run_checks("tests/fixtures/does-not-exist.csv")
    assert failures and "not found" in failures[0]


def test_data_checks_rejects_unknown_label(tmp_path):
    path = tmp_path / "bad.csv"
    _frame_with(target="angry").to_csv(path, index=False)
    failures = run_checks(str(path))
    assert any("unknown satisfaction labels" in failure for failure in failures)


def test_data_checks_rejects_out_of_range_rating(tmp_path):
    path = tmp_path / "bad-rating.csv"
    frame = _frame_with()
    frame["Seat comfort"] = 9
    frame.to_csv(path, index=False)
    failures = run_checks(str(path))
    assert any("Seat comfort" in failure and "0..5" in failure for failure in failures)


def test_data_checks_rejects_null_flood(tmp_path):
    path = tmp_path / "nulls.csv"
    frame = _frame_with()
    frame["Age"] = None
    frame.to_csv(path, index=False)
    failures = run_checks(str(path))
    assert any("null share" in failure for failure in failures)


def test_data_checks_main_exit_codes(capsys):
    assert data_checks_main(["--sample", FIXTURE]) == 0
    assert data_checks_main(["--sample", "tests/fixtures/nope.csv"]) == 1
    assert "passed" in capsys.readouterr().out


def test_smoke_produces_finite_metrics():
    metrics = run_smoke(FIXTURE, rows=300)
    assert check_metrics(metrics) == []
    assert metrics["n_train"] + metrics["n_test"] == metrics["rows"]
    assert metrics["rows"] == 300


def test_smoke_main_writes_report(tmp_path, capsys):
    report = tmp_path / "report.md"
    code = smoke_main(["--rows", "300", "--data", FIXTURE, "--report", str(report)])
    assert code == 0
    text = report.read_text(encoding="utf-8")
    assert "| accuracy |" in text and "| f1 |" in text
    assert "f1:" in capsys.readouterr().out


def test_smoke_main_fails_on_missing_data(capsys):
    code = smoke_main(["--rows", "300", "--data", "tests/fixtures/nope.csv"])
    assert code == 1
    assert "FAILED" in capsys.readouterr().err


def test_smoke_report_refuses_to_clobber_non_report(tmp_path, capsys):
    target = tmp_path / "REPORT.md"
    target.write_text("# Release report\nkeep me\n", encoding="utf-8")
    code = smoke_main(["--rows", "300", "--data", FIXTURE, "--report", str(target)])
    assert code == 2
    assert "refusing to overwrite" in capsys.readouterr().err
    assert target.read_text(encoding="utf-8").startswith("# Release report")


def test_smoke_report_overwrites_previous_smoke_report(tmp_path, capsys):
    report = tmp_path / "cml-report.md"
    for _ in range(2):
        assert smoke_main(["--rows", "300", "--data", FIXTURE, "--report", str(report)]) == 0
    capsys.readouterr()
    assert report.read_text(encoding="utf-8").startswith("| metric | value |")


def test_smoke_rejects_unmapped_labels(tmp_path):
    path = tmp_path / "bad-target.csv"
    _frame_with(target="angry").to_csv(path, index=False)
    try:
        run_smoke(str(path), rows=30)
    except ValueError as exc:
        assert "unmapped labels" in str(exc)
    else:
        raise AssertionError("expected ValueError for unmapped labels")


def test_target_map_vocabulary_unchanged():
    assert TARGET_MAP == {"satisfied": 1, "neutral or dissatisfied": 0}
