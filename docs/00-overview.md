# 00 · Overview & team decisions

## Goal

> Every result, reproducible by anyone on the team.

Take the Airline Passenger Satisfaction dataset + starter code, put it under **Git** and **DVC**, and
run it like a real team project: branches, experiments, reviewed pull requests, versioned data, CI
and a tagged release.

## Team

| Member | Roles |
|--------|-------|
| **Uzair** | **Data owner** (DVC, data checks, dataset updates) + **Platform owner A** (pre-commit, environment, releases) |
| **Saad** | **Model owner** (training pipeline, configs, experiments) + **Platform owner B** (CI, branch protection, releases) |

In a team of 2 the Platform role is split. Everyone still codes **and** reviews.

## Decisions (locked)

| Decision | Value | Why |
|----------|-------|-----|
| Team name | `skyline` | — |
| GitHub repo | **`skyline-ml-collab`** | assignment requires `<team>-ml-collab` |
| Local folder | `skyline-ml-collab` (rename from `ml-git-collaboration`) | consistency; see M01 |
| Dataset | [Airline Passenger Satisfaction](https://github.com/vrunm/Airline_Passenger_Satisfaction) | binary classification, ~104k rows, well under 50 MB |
| Starter code | same repo — `airline-passenger-satisfaction-eda-notebook.ipynb`, `-ml-notebook.ipynb`, `train.csv`, `test.csv` | credit in REPORT.md |
| DVC remote | **DagsHub** (`dagshub://<owner>/skyline-ml-collab/data`) | free shared remote, no secrets in git, gives `dvc exp`-style hosting |
| Environment | `uv` + `uv.lock` (already generated) | required by Phase 2 / Phase 9 (`uv sync`) |
| Python | 3.13 | `.python-version` |
| PR merge strategy | **squash** into `dev` (rebase for `staging`/`main`) | decide once → write in `CONTRIBUTING.md` |
| Dataset check | **ask instructor** — the PDF says pick from its list, airline satisfaction is *not* on it but meets the "<50 MB tabular" rule | do this in Phase 1 |

### ⚠️ Open item for Phase 1

The PDF says *"Choose a dataset and starter code from the list at the end of this document"*. Our
dataset is not on that list (Titanic / Wine / Adult / Heart / Telco / California). It satisfies the
stated constraint (*small tabular, < ~50 MB*). **Tell the instructor our choice and get a yes before
Phase 4**, otherwise we risk marks in "Repo structure" / instructor trust.

## Repo layout we are building

```
skyline-ml-collab/
├── configs/                 # params.yaml lives here (or root)
├── data/                    # ignored by Git, tracked by DVC
│   └── raw/train.csv, test.csv
├── models/                  # ignored by Git, tracked by DVC
├── notebooks/
│   ├── 01-eda.ipynb
│   └── 01-eda.py            # jupytext pair
├── src/
│   ├── prepare.py           # stage 1
│   ├── train.py             # stage 2
│   └── evaluate.py          # stage 3  → metrics.json
├── tests/
├── docs/                    # this folder (module plans)
├── .github/
│   ├── workflows/ci.yml
│   └── pull_request_template.md
├── .gitignore
├── .pre-commit-config.yaml
├── dvc.yaml / dvc.lock
├── params.yaml
├── metrics.json
├── CONTRIBUTING.md
├── README.md
├── REPORT.md
├── pyproject.toml + uv.lock
```

## Branching model (memorise this)

```
feat/<name>  ─┐
data/<name>  ─┼─► dev ─► staging ─► main   (tagged: model-v1.0)
              │
exp/<member>-<idea>  ──► NEVER merged (cherry-pick winner into a feat/)
fix/<name>   ──► main (patch tag model-v1.0.1) then merge main back into dev
```

| Branch | Created from | Merges into | Protection |
|--------|--------------|-------------|------------|
| `main` | — | — | PR only, 1 approval, all CI green, no force-push |
| `staging` | `main` | `main` | PR only, 1 approval, all CI green |
| `dev` | `staging` | `staging` | PR only, 1 approval, CI green |
| `feat/<name>` | `dev` | `dev` | deleted after merge |
| `data/<name>` | `dev` | `dev` | deleted after merge; `dvc push` first |
| `exp/<member>-<idea>` | `dev` | *nothing* | keep short-lived, rebase on dev often |
| `fix/<name>` | `main` | `main` → back into `dev` | deleted after merge |

**Work moves one direction only:** `dev → staging → main`.

## PR budget (how we hit the ≥2 authored / ≥2 reviewed rule)

| # | PR | Author | Reviewer | Module |
|---|----|--------|----------|--------|
| 1 | `feat/pre-commit` → dev | Saad | Uzair | M03 |
| 2 | `data/initial-dataset` → dev | Uzair | Saad | M04 |
| 3 | `feat/eda-notebook` → dev | Saad | Uzair | M05 |
| 4 | `feat/dvc-pipeline` → dev | Saad | Uzair (**request changes once**) | M06 |
| 5 | `exp/saad-max-depth` promote → dev | Saad | Uzair | M07 |
| 6 | `feat/ci` → dev | Uzair | Saad | M08 |
| 7 | `data/remove-duplicates` → dev | Uzair | Saad | M07 |
| 8 | params.yaml **conflict** PR → dev | Uzair | Saad | M07 |
| 9 | `release: v1.0` dev → staging | Saad | Uzair | M09 |
| 10 | staging → main | Uzair | Saad | M09 |

→ Uzair authors 4, reviews 5 · Saad authors 6, reviews 5. Both clear the bar with margin.

## Rubric → module traceability

- **10** Repo hygiene → M01 (layout, .gitignore, no data/secrets in history), M02, M03
- **15** Branching & protection → M01 (3 protected branches), M09 (correct flow)
- **20** PRs & review → every module's PR + M07 checklist
- **15** DVC → M04 (data), M07 (data-update PR, `git checkout`/`dvc checkout`)
- **5** Notebooks → M05
- **15** Reproducible experiments → M06 (pipeline) + M07 (≥3 experiments each)
- **10** CI → M08
- **10** Release & report → M09 + `REPORT.md`
- **+5** Bonus → CML metrics comment (M08) **or** hotfix `model-v1.0.1` (M09)

## Marks lost if we do these (from the PDF)

1. Committing dataset/model to Git → fix with `git filter-repo`, not a new commit.
2. `git push` without `dvc push` → broken pointers for teammates.
3. Experiments on uncommitted code → logged SHA ≠ code.
4. Long-lived `exp/` branches drifting from dev → rebase often.
5. Notebooks that only work in one cell order on one laptop.
6. Approving a PR without running it → check out the branch at least once per pipeline PR.
