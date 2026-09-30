# Module 06 · A reproducible pipeline

**Phase 6** · Owner: **Saad** (Model owner), **Uzair** (reviewer) · Rubric: *Reproducible experiments (15)*, *PRs (20)*
**Branch:** `feat/dvc-pipeline` → PR → `dev`
**Checkpoint:** a teammate on a fresh clone runs `dvc pull && dvc repro` and gets **identical metrics**

> **Execution note (2026-09-30):** as planned, Saad was the owner — but his session produced
> **PR #10** (`dev` → `main`, an M05-styled release PR) instead of this module's work
> (see REPORT § Known issues). Per team decision Uzair implemented M06 on `feat/dvc-pipeline`
> (PR **#11**), approved/merged PR #10 himself (his 2nd review, Saad's 2nd authored PR), and
> Saad's required **"changes requested"** review moved to **Module 07** (rubric needs it at
> least once project-wide, not per module).

## Objective

`prepare → train → evaluate` fully driven by `params.yaml`, seeded everywhere, preprocessing fit on
the training split only, commit SHA logged with every run.

## Tasks

### 1. Branch

```bash
git switch dev && git pull
git switch -c feat/dvc-pipeline
```

- [x] Done — branch from `dev` @ `ff05906`

### 2. `params.yaml` — every hyperparameter, split ratio and seed

Already in place since Module 02 (no hyperparameter lives in code):

```yaml
seed: 42

split:
  test_size: 0.2

data:
  raw_train: data/raw/train.csv
  raw_test: data/raw/test.csv
  processed_dir: data/processed
  target: satisfaction

train:
  model: random_forest
  n_estimators: 100
  max_depth: 6

paths:
  model: models/model.pkl
  metrics: metrics.json
```

- [x] No hyperparameter left in code
- [x] `seed: 42` at the top level

### 3. Stages in `dvc.yaml`

