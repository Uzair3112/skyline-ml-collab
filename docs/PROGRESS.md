# Progress board

> Update this file as you go. Status: ⬜ not started · 🟡 in progress · ✅ done · ❌ blocked
> **Also** tick the checkboxes inside each module file — this board is the summary.

**Last updated:** — · **Current phase:** —

## Module status

| # | Module | Status | Branch | PR | Checkpoint evidence |
|---|--------|--------|--------|----|---------------------|
| 01 | Team & repository setup | ⬜ | `main` | — | collaborators, both members pushed a branch |
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
| Instructor approval of the Airline dataset (not on the PDF's list) | Uzair | ⬜ |
| DagsHub account created + `dvc dagshub-setup` run | Uzair | ⬜ |
| Local folder renamed to `skyline-ml-collab` | Uzair | ⬜ |
| Repo created on GitHub, Saad + instructor added | Uzair | ⬜ |

## Log

| Date | What happened |
|------|---------------|
| — | Module plans written (`docs/module-01…09.md`) |
