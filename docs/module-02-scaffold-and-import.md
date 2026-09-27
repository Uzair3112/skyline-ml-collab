# Module 02 · Scaffold the project and import the initial code

**Phase 2** · Owner: **both** · Rubric: *Repo hygiene (10)* + *Branching & protection (15)*
**Checkpoint:** three protected branches exist; `git log` on `main` shows the initial import.

## Objective

Create the standard layout, import the starter code as runnable CLI code with a pinned
environment, then create and protect `staging` and `dev`.

> **This is the only time anyone pushes directly to `main`.**

## Final layout to create

```
.
├── configs/            # params.yaml (or at root — pick one, we use root params.yaml + configs/)
├── data/               # git-ignored, DVC-tracked
├── models/             # git-ignored, DVC-tracked
├── notebooks/
├── src/                # reusable, tested code
├── tests/
├── .github/workflows/
├── docs/               # module plans (this folder)
├── .gitignore
├── .pre-commit-config.yaml   # added in Module 03
├── CONTRIBUTING.md
├── README.md
└── pyproject.toml + uv.lock
```

## Tasks

### 1. Directory skeleton

```bash
mkdir -p configs data/raw data/processed models notebooks src/ml_skyline tests .github/workflows
touch data/raw/.gitkeep models/.gitkeep tests/__init__.py
```

Package name under `src/`: **`ml_skyline`** (importable, valid identifier — not the repo name).

### 2. `.gitignore` (must satisfy the PDF)

Required exclusions: **datasets, checkpoints, `.env`, `__pycache__/`, `.venv/`, `mlruns/`**.

```gitignore
# Python
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info
.pytest_cache/
.ruff_cache/

# Environments & secrets
.venv/
env/
.env
.env.*

# Data & models (DVC owns these)
data/
models/
*.csv
*.parquet
*.joblib
*.pkl
*.h5

# ML tracking / experiment leftovers
mlruns/
runs/
wandb/
.ipynb_checkpoints/

# DVC local-only credentials
.dvc/config.local
```

- [ ] `.env`, `.venv/`, `__pycache__/`, `mlruns/` all covered
- [ ] `data/` and `models/` ignored so no CSV can ever be committed by accident

### 3. Import starter code → `src/`

Source: <https://github.com/vrunm/Airline_Passenger_Satisfaction>
(`airline-passenger-satisfaction-eda-notebook.ipynb`, `-ml-notebook.ipynb`, `train.csv`, `test.csv`)

- [ ] Refactor the ML notebook's logic into `src/ml_skyline/{prepare,train,evaluate}.py`
- [ ] Runnable from CLI: `python -m ml_skyline.train` **or** `python src/train.py`
- [ ] **Remove every hardcoded absolute path** — use `pathlib.Path(__file__).resolve().parents[1]`
      and read paths from `params.yaml`
- [ ] Keep the original notebooks as-is for now (Module 05 rewrites them properly)
- [ ] `tests/` gets at least one smoke test so `pytest` is non-empty from day one

### 4. Pin the environment

Already done: `uv.lock` exists. Verify:

```bash
uv sync
uv lock --check
```

- [ ] `uv.lock` committed alongside `pyproject.toml`
- [ ] dependencies include: `dvc`, `jupyter`, `jupytext`, `pandas`, `pre-commit`, `pytest`, `ruff`,
      `scikit-learn` (already present)

### 5. Initial import commits → `main`

Small, well-described commits. Suggested sequence:

```
chore: scaffold project layout
chore: pin environment with uv.lock
feat: import airline satisfaction starter code
docs: add README and CONTRIBUTING
chore: expand .gitignore for data, models and secrets
```

```bash
git add -A
git commit -m "chore: scaffold project layout"
git push -u origin main          # ← ONLY direct push to main in the whole project
```

- [ ] `git log --oneline` on `main` shows the initial import (checkpoint)

### 6. Create the long-lived branches

```bash
git switch -c staging && git push -u origin staging
git switch -c dev     && git push -u origin dev
git switch main
```

- [ ] `main`, `staging`, `dev` all exist on GitHub

### 7. Branch protection (Uzair + Saad)

Settings → Branches (or **Rulesets**) for `main`, `staging`, `dev`:

- [ ] Require a pull request before merging
- [ ] Require at least **1 approving review**
- [ ] Block **force pushes**
- [ ] Do **not** allow direct pushes / deletions
- [ ] (After Module 08) add **required status checks** = the four CI jobs

### 8. `CONTRIBUTING.md`

Must state:

- [ ] Branch naming rules → `feat/`, `data/`, `exp/`, `fix/` (table from `docs/00-overview.md`)
- [ ] Commit convention → **Conventional Commits**
      (`feat:`, `fix:`, `data:`, `exp:`, `chore:`, `ci:`, `docs:`, `test:`)
- [ ] Merge strategy decision → **squash-merge PRs into `dev`**, rebase/merge-commit into
      `staging`/`main`. Written down once, as the PDF requires.
- [ ] `dvc push` before `git push`
- [ ] Never run experiments on uncommitted code
- [ ] Reviewer must check out the branch for any PR touching the pipeline

## Checkpoint (evidence for REPORT.md)

- [ ] Screenshot: three branches with protection rules visible
- [ ] `git log --oneline` on `main` shows the import commits
- [ ] `git log --format='%an' | sort -u` shows both members (once they commit)

## Pitfalls

- Pushing the CSV "just for now" → it lands in history and needs `git filter-repo` to remove.
- Skipping `uv.lock` → Phase 9 `uv sync` diverges.
- Creating `dev` from `main` *before* the import → `dev` misses the scaffold.
  (PDF says `dev` is created from `staging`, `staging` from `main`, after the import.)
