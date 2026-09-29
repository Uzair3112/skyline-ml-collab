# Module 02 · Scaffold the project and import the initial code

**Phase 2** · Owner: **both** · Rubric: *Repo hygiene (10)* + *Branching & protection (15)*
**Checkpoint:** three protected branches exist; `git log` on `main` shows the initial import.

## Objective

Create the standard layout, import the starter code as runnable CLI code with a pinned
environment, then create and protect `staging` and `dev`.

> **This is the only time anyone pushes directly to `main`.** ✅ done — push `5078478`.

## Final layout

```
.
├── configs/            # .gitkeep now; extra configs later
├── data/               # contents git-ignored by extension, tracked by DVC (M04)
├── models/             # ditto
├── notebooks/          # .gitkeep now; 01-eda.ipynb in M05
├── src/ml_skyline/      # reusable, tested code
├── tests/
├── .github/workflows/   # ci.yml in M08
├── docs/                # this folder
├── .gitignore
├── CONTRIBUTING.md      ✅
├── README.md            ✅
├── params.yaml          ✅
├── metrics.json         ✅
└── pyproject.toml + uv.lock   ✅
```

## Tasks

### 1. Directory skeleton — ✅ done

```bash
mkdir -p configs data/raw data/processed models notebooks src/ml_skyline tests .github/workflows
touch configs/.gitkeep data/raw/.gitkeep data/processed/.gitkeep models/.gitkeep \
      notebooks/.gitkeep .github/workflows/.gitkeep tests/__init__.py
```

Package name under `src/`: **`ml_skyline`** (importable, valid identifier — not the repo name),
wired up via `[tool.uv.build-backend] module-name = "ml_skyline"`.

### 2. `.gitignore` — ✅ done (plan corrected)

Required exclusions: **datasets, checkpoints, `.env`, `__pycache__/`, `.venv/`, `mlruns/`**.

> ⚠️ **Correction to the original plan.** The draft ignored `data/` and `models/` as *directories*.
> That is wrong for DVC: `dvc add data/raw/train.csv` must produce a **committable**
> `data/raw/train.csv.dvc`, and if `data/` is ignored the pointer is ignored too — teammates would
> get broken pointers and `dvc pull` would be impossible. So we ignore by **file extension**
> instead, which excludes every dataset file while leaving `*.dvc` and DVC's own `.gitignore`
> committable.

```gitignore
# Python
__pycache__ / *.py[oc] / build / dist / wheels / *.egg-info / .pytest_cache / .ruff_cache
# Environments & secrets
.venv/ venv/ env/ .env .env.* !.env.example *.pem *.key
# Datasets and trained artifacts — DVC owns the real files
*.csv *.tsv *.parquet *.feather *.arrow *.joblib *.pkl *.pickle *.h5 *.onnx *.ckpt
!tests/fixtures/*.csv          # CI needs a small committed sample
# Checkpoints
checkpoints/ lightning_logs/ *.pt
# ML tracking / notebooks
mlruns/ runs/ wandb/ dvc_plots/ .ipynb_checkpoints/
# DVC local-only credentials
.dvc/config.local
```

- [x] `.env`, `.venv/`, `__pycache__/`, `mlruns/`, checkpoints all covered
- [x] every CSV/model file excluded → verified with `git status --ignored`:
      `data/raw/{train,test}.csv`, `data/processed/{train,test}.csv`, `models/model.pkl` all `!!`
- [x] `git status -uall` shows the four `.gitkeep` pointers as tracked → DVC pointers will be too

### 3. Import starter code → `src/` — ✅ done

Source: <https://github.com/vrunm/Airline_Passenger_Satisfaction>
(`airline-passenger-satisfaction-eda-notebook.ipynb`, `-ml-notebook.ipynb`, `train.csv`, `test.csv`)

- [x] Refactored into `src/ml_skyline/`:
  - `common.py` — `REPO_ROOT`, `load_params`, `set_seed`, `TARGET_MAP`, `normalise_text`
  - `prepare.py` — **stage 1**: repair corrupted CSV, drop ids, encode target, seeded stratified split
  - `pipeline.py` — preprocessing + estimator, both parameter driven
  - `train.py` — **stage 2**: fit on the processed training split, save `models/model.pkl`
  - `evaluate.py` — **stage 3**: score the holdout, write `metrics.json` (+ `commit_sha`, `seed`)
- [x] Runnable from the CLI, no hardcoded paths anywhere:

  ```bash
  python -m ml_skyline.prepare && python -m ml_skyline.train && python -m ml_skyline.evaluate
  ```

- [x] Paths come from `params.yaml` and `REPO_ROOT = Path(__file__).resolve().parents[2]`
- [x] `tests/` has 17 tests, all green; includes
      `test_no_hardcoded_absolute_paths_in_source`
- [x] Starter notebooks deliberately **not** imported — they carry outputs and their logic is what
      `src/` now is. Credit the source link in `README.md` / `REPORT.md`. Module 05 writes a clean
      notebook.

**Two starter-code defects we fixed (put these in REPORT.md):**

