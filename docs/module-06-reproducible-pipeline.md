# Module 06 · A reproducible pipeline

**Phase 6** · Owner: **Saad** (Model owner), **Uzair** (reviewer) · Rubric: *Reproducible experiments (15)*, *PRs (20)*
**Branch:** `feat/dvc-pipeline` → PR → `dev`
**Checkpoint:** a teammate on a fresh clone runs `dvc pull && dvc repro` and gets **identical metrics**.

## Objective

`prepare → train → evaluate` fully driven by `params.yaml`, seeded everywhere, preprocessing fit on
the training split only, commit SHA logged with every run.

## Tasks

### 1. Branch

```bash
git switch dev && git pull
git switch -c feat/dvc-pipeline
```

### 2. `params.yaml` — every hyperparameter, split ratio and seed

```yaml
seed: 42

split:
  test_size: 0.2

prepare:
  raw_data: data/raw/train.csv
  processed_dir: data/processed
  target: satisfaction

train:
  model: random_forest
  n_estimators: 100
  max_depth: 6

evaluate:
  metrics_path: metrics.json
```

- [ ] No hyperparameter left in code
- [ ] `seed: 42` at the top level

### 3. Stages in `dvc.yaml`

```yaml
stages:
  prepare:
    cmd: python -m ml_skyline.prepare
    deps:
      - src/ml_skyline/prepare.py
      - data/raw/train.csv
    params:
      - prepare:
      - seed:
    outs:
      - data/processed/train.csv
      - data/processed/test.csv

  train:
    cmd: python -m ml_skyline.train
    deps:
      - src/ml_skyline/train.py
      - data/processed/train.csv
    params:
      - train:
      - seed:
    outs:
      - models/model.pkl

  evaluate:
    cmd: python -m ml_skyline.evaluate
    deps:
      - src/ml_skyline/evaluate.py
      - models/model.pkl
      - data/processed/test.csv
    params:
      - train:
      - seed:
    metrics:
      - metrics.json
    outs: []
```

- [ ] `prepare`, `train`, `evaluate` stages defined
- [ ] `evaluate` writes **`metrics.json`**

### 4. Stage responsibilities

**`prepare.py`**
- [ ] Load raw CSV, drop `id`/`Unnamed: 0`, handle `Arrival Delay in Minutes` nulls
- [ ] Train/test split with `random_state=seed` and `stratify=y`
- [ ] **Fit `SimpleImputer` / `StandardScaler` / `OneHotEncoder` on the training split only**,
      then `transform` the test split (use `sklearn.compose.ColumnTransformer` inside a `Pipeline`
      so leakage is impossible)
- [ ] Write `data/processed/{train,test}.csv` (or `.parquet`)

**`train.py`**
- [ ] Read `params.yaml` via `dvc.api.params` or `yaml.safe_load`
- [ ] Set `random_state=seed` on the estimator
- [ ] Fit on the processed training split
- [ ] Persist `models/model.pkl` with `joblib`/`pickle`

**`evaluate.py`**
- [ ] Compute accuracy, precision, recall, F1, ROC-AUC on the test split
- [ ] Write `metrics.json`
- [ ] **Log the current commit SHA** in `metrics.json`:

```python
import subprocess, json, datetime

sha = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
meta = {"commit_sha": sha, "run_at": datetime.datetime.now(datetime.UTC).isoformat(), "seed": seed}
```

  (MLflow/W&B optional; commit SHA inside `metrics.json` satisfies the PDF's "at minimum".)

### 5. Seeds everywhere randomness occurs

- [ ] `train_test_split(random_state=seed)`
- [ ] any `shuffle=True` → `random_state=seed`
- [ ] model `random_state=seed` (RandomForest, etc.)
- [ ] any sampling / `df.sample` → `random_state=seed`
- [ ] `np.random.seed(seed)` at module entry where needed

### 6. Run and commit

```bash
uv run dvc repro
cat metrics.json                 # note the numbers
git add dvc.yaml dvc.lock params.yaml metrics.json src/ tests/
git commit -m "feat: add reproducible prepare/train/evaluate DVC pipeline"
dvc push                         # models/ + data/processed
git push -u origin feat/dvc-pipeline
```

- [ ] `dvc.yaml`, `dvc.lock`, `params.yaml`, `metrics.json` all committed
- [ ] `dvc push` **before** `git push`

### 7. PR + reviewer reproduction

- [ ] Title: `feat: reproducible DVC pipeline (prepare/train/evaluate)` → base `dev`
- [ ] Author **Saad**, reviewer **Uzair**
- [ ] PR description: metrics before → after, `dvc.lock` hash, seed
- [ ] **Uzair checks out the branch fresh** and runs `dvc pull && dvc repro`, confirms metrics match
- [ ] **Uzair requests changes at least once here** (M07 requires a "changes requested" review) —
      e.g. note that `Arrival Delay` imputation must be fit on train only, or that `metrics.json`
      lacks `commit_sha`, then Saad pushes a fix.

## Checkpoint (evidence for REPORT.md)

- [ ] Fresh clone: `uv sync && dvc pull && dvc repro` → byte-identical `metrics.json`
- [ ] `metrics.json` contains `commit_sha` and `seed`
- [ ] `git diff HEAD -- dvc.lock` is empty after re-running (pipeline is up to date)

## Pitfalls

- Preprocessing fitted on the whole dataset → **data leakage**, caught by the review checklist.
- `dvc.lock` not committed → teammates get a different pipeline.
- Absolute paths (`/home/kali/...`) → breaks on a teammate's machine.
- Committing `models/*.pkl` to git instead of `dvc push`.
- Editing code then running `dvc exp run` without committing → logged SHA ≠ code.
