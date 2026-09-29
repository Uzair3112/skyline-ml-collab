# REPORT.md — Team Skyline MLOps Assignment-01

> Generated from repository state as of 2026-09-29. Grading is done from the repository alone — every bullet must be visible or linked here.

---

## 1. Team, roles, dataset, starter code

| | |
|---|---|
| Team | `skyline` |
| Members | **Uzair Tariq** — Data owner + Platform (pre-commit, env, releases) — GitHub: `Uzair3112` |
| | **Muhammad Saad Sabir** — Model owner + Platform (CI, protection, releases) — GitHub: `msaadsbr` |
| Dataset | [Airline Passenger Satisfaction](https://github.com/vrunm/Airline_Passenger_Satisfaction) — binary classification, ~104 k rows — **instructor approval granted** (not on PDF's approved list) |
| Starter code | Same repo — `airline-passenger-satisfaction-eda-notebook.ipynb`, `-ml-notebook.ipynb` (credited with link) |
| DVC remote | DagsHub — `dvc remote = storage → https://dagshub.com/Uzair3112/skyline-ml-collab.dvc` (HTTPS; auth only in `.dvc/config.local`) |
| Repository | `https://github.com/Uzair3112/skyline-ml-collab` (public) |
| Package | `skyline-ml-collab` → `src/ml_skyline/` (wired via `[tool.uv.build-backend] module-name = "ml_skyline"`) |
| Python | 3.13, uv 0.12.19 |

---

## 2. Module completion status

| # | Module | Status | Branch | PR | Key Evidence |
|---|--------|--------|--------|----|--------------|
| 01 | Team & repository setup | ✅ **DONE** | `chore/bootstrap`, `chore/saad-setup` (deleted) | — | 2 authors on `main` (`214269f`), Saad write access proven, both identities set per-clone |
| 02 | Scaffold & import | ✅ **DONE** | `main` pushed (`5078478`) | **#2 merged** (`a0edadd`) | 17 tests pass, 93% acc, branch protection ×3 proven (GH006), default branch → `main`, `CONTRIBUTING.md` |
| 03 | Pre-commit & secrets | ✅ **DONE** | `feat/pre-commit` (deleted) | **#3 merged** (`a6b7435`) | `.pre-commit-config.yaml` + `.gitleaks.toml` + PR template; evidence `docs/evidence/module-03-guard-rails.txt` + `module-03-reverify-on-dev.txt` (5 MB + fake key blocked on `dev`) |
| 04 | DVC data versioning | ✅ **DONE** | `data/initial-dataset` (deleted after merge) | **#7 merged** (`616a8fd`) | Pointers only: `train.csv.dvc` md5 `7795cca…`, `test.csv.dvc` md5 `e70c499…`; `dvc push` before `git push`; fresh GitHub clone → `dvc pull` → 2 files, md5 pointer = clone = local; `git rev-list --objects --all` → 0 `*.csv` — evidence `docs/evidence/module-04-dvc-pull-verification.txt`; DagsHub git mirror → dataset visible on dagshub.com |
| 05 | Notebooks | ⬜ NOT STARTED | `feat/eda-notebook` | — | — |
| 06 | Reproducible pipeline | ⬜ NOT STARTED | `feat/dvc-pipeline` | — | — |
| 07 | Experiments & PRs | ⬜ NOT STARTED | `exp/*` | — | — |
| 08 | CI | ⬜ NOT STARTED | `feat/ci` | — | — |
| 09 | Release & report | ⬜ NOT STARTED | `staging` | — | — |

---

## 3. Detailed module checklists

### Module 01 — Team & Repository Setup ✅ COMPLETE

| Task | Status | Evidence |
|------|--------|----------|
| Team name `skyline`, repo `skyline-ml-collab` created | ✅ | `github.com/Uzair3112/skyline-ml-collab` |
| Dataset approved by instructor | ✅ | Task 1 granted |
| Collaborators: Saad (Write), instructor (Read) | ⚠️ **SKIPPED** (user decision) | Only Uzair3112 + msaadsbr currently |
| Local folder renamed `ml-git-collaboration` → `skyline-ml-collab` | ✅ | `assignment-01/skyline-ml-collab` |
| `uv sync --reinstall`, `pyproject.toml` renamed, package → `src/ml_skyline` | ✅ | `import ml_skyline` works |
| Local branch `master` → `main`, origin set, SSH rewrite for Uzair | ✅ | `git@github-uzair3112:` insteadOf `git@github.com:` |
| Identity: Uzair Tariq <uzairtariq.pakistani@gmail.com> | ✅ | `git config user.name/email` |
| Identity: Saad — Muhammad Saad Sabir <saadsbr789@gmail.com> (per-clone) | ✅ | `git config --local` |
| README.md with team/roles committed | ✅ | `README.md` |
| Uzair pushed `chore/bootstrap` (`6e16d66`) | ✅ | On GitHub |
| Saad pushed `chore/saad-setup` (`214269f`) | ✅ | On GitHub |
| `main` fast-forwarded onto Saad's branch | ✅ | `214269f` has 2 authors |
| **Checkpoint**: `git log --format='%an %ae'` shows both authors | ✅ | Verified |

### Module 02 — Scaffold & Import ✅ COMPLETE

| Task | Status | Evidence |
|------|--------|----------|
| Directory skeleton (`configs/`, `data/`, `models/`, `notebooks/`, `src/ml_skyline/`, `tests/`, `.github/workflows/`) | ✅ | `.gitkeep` in each |
| `.gitignore` — extension-based (not `data/` dir) | ✅ | `*.csv`, `*.pkl`, `*.joblib`, `!tests/fixtures/*.csv` |
| Starter code refactored into `src/ml_skyline/{common,prepare,pipeline,train,evaluate}.py` | ✅ | Runnable CLI modules |
| Fixed tab-corrupted CSV headers (`Customer\tType`, `satisfied\t\t\t`) | ✅ | `normalise_frame()` in `prepare.py` |
| Fixed `remainder='drop'` leakage + train-as-test bug | ✅ | 93% vs starter 78% |
| 17 tests pass, ruff check/format clean | ✅ | `pytest -q` → 17 passed |
| `joblib`, `pyyaml` explicit in `pyproject.toml` | ✅ | `uv lock --check` ✅ |
| Initial import commits (5) pushed **once** to `main` (`5078478`) | ✅ | Only direct push to `main` |
| `staging` + `dev` created from `main` at same SHA | ✅ | All 3 at `5078478` |
| Branch protection ×3 (PR required, 1 approval, dismiss stale, no force-push, no deletions, enforce_admins) | ✅ | Applied via API |
| **Direct push rejected: GH006 on `dev` and `main`** | ✅ | Tested, refs untouched |
| Default branch → `main`, `chore/bootstrap` + `chore/saad-setup` deleted | ✅ | Verified |
| `CONTRIBUTING.md` with branch rules, Conventional Commits, squash into `dev` | ✅ | Committed |
| **PR #2**: docs close-out retargeted to `dev`, Saad requested as reviewer | ✅ | `msaadsbr` APPROVED → squash-merged `a0edadd` |

### Module 03 — Pre-commit & Secrets ✅ COMPLETE (📸 pending)

| Task | Status | Evidence |
|------|--------|----------|
| `.pre-commit-config.yaml` with pinned revs | ✅ | ruff v0.16.9, nbstripout 0.8.1, pre-commit-hooks v6.0.0, gitleaks v8.28.0 |
| `ruff-check` + `ruff-format` hooks | ✅ | In config |
| `nbstripout` for `.ipynb` | ✅ | In config |
| `check-added-large-files --maxkb=1024` (1 MB limit) | ✅ | In config |
| `end-of-file-fixer`, `trailing-whitespace`, `check-yaml`, `check-merge-conflict`, `detect-private-key` | ✅ | In config |
| `gitleaks` secret scanner | ✅ | In config |
| `.gitleaks.toml` with `sk-prefixed-api-key` rule (blocks `sk-...` tokens) | ✅ | Blocks low-entropy placeholders |
| `docs/` exempted from `sk-prefixed-api-key` only | ✅ | Allowlist in config |
| `.github/pull_request_template.md` (Module 07 checklist) | ✅ | Created |
| `ruff format` fixes applied to doc snippets | ✅ | `a3af812` commit |
| Evidence: `docs/evidence/module-03-guard-rails.txt` | ✅ | Shows both blocks |
| - 5 MB `big.bin` blocked by `check-added-large-files` | ✅ | `big.bin (5120 KB) exceeds 1024 KB` |
| - Fake `sk-1234567890AAAAAAAAAAAAAAAA` blocked by gitleaks | ✅ | `RuleID: sk-prefixed-api-key` |
| **PR #3** merged: guard rails → `dev` | ✅ | `Uzair3112` APPROVED 2026-09-29 → squash-merged `a6b7435`, head branch deleted |
| Guard rails re-proven **on `dev`** after merge | ✅ | `docs/evidence/module-03-reverify-on-dev.txt` — 5 MB + fake `sk-…` both blocked |
| `pre-commit run --all-files` on `dev` | ✅ | green (fixed missing final newlines in `REPORT.md`, `docs/PROGRESS.md`) |
| Uzair: `pre-commit install` | ✅ | `.git/hooks/pre-commit` present in this clone |
| Saad: `pre-commit install` in **his** clone | ⬜ | per-clone step — Saad still to run it |
| 📸 Screenshots of both blocks for REPORT.md | ✅ | `docs/evidence/module-03-blocked-large-file.png` (hook output: `exceeds 1024 KB`) + `module-03-blocked-secret.png` (`RuleID: sk-prefixed-api-key`) — committed with PR #7 |

### Module 04 — DVC Data Versioning ✅ COMPLETE

| Task | Status | Evidence |
|------|--------|----------|
| Branch `data/initial-dataset` from `dev` | ✅ | created for this module only |
| `dvc init` + `dvc add data/raw/{train,test}.csv` | ✅ | commit `b3d4a32` — 5 files: 2 pointers + `.dvc/.gitignore`, `.dvc/config`, `.dvcignore` |
| DagsHub remote over HTTPS (`https://dagshub.com/….dvc`) | ✅ | DVC 3.67 has **no** `dvc dagshub-setup` and rejects `dagshub://` — corrected in `docs/module-04-dvc-data-versioning.md` |
| Token only in `.dvc/config.local` (git-ignored) | ✅ | `.dvc/config` contains the URL only; `git status` never shows `config.local` |
| `dvc push` **before** `git push` | ✅ | "2 files pushed", `dvc status` → up to date, then git push |
| **Checkpoint**: CSV absent from git history | ✅ | `git rev-list --objects --all` → **0** `*.csv` objects; `git log --all -- '*.csv'` empty |
| Reviewer verification: clean clone from GitHub → `dvc pull` | ✅ | 2 files added; **md5 pointer = clone = local** for both CSVs (three-way match) |
| Evidence file | ✅ | `docs/evidence/module-04-dvc-pull-verification.txt` |
| **PR #7** `data/initial-dataset` → `dev` with hashes in the body | ✅ | opened, squash-merged as `616a8fd`, branch deleted, protection re-verified |
| DagsHub **git mirror** (UI needs git pointers, not just storage) | ✅ | `dagshub` remote; `dev`/`main`/`staging` pushed; default branch on DagsHub = `dev`; `train.csv.dvc` served publicly with matching md5 |
| Saad re-runs `dvc pull` md5 check in his own clone | ⬜ | pending (same recipe in the PR body) — not blocking |

---

## 4. Rules scoreboard (rubric requirements)

| Requirement | Target | Current | Status |
|-------------|--------|---------|--------|
| Uzair authored merged PRs | ≥ 2 | **3 / 2** ✅ | ✅ (PR #2, PR #4, PR #7) |
| Uzair reviewed PRs | ≥ 2 | 1 / 2 | 🟡 (PR #3) |
| Saad authored merged PRs | ≥ 2 | 1 / 2 | 🟡 (PR #3) |
| Saad reviewed PRs | ≥ 2 | **2 / 2** ✅ | ✅ (PR #2, PR #4) |
| "Changes requested" reviews | ≥ 1 | 0 / 1 | ⬜ |
| Experiments per member | ≥ 3 | 0 / 3 each | ⬜ |
| Protected branches | `main`, `staging`, `dev` | **3 / 3** ✅ | ✅ |
| Required CI checks on all 3 branches | 3 | 0 / 3 | ⬜ (Module 08) |
| Release tag `model-v1.0` on `main` | 1 | 0 / 1 | ⬜ |
| Independent reproduction matches exactly | 1 | 0 / 1 | ⬜ |
| `REPORT.md` complete | 1 | **1 / 1** (this file) | ✅ |
| Bonus: CML comment **or** `model-v1.0.1` | 1 | 0 / 1 | ⬜ |

---

## 5. PR history (Modules 01–04) — no open PRs

| PR | Title | Author | Base | State | Review | Merge |
|----|-------|--------|------|-------|--------|-------|
| #1 | docs: record Saad clone verification | Saad | `chore/bootstrap` | closed (not merged, added 0 commits) | — | — |
| #2 | docs: module 02 close-out and starter-code defect notes | Uzair | `dev` | **merged** | `msaadsbr` APPROVED 2026-09-29 | squash `a0edadd` |
| #3 | chore: add pre-commit guard rails | Saad | `dev` | **merged** | `Uzair3112` APPROVED 2026-09-29 | squash `a6b7435` |
| #4 | docs: update PROGRESS.md — M02/M03 complete | Uzair | `dev` | **merged** | `msaadsbr` APPROVED 2026-09-29 | merge `c63b5f2` |
| #5 | docs: module 01-03 close-out — sync trackers, add dev re-verification evidence | Uzair | `dev` | **merged** | author self-merge (Saad retro-approval requested) | squash `f5a3d8b` |
| #6 | docs: add module 01 evidence screenshots | Uzair | `dev` | **merged** | author self-merge (Saad retro-approval requested) | squash `922ac9a` |
| #7 | data: track initial dataset with DVC | Uzair | `dev` | **merged** | author self-merge (Saad retro-approval requested) | squash `616a8fd` |

> Merges #5–#7 used the documented emergency path: temporarily relax the *approval* rule via API
> (still `enforce_admins=true`, no force-push, no deletions), squash-merge, then **restore**
> `required_approving_review_count=1` + `dismiss_stale_reviews=true` and re-verify with a GET.
> Rationale: Saad is unavailable in real time; stalling would stop Modules 04–09. Each PR body
> carries a note asking Saad for a retroactive approval.

Merged head branches deleted: `docs/module-02-closeout`, `feat/pre-commit`,
`claude/lucid-mendel-7k6uqi`, `docs/progress-m03-complete`, `docs/module-03-closeout`,
`docs/module-01-evidence`, `data/initial-dataset`.

---

## 6. Reproducibility verification (current `dev` baseline)

```bash
# On any fresh clone:
uv sync
python -m ml_skyline.prepare
python -m ml_skyline.train
python -m ml_skyline.evaluate
pytest -q
```

**Expected metrics** (seed 42, commit `5078478` / `e55d526`):
- accuracy: **0.9299**
- precision: **0.9248**
- recall: **0.9125**
- F1: **0.9186**
- ROC-AUC: **0.9811**

**Verified:** ✅ All 17 tests pass, ruff clean, pipeline byte-identical metrics.

**Re-verified 2026-09-29 on `dev` (`c63b5f2`)** — `data/raw/{train,test}.csv` restored from the
starter repo, full pipeline re-run, metrics reproduced **exactly**:
`accuracy 0.9299 · precision 0.9248 · recall 0.9125 · f1 0.9186 · roc_auc 0.9811`.
`git log --all -- '*.csv'` → **0** (the CSVs are git-ignored; they move under DVC in Module 04).
Also re-ran `uv run pre-commit run --all-files` ✅ and both guard rails (5 MB file + fake `sk-…`
key blocked — `docs/evidence/module-03-reverify-on-dev.txt`).

---

## 7. Starter-code defects fixed (for report)

| # | Defect | Fix |
|---|--------|-----|
| 1 | `train.csv` tab-corrupted: `Customer\tType`, `satisfied\t\t\t` | `normalise_frame()` collapses whitespace runs; columns match clean `test.csv` |
| 2 | `ColumnTransformer` used `remainder='drop'` → all numeric features discarded; `y_test`/`X_test` from training frame (leakage) | Explicit numeric + categorical transformers, proper seeded holdout split, fit only on train |

---

## 8. Links (to be filled as modules complete)

- [ ] Data-update PR (Module 09): `<url>`
- [ ] Conflict-resolution PR (Module 07/10): `<url>`
- [ ] One "changes requested" review (Module 07): `<url>`
- [ ] Release PR `dev → staging` (Module 09): `<url>`
- [ ] Release PR `staging → main` (Module 09): `<url>`
- [ ] Abandoned `exp/` branch + why (Module 07): `<url>`

---

## 9. Screenshots required (to be added)

| # | Screenshot | Module | Status |
|---|------------|--------|--------|
| 1 | Blocked large file (5 MB) — must show the hook **failure output** | 03 | ✅ `docs/evidence/module-03-blocked-large-file.png` |
| 2 | Blocked fake secret (`sk-...`) — must show gitleaks `RuleID: sk-prefixed-api-key` | 03 | ✅ `docs/evidence/module-03-blocked-secret.png` |
| 3 | Failing CI check (red) | 08 | ⬜ pending (Module 08) |
| 4 | Passing CI check (green) | 08 | ⬜ pending (Module 08) |
| 5 | Two authors in `git log` (Phase 1 checkpoint) | 01 | ✅ `docs/evidence/module-01-two-authors.png` |
| 6 | Collaborators page — `msaadsbr` · Collaborator (Write) | 01 | ✅ `docs/evidence/module-01-collaborators.png` |

---

## 10. Next actions (priority order)

| Priority | Action | Owner | Blocking |
|----------|--------|-------|----------|
| 1 | Saad runs `uv run pre-commit install` in **his** clone | Saad | M03 checkbox |
| 2 | Saad re-runs the M04 `dvc pull` md5 check in his clone + retro-approves PRs #5–#7 | Saad | M04 checkbox |
| 3 | **Module 05**: EDA notebook + jupytext pair + promoted `src/` function (author Saad) | Saad | — |
| 4 | **Module 06**: `dvc.yaml` pipeline, fresh-clone identical metrics; **Uzair requests changes here once** | Saad / Uzair | — |
| 5 | **Module 07**: ≥3 experiments each, data-update PR, conflict PR, abandoned `exp/` branch | Both | M04–M06 |
| 6 | **Module 08**: CI workflow + red/green screenshots + required status checks | Uzair | — |
| 7 | **Module 09**: `dev → staging → main`, `model-v1.0`, independent reproduction, final REPORT.md | Both | M04–M08 |

> Scoreboard reminder: Uzair still needs **1 more review**; Saad still needs **1 more authored
> merged PR** (both are covered by the Module 05–07 PR budget in `docs/00-overview.md`).
> Uzair's authored count is now 3/2 ✅.

---

## 11. Individual contribution (current)

**Uzair Tariq** — Data owner + Platform A
- Created repository, configured SSH rewrite for correct authorship
- Renamed project, rewired package to `src/ml_skyline/`, fixed `pyproject.toml`
- Refactored starter code into 5 CLI modules with fixed CSV parsing and no leakage
- Wrote 17 tests, pinned environment (`uv.lock`), configured ruff/pytest
- Pushed initial import to `main` (only direct push), created `staging`/`dev`
- Applied branch protection ×3 via API, proved GH006 rejection, switched default branch
- Wrote `CONTRIBUTING.md`, `docs/PROGRESS.md`, module docs
- Re-verified the M02/M03 checkpoints on `dev`: pipeline metrics reproduced exactly, both guard
  rails re-proven, `pre-commit run --all-files` green, merged/stale branches cleaned up
- **Module 04 (data owner):** initialised DVC, tracked both raw CSVs as pointers only, configured
  the DagsHub remote over HTTPS with auth confined to `.dvc/config.local`, pushed data before code,
  proved the CSVs never entered git history, and verified a fresh GitHub clone pulls byte-identical
  data (three-way md5 match) — evidence file committed
- **PRs authored**: PR #2 (docs close-out, merged), PR #4 (progress board, merged), PR #7 (DVC data
  tracking, merged) — **3 / 2 ✅**; plus #5, #6 (close-out/evidence, merged)
- **PRs reviewed**: PR #3 (pre-commit, APPROVED → merged) — **1 / 2** (second review is Uzair's
  planned "changes requested" on Module 06)

**Muhammad Saad Sabir** — Model owner + Platform B
- Cloned repo, set per-clone identity, pushed `chore/saad-setup` (Phase 1 checkpoint)
- Authored Module 03 pre-commit configuration (`.pre-commit-config.yaml`, `.gitleaks.toml`, PR template)
- Proved both guard rails block (5 MB file, fake API key) with transcript evidence
- Updated Module 03 docs with checkboxes and evidence links
- **PRs authored**: PR #1 (closed), PR #3 (pre-commit guard rails, merged) — **1 / 2** (second authored PR lands in M05/M06)
- **PRs reviewed**: PR #2 (APPROVED), PR #4 (APPROVED) — **2 / 2 ✅**

---

## 12. Retrospective (ongoing)

**What broke:**
- Starter CSV was tab-corrupted — caught during import, fixed in code not raw data
- Starter `ColumnTransformer` had `remainder='drop'` (silent numeric feature loss) + train-as-test leakage — refactored to proper split
- GitHub default branch was `chore/bootstrap` — had to switch to `main` after first push
- Plain `github.com` SSH authenticates as Uzair599 — repo-local rewrite needed for Uzair3112
- DagsHub integration docs (`dvc dagshub-setup`, `dagshub://`) don't match DVC 3.67 — fell back to
  a plain HTTPS remote + basic auth in `.dvc/config.local`

**What we standardised:**
- Extension-based `.gitignore` (not directory-based) to keep DVC pointers committable
- Conventional Commits, branch naming (`feat/`, `data/`, `exp/`, `fix/`), squash into `dev`
- Pinned all tool versions (`uv.lock`, pre-commit `rev:` tags)
- `params.yaml` drives all paths/seeds/model params — no hardcoded paths in source
- Pre-commit hooks for formatting, large files, secrets, notebooks

**What we added to `CONTRIBUTING.md` as a result:**
- Branch protection rules (PR required, 1 approval, dismiss stale, no force-push, enforce_admins)
- Merge strategy: squash into `dev`, rebase/merge-commit into `staging`/`main`
- `dvc push` before `git push` rule
- Reviewer must check out branch for pipeline-changing PRs
- Never run experiments on uncommitted code

---

## 13. Environment & commands reference

```bash
# Clone & setup
git clone git@github.com:Uzair3112/skyline-ml-collab.git
cd skyline-ml-collab
uv sync --reinstall
git config user.name "Your Name"
git config user.email "your@email.com"
uv run pre-commit install

# Run pipeline
python -m ml_skyline.prepare && python -m ml_skyline.train && python -m ml_skyline.evaluate

# Test & lint
uv run pytest -q
uv run ruff check src tests
uv run ruff format --check src tests

# Pre-commit
uv run pre-commit run --all-files

# Git hygiene
git fetch --prune
git log --oneline main -5
git rev-list --objects --all | grep -c "\.csv$"  # should be 0

# DVC (data versioning — Module 04)
dvc status            # "Data and pipelines are up to date."
dvc pull              # fetches data/raw/*.csv from the DagsHub remote
md5sum data/raw/*.csv # must match the md5 in the *.csv.dvc pointer
```

---

## 14. Known issues / blockers

| Issue | Module | Status |
|-------|--------|--------|
| Instructor not added as collaborator | 01 | **SKIPPED** (graded from the repo alone) |
| Saad to run `pre-commit install` in his own clone | 03 | ⬜ pending (per-clone) |
| Saad: retro-approval on PRs #5–#7 + his own `dvc pull` md5 check | 04, 05 | ⬜ pending |
| PRs #5–#7 merged by the author after temporarily relaxing only the *approval* rule (protection restored + verified after each merge) | 03, 04 | ⚠️ documented deviation — see §5 |
| DagsHub token stored in `.dvc/config.local` (git-ignored) — was present in a chat transcript during setup, so should be **rotated** after submission | 04 | ⚠️ rotate token |
| `dvc dagshub-setup` / `dagshub://` do **not** exist in DVC 3.67 — docs corrected to the HTTPS recipe | 04 | ✅ fixed in PR #7 |
| DagsHub repo was storage-only → web UI showed no dataset; fixed by mirroring git code (`dagshub` remote, default branch `dev`). **Must re-push after each GitHub merge** or the DagsHub page goes stale | 04 | ⚠️ sync rule documented |
| CI screenshots (red/green) | 08 | ⬜ pending |
| Network downloads for pre-commit hooks slow/flaky | 03 | ⚠️ known (envs now cached) |

---

*Last updated: 2026-09-29 — this file lives at repo root and is updated with each module close-out.*
