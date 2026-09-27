# Progress board

> Update this file as you go. Status: ⬜ not started · 🟡 in progress · ✅ done · ❌ blocked
> **Also** tick the checkboxes inside each module file — this board is the summary.

**Last updated:** 2026-09-27 · **Current phase:** Module 02 (Phase 2) — 🟡 code done, GitHub protection pending · next: Module 03

## Module status

| # | Module | Status | Branch | PR | Checkpoint evidence |
|---|--------|--------|--------|----|---------------------|
| 01 | Team & repository setup | ✅ | `chore/bootstrap` + `chore/saad-setup` | — | ✅ 2 authors · ✅ write access · ⬜ collaborators 📸 |
| 02 | Scaffold & import | 🟡 | `main` pushed (`5078478`) | docs PR | ✅ import in `git log` · ✅ `staging`+`dev` · ⬜ protection 📸 |
| 03 | Pre-commit & secrets | ⬜ | `feat/pre-commit` | # | 📸 blocked 5 MB file + fake key |
| 04 | DVC data versioning | ⬜ | `data/initial-dataset` | # | CSV absent from git history |
| 05 | Notebooks | ⬜ | `feat/eda-notebook` | # | no outputs in PR diff |
| 06 | Reproducible pipeline | ⬜ | `feat/dvc-pipeline` | # | fresh-clone `dvc repro` identical metrics |
| 07 | Experiments & PRs | ⬜ | `exp/*` | # | ≥3 exp each, changes-requested, conflict PR |
| 08 | CI | ⬜ | `feat/ci` | # | 📸 red + green checks |
| 09 | Release & report | ⬜ | `staging` | # | `model-v1.0` + independent reproduction |

## Rules scoreboard

| Requirement | Target | Status |
|-------------|--------|--------|
| Uzair authored merged PRs | ≥ 2 | 0 / 2 |
| Uzair reviewed PRs | ≥ 2 | 0 / 2 |
| Saad authored merged PRs | ≥ 2 | 0 / 2 |
| Saad reviewed PRs | ≥ 2 | 0 / 2 |
| "Changes requested" reviews | ≥ 1 | 0 / 1 |
| Experiments per member | ≥ 3 | Uzair 0/3 · Saad 0/3 |
| Protected branches | `main`, `staging`, `dev` | 0 / 3 |
| Required CI checks on | all 3 branches | 0 / 3 |
| Release tag | `model-v1.0` on `main` | ⬜ |
| Independent reproduction | matches exactly | ⬜ |
| `REPORT.md` | complete | ⬜ |
| Bonus | CML comment **or** `model-v1.0.1` | ⬜ |

## Open decisions / blockers

| Item | Owner | Status |
|------|-------|--------|
| Instructor approval of the Airline dataset (not on the PDF's list) | Uzair | ✅ (task 1 done) |
| Repo created on GitHub, Saad + instructor added | Uzair | ✅ (task 2 done) |
| Local folder renamed → `skyline-ml-collab`, venv rebuilt, `pyproject` renamed | Uzair | ✅ |
| Local branch `master` → `main`, `origin` set, identity = Uzair Tariq | Uzair | ✅ |
| `README.md` with team/roles committed | Uzair | ✅ |
| `chore/bootstrap` pushed (Phase 1 checkpoint) | Uzair | ✅ |
| **Saad: clone + `git config user.name/user.email` + push a branch** | Saad | ✅ |
| **📸 Screenshot: Settings → Collaborators** (Saad = Write, instructor = Read) | Uzair | ⬜ **only Module 01 item left** |
| DagsHub account created + `dvc dagshub-setup` run | Uzair | ⬜ (Module 04) |

### ⚠️ Open in Module 02 (all GitHub-UI, owner Uzair)

1. **Branch protection** on `main`, `staging`, `dev`: PR required, ≥1 approval, no force-push.
   Then 📸 screenshot for `REPORT.md`.
2. **Default branch** `chore/bootstrap` → `main`, then delete **`chore/bootstrap`** and
   **`chore/saad-setup`**.
3. **Collaborators screenshot** (carried over from Module 01).
4. Saad re-runs his env check from `main`: `uv sync` then `python -m ml_skyline.prepare && …`.
5. Module 02 documentation close-out rides on branch **`docs/module-02-closeout`** → PR → `dev`
   (first real PR; Saad reviews). *No direct pushes to `dev` — the rule applies from now on.*

### ⚠️ Data note found in Phase 2 — matters for Modules 05/06/07

The published `train.csv` is **tab-corrupted** (headers `Customer\tType`, labels
`satisfied\t\t\t`). Repaired in code by `ml_skyline.prepare.normalise_frame`, not by rewriting the
raw file — the raw bytes stay identical to the source repo. A good candidate for the Module 07
`data/<change>` PR: fix the source file itself and show `git checkout` + `dvc checkout` moving
between the broken and fixed versions.

The starter also had a **leakage bug** (`remainder='drop'` discarded every numeric column, and
`y_test`/`X_test` were taken from the training frame), which is why it reported 78 % while the
refactor scores 93 %.

## Log

| Date | What happened |
|------|---------------|
| 2026-09-27 | Module plans written (`docs/module-01…09.md`) |
| 2026-09-27 | **Task 1–2 (Uzair):** team `skyline`, repo `Uzair3112/skyline-ml-collab` created, collaborators added |
| 2026-09-27 | **Task 3:** folder `ml-git-collaboration` → `skyline-ml-collab`; `uv sync --reinstall` (stale shebangs fixed); `pyproject` name → `skyline-ml-collab`; broken `[project.scripts]` removed; package → `src/ml_skyline` |
| 2026-09-27 | **Task 4–5:** `git branch -m main`; `origin` = `git@github.com:Uzair3112/skyline-ml-collab.git` (+ repo-local rewrite to the `github-uzair3112` SSH alias, because plain `github.com` authenticates as Uzair599); local identity `Uzair Tariq <uzairtariq.pakistani@gmail.com>` |
| 2026-09-27 | **Task 6–7:** `README.md` with team/roles; commit `6e16d66` pushed to **`chore/bootstrap`** as Uzair3112 ✅ |
| 2026-09-27 | **Task 4/7 (Saad):** clone verified; local identity `Muhammad Saad Sabir <saadsbr789@gmail.com>`; SSH as `msaadsbr` with write access; branch **`chore/saad-setup`** pushed ✅ — Phase-1 two-author checkpoint met |
| 2026-09-27 | **Module 01 close-out (Uzair):** `main` fast-forwarded onto Saad's branch → `214269f`; both authors confirmed; `main` deliberately not pushed (Phase 2 owns that) |
| 2026-09-27 | **M02 tasks 1–2:** skeleton created; `.gitignore` rewritten — *correction*: ignore by extension, **not** `data/` wholesale, or DVC pointers would be uncommittable |
| 2026-09-27 | **M02 task 3:** starter refactored into `src/ml_skyline/{common,prepare,pipeline,train,evaluate}.py` + 17 tests; fixed the starter's tab-corrupted CSV and its `remainder='drop'`/train-as-test leakage; **93.0 % accuracy** vs 78 % |
| 2026-09-27 | **M02 tasks 4–6:** `joblib`/`pyyaml` made explicit + ruff/pytest config; 5 small commits; **`main` pushed once** (`5078478`); `staging` and `dev` created and pushed at the same SHA |
| 2026-09-27 | **M02 task 8:** `CONTRIBUTING.md` — branch rules, Conventional Commits, **squash into `dev`** decision, DVC and review rules |
