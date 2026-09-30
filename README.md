# skyline-ml-collab

MLOps **Assignment 01 — Git-Based Collaboration for an ML Project**.
Team `skyline` takes the [Airline Passenger Satisfaction](https://github.com/vrunm/Airline_Passenger_Satisfaction)
dataset and starter code and runs it as a real team project: branches, reviewed PRs, DVC-versioned
data, reproducible experiments, CI and a tagged release.

> Goal: **every result, reproducible by anyone on the team.**

## Team and roles

| Member | Role | Owns |
|--------|------|------|
| **Uzair Tariq** | Data owner · Platform owner (A) | DVC, data checks, dataset updates · pre-commit, environment, releases |
| **Saad** | Model owner · Platform owner (B) | training pipeline, configs, experiments · CI, branch protection, releases |

Everyone codes **and** reviews. Each member must author ≥ 2 merged PRs and review ≥ 2.

## Dataset and source

| | |
|---|---|
| Task | Binary classification — passenger `satisfaction` (`satisfied` / `neutral or dissatisfied`) |
| Size | ~104 k rows, well under 50 MB |
| Dataset + starter code | <https://github.com/vrunm/Airline_Passenger_Satisfaction> (credited as the starter source) |

## Branch model

```
feat/<name>   ─┐
data/<name>   ─┼─► dev ─► staging ─► main   (tagged model-v1.0)
exp/<member>-<idea>  ──► never merged (cherry-pick the winner into a feat/)
fix/<name>    ──► main (model-v1.0.1) then merge main back into dev
```

Nobody pushes directly to `dev`, `staging` or `main` — pull requests only, one approving review,
CI green. Full rules land in `CONTRIBUTING.md` (Phase 2); the plan lives in [`docs/`](docs/).

## Getting started

```bash
git clone git@github.com:Uzair3112/skyline-ml-collab.git
cd skyline-ml-collab
uv sync                 # reproducible environment from uv.lock
pre-commit install      # ruff, nbstripout, large-file and secret guards
dvc pull                # dataset from the DVC remote
```

## Release status

| | |
|---|---|
| Modules | **01–09 complete** — full walkthrough in [`REPORT.md`](REPORT.md) |
| Release | tag **`model-v1.0`** → `bb6517a` on `main` · hotfix **`model-v1.0.1`** → `e7ccda0` |
| Branches | `dev` → `staging` → `main`, all three protected: 1 approving review + `lint`, `tests`, `data-checks`, `smoke-train` required **and green** |
| CI | every PR runs lint / tests / data-checks / smoke-train (~1 min) and posts a CML metrics comment |
| Data | DVC remote on DagsHub (`storage`) — pointers only in git, no CSVs in history |
| Experiments | `exp/uzair-model-sweep`, `exp/saad-depth-sweep` deliberately **unmerged** (abandoned-branch evidence) |

## Reproduce the release

```bash
git clone https://github.com/Uzair3112/skyline-ml-collab.git
cd skyline-ml-collab
git checkout model-v1.0          # or branch staging / main — all share one tree
uv sync --frozen                 # pinned environment from uv.lock
dvc pull                         # data + trained model from the DagsHub remote
dvc repro                        # no-ops: outputs already match dvc.lock
cat metrics.json
```

Expected (seed 42, `max_depth 24`, single-threaded scoring):

| metric | value |
|--------|-------|
| accuracy | `0.9624657138732496` |
| precision | `0.9683407356793076` |
| recall | `0.9442531926707385` |
| f1 | `0.9561452828067019` |
| roc_auc | `0.9941573399364485` |

Only `commit_sha` differs if you run it from a later checkout — it records the commit the run
happened on. Full transcript: [`docs/evidence/module-09-reproduction.txt`](docs/evidence/module-09-reproduction.txt).

## Documentation

| Doc | Purpose |
|-----|---------|
| [`docs/README.md`](docs/README.md) | Module index and grading map |
| [`docs/00-overview.md`](docs/00-overview.md) | Decisions, roles, branch model, PR plan |
| [`docs/module-01…09.md`](docs/) | Step-by-step plan per phase, with checkpoints |
| [`docs/PROGRESS.md`](docs/PROGRESS.md) | Live progress board |
| `CONTRIBUTING.md` | Branch/commit/review rules *(added in Phase 2)* |
| `REPORT.md` | Final submission report *(added in Phase 9)* |