Final file (⚠️ corrected — the original sketch below used `- key:` trailing-colon
entries, which YAML parses as `{key: null}`; DVC then treats the **left side as a params
*file name*** (`- seed:` → a file called `seed`; `- data:` → the real **`data/` directory**,
which collided with the stage's own outputs and raised `CyclicGraphError`). Correct syntax
is colon-free strings for keys in the default `params.yaml`):

```yaml
stages:
  prepare:
    cmd: uv run python -m ml_skyline.prepare
    deps:
      - src/ml_skyline/prepare.py
      - src/ml_skyline/common.py
      - data/raw/train.csv
    params:
      - seed
      - split
      - data
    outs:
      - data/processed/train.csv
      - data/processed/test.csv

  train:
    cmd: uv run python -m ml_skyline.train
    deps:
      - src/ml_skyline/train.py
      - src/ml_skyline/pipeline.py
      - src/ml_skyline/common.py
      - data/processed/train.csv
    params:
      - seed
      - train
      - paths
      - data
    outs:
      - models/model.pkl

  evaluate:
    cmd: uv run python -m ml_skyline.evaluate
    deps:
      - src/ml_skyline/evaluate.py
      - src/ml_skyline/common.py
      - models/model.pkl
      - data/processed/test.csv
    params:
      - seed
      - train
      - paths
      - data
    metrics:
      - metrics.json:
          cache: false        # stays a plain git file (PDF: commit metrics.json)
```

- [x] `prepare`, `train`, `evaluate` stages defined
- [x] `evaluate` writes **`metrics.json`** (`cache: false` so it remains git-tracked)

### 4. Stage responsibilities

**`prepare.py`** (existed since M02)
- [x] Load raw CSV, drop `id`/`Unnamed: 0`, handle `Arrival Delay in Minutes` nulls
      (repaired/validated in code; imputation itself lives in the sklearn Pipeline)
- [x] Train/test split with `random_state=seed` and `stratify=y`
- [x] **Fit `SimpleImputer` / `StandardScaler` / `OneHotEncoder` on the training split only**
      via `ColumnTransformer` inside `Pipeline` (anti-leakage asserted in `tests/test_pipeline.py`)
- [x] Write `data/processed/{train,test}.csv`

**`train.py`**
- [x] Read `params.yaml` via `yaml.safe_load` (`ml_skyline.common.load_params`)
- [x] Set `random_state=seed` on the estimator
- [x] Fit on the processed training split
- [x] Persist `models/model.pkl` with `joblib`

**`evaluate.py`**
- [x] Compute accuracy, precision, recall, F1, ROC-AUC on the test split
- [x] Write `metrics.json`
- [x] **Log the current commit SHA** in `metrics.json` (`git rev-parse HEAD`)
- [x] `run_at` **removed** in M06 — a timestamp made every run rewrite `metrics.json`,
      churning `dvc.lock` and breaking the "byte-identical metrics" checkpoint.
      With `seed` + `commit_sha` only, evaluate is fully deterministic.
      (MLflow/W&B not needed; commit SHA inside `metrics.json` satisfies the PDF's "at minimum".)

### 5. Seeds everywhere randomness occurs

- [x] `train_test_split(random_state=seed)`
- [x] no `shuffle=True` without a seed
- [x] model `random_state=seed` (RandomForest, etc.)
- [x] no sampling/`df.sample` in the pipeline
- [x] `set_seed()` seeds `random` + `numpy.random` at stage entry (`ml_skyline.common`)

### 6. Run and commit

```bash
uv run dvc repro                 # -> dvc.lock
git add src/ml_skyline/evaluate.py dvc.yaml
git commit -m "feat: wire prepare/train/evaluate stages into dvc.yaml and make evaluate deterministic"   # 050ee1c
uv run dvc repro -f              # re-runs at the code commit so commit_sha matches
git add dvc.lock metrics.json
git commit -m "feat: add reproducible prepare/train/evaluate DVC pipeline"                                # 9e6ff42
uv run dvc push                  # 3 files (processed x2 + model.pkl)
git push -u origin feat/dvc-pipeline
```

- [x] `dvc.yaml`, `dvc.lock`, `params.yaml`, `metrics.json` all committed
- [x] `dvc push` **before** `git push` (3 files pushed, exit 0)
- [x] re-run after commit: `Data and pipelines are up to date.` + `git diff` empty

### 7. PR + reviewer reproduction

- [x] Title: `feat: reproducible DVC pipeline (prepare/train/evaluate)` → base `dev` — **PR #11**
- [~] Author **Saad**, reviewer **Uzair** → **deviation:** Uzair authored (Saad produced the
      wrong artifact — PR #10 — and was not looped back per team decision)
- [x] PR description: metrics before → after (unchanged: 0.9299 → 0.9299 at seed 42),
      `dvc.lock` recorded, seed 42, determinism change documented
- [x] **Fresh-clone reproduction** (Uzair, this machine, empty temp dir):
      `uv sync && dvc pull && dvc repro` → up to date, tree clean; `dvc repro -f` →
      all 9 value metrics identical — evidence
      `docs/evidence/module-06-dvc-repro-verification.txt`
- [~] **"Changes requested" at least once** → **moved to Module 07**: needs Saad's account on a
      Uzair-authored PR (an author cannot request changes on their own PR); scheduled for
      Saad's first M07 action.

## Checkpoint (evidence for REPORT.md)

- [x] Fresh clone: `uv sync && dvc pull && dvc repro` → identical metrics
      (value metrics byte-identical; `commit_sha` records each run's code commit by design)
- [x] `metrics.json` contains `commit_sha` and `seed`
- [x] `git diff HEAD -- dvc.lock` empty after re-running (plain `dvc repro` is a no-op)

## Pitfalls

- Preprocessing fitted on the whole dataset → **data leakage**, caught by the review checklist.
- `dvc.lock` not committed → teammates get a different pipeline.
- Absolute paths (`/home/kali/...`) → breaks on a teammate's machine.
- Committing `models/*.pkl` to git instead of `dvc push`.
- Editing code then running `dvc exp run` without committing → logged SHA ≠ code.
- **`params:` entries must NOT use trailing colons** (`- seed:` ≠ key `seed`; it means
  "file named `seed`"). Encountered live in this module — see §3.
