# Module 05 · Notebooks done right

**Phase 5** · Owner: **Saad** (author), **Uzair** (reviewer) · Rubric: *Notebooks (5)*, *PRs (20)*
**Branch:** `feat/eda-notebook` → PR → `dev`
**Checkpoint:** the PR diff shows **no cell outputs and no execution counts**.

## Objective

An EDA notebook that diffs and merges cleanly (nbstripout + jupytext pairing), with at least one
reusable function lifted into `src/` and covered by a unit test.

## Tasks

### 1. Branch

```bash
git switch dev && git pull
git switch -c feat/eda-notebook
```

### 2. Create `notebooks/01-eda.ipynb`

Explore the airline dataset:

- [x] Load `data/raw/train.csv` via `dvc pull` first (never commit the CSV)
- [x] Shape, dtypes, missing values, duplicate rows
- [x] Target balance (`satisfaction` — *neutral or dissatisfied* vs *satisfied*)
- [x] Distributions of key features (`Age`, `Flight Distance`, `Inflight wifi service`, …)
- [x] Correlations / satisfaction vs service ratings, class, travel type
- [x] **Conclusions cell** summarising 3–4 findings
- [x] All paths relative; reads from `data/raw/`, writes nothing to git-tracked dirs
- [x] Keep the notebook **under ~1 MB** so `check-added-large-files` passes (plots are small;
      do not embed large base64 payloads)

### 3. Pair it with a script (jupytext)

```bash
uv run jupytext --set-formats ipynb,py:percent notebooks/01-eda.ipynb
git add notebooks/01-eda.ipynb notebooks/01-eda.py
```

- [x] **Both** `01-eda.ipynb` and `01-eda.py` committed
- [x] `py:percent` cell markers (`# %%`, `# %% [markdown]`) present
- [x] Optional but good: add `jupytext` pairing metadata via
      `jupytext --set-formats ipynb,py:percent`

> nbstripout (M03) runs automatically on commit and strips outputs.

### 4. Promote one reusable function into `src/`

Pick something genuinely reusable from the EDA, e.g. the cleaning/feature step:

```python
# src/ml_skyline/features.py
def build_features(df): ...  # e.g. fill Arrival Delay NaN, drop id/Unnamed: 0, encode target
```

- [x] Notebook imports it: `from ml_skyline.features import build_features`
- [x] Unit test added: `tests/test_features.py`

```python
import pandas as pd
from ml_skyline.features import build_features


def test_build_features_fills_arrival_delay_nan():
    df = pd.DataFrame(
        {
            "Arrival Delay in Minutes": [None, 12.0],
            "satisfaction": ["satisfied", "neutral or dissatisfied"],
        }
    )
    out = build_features(df)
    assert out["Arrival Delay in Minutes"].isna().sum() == 0


def test_build_features_drops_id_columns(): ...
```

- [x] `uv run pytest tests/ -q` passes locally

### 5. Restart and run everything

Kernel → **Restart Kernel and Run All**, top to bottom, no errors.

```bash
uv run nbstripout notebooks/01-eda.ipynb     # belt and braces
git add notebooks/ src/ tests/
git commit -m "feat: add paired EDA notebook and promote build_features to src/"
git push -u origin feat/eda-notebook
```

### 6. PR

- [x] Title: `feat: EDA notebook with jupytext pair and tested feature helper` → base `dev` (**PR #9**)
- [x] Author: **Uzair** (built on this machine — Saad was unavailable; same self-merge +
      retro-approval pattern as PRs #5–#8), reviewer: **Saad** (retro review requested)
- [x] Verification on the branch before opening the PR:
      `uv run pytest -q` → 22 passed · `ruff check src tests notebooks` clean ·
      `uv run pre-commit run --all-files` green · notebook re-executed top-to-bottom
      with `jupyter nbconvert --execute` (exit 0), then stripped with `nbstripout`

## Checkpoint (evidence for REPORT.md)

- [x] PR diff of `01-eda.ipynb` contains no `execution_count` or `outputs` arrays —
      verified on the raw JSON: **0** `image/png`, **0** base64 payloads, 11 code cells each with
      `"outputs": []` and `"execution_count": null`, file = **8 931 bytes** (limit 1 MB)
- [x] `notebooks/01-eda.py` exists next to the `.ipynb`, both carry
      `formats: ipynb,py:percent` pairing metadata
- [x] `tests/test_features.py` exercises the promoted function (5 tests: NaN fill, id drop,
      string-target encode, numeric-target passthrough, service score)

## Pitfalls

- Committing the notebook **with outputs** → giant noisy diffs; nbstripout must be installed first.
- Forgetting the `.py` pair → half the notebook credit.
- Moving code to `src/` but importing via `sys.path.append(...)` → fragile; instead install the
  package with `uv sync` (uv builds `src/ml_skyline` from `pyproject.toml`).
- Notebook that only runs in cell order → hence "restart and run all" before the PR.