| # | Defect in the starter | What we do |
|---|------------------------|------------|
| 1 | `train.csv` is **tab-corrupted**: headers like `Customer\tType` and labels like `satisfied\t\t\t` | `normalise_frame()` collapses all whitespace runs; after repair the columns match the clean `test.csv` exactly |
| 2 | `ColumnTransformer` listed only the 4 categorical columns with default `remainder='drop'`, so **every numeric feature was silently discarded**; and `y_test`/`X_test` were assigned from the *training* frame, so it scored on its own training data | explicit numeric + categorical transformers, proper seeded holdout split, `fit` only on the training split |

Result: **93.0 % accuracy / F1 0.919 / ROC-AUC 0.981** vs the starter's reported 78 %.

### 4. Pin the environment — ✅ done

- [x] `uv sync` + `uv lock --check` both pass
- [x] `uv.lock` committed alongside `pyproject.toml`
- [x] deps: `dvc`, `jupyter`, `jupytext`, `pandas`, `pre-commit`, `pytest`, `ruff`, `scikit-learn`
      — plus **`joblib`** and **`pyyaml`** made explicit (they were only transitive before)
- [x] `[tool.ruff]` and `[tool.pytest.ini_options]` added so local, pre-commit and CI agree

### 5. Initial import commits → `main` — ✅ done

```
819504f chore: scaffold project layout and gitignore
0d5a343 chore: pin environment with uv.lock
e55d526 feat: import airline satisfaction starter code as prepare/train/evaluate CLI
4d0ee14 chore: record baseline metrics from the initial import
5078478 docs: add CONTRIBUTING with branch, commit and merge rules
```

- [x] `git log` on `main` shows the initial import **(checkpoint)**
- [x] pushed **once** to `origin/main` — the only direct push to `main` in the whole project

Verified before pushing: `ruff check` clean · `ruff format --check` clean · `pytest` 17/17 ·
full pipeline re-run produced **byte-identical** `metrics.json` (minus `run_at`).

### 6. Create the long-lived branches — ✅ done

```bash
git switch -c staging && git push -u origin staging
git switch -c dev     && git push -u origin dev
```

- [x] `main`, `staging`, `dev` all exist on GitHub, all at `5078478`

### 7. Branch protection — ✅ done (applied via GitHub API)

Settings → Branches (or **Rulesets**) for **`main`**, **`staging`**, **`dev`**:

- [x] Require a pull request before merging
- [x] Require at least **1 approving review** (plus dismiss-stale-approvals)
- [x] Block **force pushes**
- [x] Do **not** allow direct pushes / deletions
- [x] `enforce_admins: true` — the rule binds admins too, which is the whole point
- [ ] (After Module 08) add **required status checks** = the four CI jobs — deliberately left **off**,
      because no checks exist yet
- [x] **Proven by test, not just by settings** — direct pushes to `dev` and `main` were attempted
      and rejected:

  ```
  remote: error: GH006: Protected branch update failed for refs/heads/dev.
  remote: - Changes must be made through a pull request.
   ! [remote rejected] HEAD -> dev (protected branch hook declined)
  ```

  Identical rejection for `refs/heads/main`. All three refs stayed at `5078478` — nothing changed.
  > Screenshots of the rules are nice to have, but `REPORT.md` only mandates screenshots of a
  > **blocked large file/secret** and of **red/green CI**.

**One-time repo housekeeping — ✅ done:**

- [x] Default branch switched from `chore/bootstrap` → **`main`**
- [x] **`chore/bootstrap`** and **`chore/saad-setup`** deleted (both were ancestors of `main`)
- [x] Remaining: `main` (default), `staging`, `dev` — **all three protected**

### 8. `CONTRIBUTING.md` — ✅ done

- [x] Branch naming rules (`feat/`, `data/`, `exp/`, `fix/` + the three permanent branches)
- [x] Conventional Commits with a type table
- [x] **Merge strategy decided once:** *squash-merge PRs into `dev`*; rebase/merge-commit into
      `staging`/`main`
- [x] `dvc push` before `git push`
- [x] never run experiments on uncommitted code
- [x] reviewer must check out the branch for any pipeline-changing PR

## Checkpoint (evidence for REPORT.md)

- [x] Three branches protected — **proved** by `GH006: Changes must be made through a pull request`
      on both `dev` and `main` (refs untouched at `5078478`)
- [x] `git log --oneline` on `main` shows the import commits
- [x] `git log --format='%an' | sort -u` shows both members

## Pitfalls (avoided)

- Pushing the CSV "just for now" → `.gitignore` blocks it by extension from the first commit.
- Skipping `uv.lock` → `uv.lock` committed and `uv lock --check` enforced.
- Creating `dev` from `main` *before* the import → created **after** the import, from `main`.

## Status

| Item | Status |
|------|--------|
| Tasks 1–6, 8 | ✅ |
| Task 7 branch protection + default-branch switch + delete 2 chore branches | ✅ |
| Proof that a direct push is rejected | ✅ `GH006` on `dev` and `main` |
| Documentation close-out PR → `dev` | 🟡 **PR #2 awaiting Saad's review** |
| **Instructor added as viewer** | ⬜ **blocked — need their GitHub username** |
| 📸 optional: collaborators + protection screenshots | ⬜ Uzair |
