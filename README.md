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

## Documentation

| Doc | Purpose |
|-----|---------|
| [`docs/README.md`](docs/README.md) | Module index and grading map |
| [`docs/00-overview.md`](docs/00-overview.md) | Decisions, roles, branch model, PR plan |
| [`docs/module-01…09.md`](docs/) | Step-by-step plan per phase, with checkpoints |
| [`docs/PROGRESS.md`](docs/PROGRESS.md) | Live progress board |
| `CONTRIBUTING.md` | Branch/commit/review rules *(added in Phase 2)* |
| `REPORT.md` | Final submission report *(added in Phase 9)* |
