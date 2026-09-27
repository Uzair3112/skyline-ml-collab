# Progress board

> Update this file as you go. Status: ⬜ not started · 🟡 in progress · ✅ done · ❌ blocked
> **Also** tick the checkboxes inside each module file — this board is the summary.

**Last updated:** 2026-09-27 · **Current phase:** Module 01 (Phase 1) — 🟡 waiting on Saad

## Module status

| # | Module | Status | Branch | PR | Checkpoint evidence |
|---|--------|--------|--------|----|---------------------|
| 01 | Team & repository setup | 🟡 | `chore/bootstrap` pushed | — | ✅ Uzair pushed · ⬜ Saad clone + push |
| 02 | Scaffold & import | ⬜ | `main` | — | 3 protected branches, import in `git log` |
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
| **Saad: clone + `git config user.name/user.email` + push a branch** | Saad | ⬜ |
| **Screenshot: collaborators list** | Uzair | ⬜ |
| DagsHub account created + `dvc dagshub-setup` run | Uzair | ⬜ (Module 04) |

### ⚠️ Carry into Module 02

1. `chore/bootstrap` is currently GitHub's **default branch** (it was pushed first) → push `main`,
   switch the default branch to `main`, then delete `chore/bootstrap`.
2. Still untracked and belonging to the Phase 2 initial import:
   `.gitignore`, `.python-version`, `pyproject.toml`, `uv.lock`, `src/ml_skyline/`.

## Log

| Date | What happened |
|------|---------------|
| 2026-09-27 | Module plans written (`docs/module-01…09.md`) |
| 2026-09-27 | **Task 1–2 (Uzair):** team `skyline`, repo `Uzair3112/skyline-ml-collab` created, collaborators added |
| 2026-09-27 | **Task 3:** folder `ml-git-collaboration` → `skyline-ml-collab`; `uv sync --reinstall` (stale shebangs fixed); `pyproject` name → `skyline-ml-collab`; broken `[project.scripts]` removed; package → `src/ml_skyline` |
| 2026-09-27 | **Task 4–5:** `git branch -m main`; `origin` = `git@github.com:Uzair3112/skyline-ml-collab.git` (+ repo-local rewrite to the `github-uzair3112` SSH alias, because plain `github.com` authenticates as Uzair599); local identity `Uzair Tariq <uzairtariq.pakistani@gmail.com>` |
| 2026-09-27 | **Task 6–7:** `README.md` with team/roles; commit `6e16d66` pushed to **`chore/bootstrap`** as Uzair3112 ✅ |
