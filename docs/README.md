# Assignment 01 · Git-Based Collaboration for an ML Project — Module Index

> **Team:** `skyline` (Uzair, Saad) · **Repo:** `skyline-ml-collab`
> **Dataset:** [Airline Passenger Satisfaction](https://github.com/vrunm/Airline_Passenger_Satisfaction)
> **Source of this plan:** `Assignment-01.pdf` (9 phases, 100 pts + 5 bonus)

This folder is the team's implementation and tracking plan. Complete the modules **in order** —
each one ends with a checkpoint that must be visible in the repository.

## Modules

| # | Module | Phase | Owner | Branch | Status |
|---|--------|-------|-------|--------|--------|
| 00 | [Overview & decisions](00-overview.md) | — | both | — | ✅ done |
| 01 | [Team & repository setup](module-01-team-and-repo-setup.md) | Phase 1 | Uzair | `main` | ✅ (collaborators 📸 pending) |
| 02 | [Scaffold & import starter code](module-02-scaffold-and-import.md) | Phase 2 | both | `main` pushed · `docs/module-02-closeout` | 🟡 code done, protection ⬜ |
| 03 | [Guard rails: pre-commit & secrets](module-03-guard-rails-pre-commit.md) | Phase 3 | Saad | `feat/pre-commit` | ⬜ |
| 04 | [Version the data with DVC](module-04-dvc-data-versioning.md) | Phase 4 | Uzair | `data/initial-dataset` | ⬜ |
| 05 | [Notebooks done right](module-05-notebooks.md) | Phase 5 | Saad | `feat/eda-notebook` | ⬜ |
| 06 | [Reproducible DVC pipeline](module-06-reproducible-pipeline.md) | Phase 6 | Saad | `feat/dvc-pipeline` | ⬜ |
| 07 | [Experiments & pull requests](module-07-experiments-and-prs.md) | Phase 7 | both | `exp/*` | ⬜ |
| 08 | [CI on every pull request](module-08-ci.md) | Phase 8 | Uzair | `feat/ci` | ⬜ |
| 09 | [Release: dev → staging → main](module-09-release.md) | Phase 9 | both | `staging` | ⬜ |
| — | [REPORT.md outline](REPORT-outline.md) | submission | both | — | ⬜ |
| — | [Progress board](PROGRESS.md) | all | both | — | ⬜ |

## What we submit

1. Repository link (`skyline-ml-collab`)
2. `REPORT.md` in the repo root
3. Release tag **`model-v1.0`** on `main` that a stranger can reproduce

## Non-negotiable team rules

- Nobody pushes directly to `dev`, `staging` or `main` — **PRs only** (after Phase 2's initial import).
- Every member authors **≥ 2 merged PRs** and reviews **≥ 2 PRs**, with **≥ 1 "changes requested"**.
- Never commit on each other's behalf; contribution is read from Git history.
- `dvc push` **before** `git push` whenever data or models changed.
- Conventional Commits: `feat:`, `fix:`, `data:`, `exp:`, `chore:`, `ci:`, `docs:`, `test:`.

## Grading map (100 + 5)

| Area | Pts | Delivered by |
|------|-----|--------------|
| Repo structure & hygiene | 10 | M01, M02, M03 |
| Branching & protection | 15 | M01, M09 |
| Pull requests & review | 20 | M03–M09 (every PR) |
| Data & model versioning | 15 | M04, M07 |
| Notebooks | 5 | M05 |
| Reproducible experiments | 15 | M06, M07 |
| CI | 10 | M08 |
| Release & report | 10 | M09 |
| **Bonus** | +5 | CML comment **or** hotfix `model-v1.0.1` |
