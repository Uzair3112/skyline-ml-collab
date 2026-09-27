# REPORT.md — required contents (outline)

> Copy this structure into `REPORT.md` at the repo root **before** submitting. Grading is done from
> the repository alone — every bullet must be visible or linked there.

---

## 1. Team, roles, dataset, starter code

| | |
|---|---|
| Team | `skyline` |
| Members | **Uzair** — Data owner + Platform (pre-commit, env, releases) |
| | **Saad** — Model owner + Platform (CI, protection, releases) |
| Dataset | [Airline Passenger Satisfaction](https://github.com/vrunm/Airline_Passenger_Satisfaction) — binary classification, ~104 k rows |
| Starter code | same repo — `airline-passenger-satisfaction-eda-notebook.ipynb`, `-ml-notebook.ipynb` (credited with link) |
| DVC remote | DagsHub `dagshub://<owner>/skyline-ml-collab/data` |

## 2. Reproducibility table for the released model

| Field | Value |
|-------|-------|
| Release tag | `model-v1.0` |
| Commit SHA | `<sha of model-v1.0>` |
| `params.yaml` | seed `42`, `test_size 0.2`, `model random_forest`, `n_estimators 100`, `max_depth …` |
| Data `.dvc` hash | `md5 <hash from data/raw/train.csv.dvc>` |
| Lock file | `dvc.lock` (commit SHA / hash) |
| Environment | `uv.lock` (commit SHA) |
| Seed | `42` |
| Metrics | accuracy / precision / recall / F1 / ROC-AUC from `metrics.json` |
| Reproduced by | **Uzair**, fresh clone, on `staging` — identical metrics ✅ |

## 3. Experiment comparison

Paste `dvc exp show` output:

| Experiment | params change | accuracy | F1 | notes |
|------------|---------------|----------|----|-------|
| baseline | max_depth 6 | … | … | Saad |
| exp-1 | max_depth 4 | … | … | Saad |
| exp-2 | max_depth 10 | … | … | Saad — **winner** |
| … | model logreg | … | … | Uzair |
| … | test_size 0.3 | … | … | Uzair |
| … | seed 7 | … | … | Uzair |

**Why the winner:** *(e.g. highest F1 on a fixed seed with no added inference cost; gains were
stable across seeds and the change was a single `params.yaml` line, so it ported cleanly to a
`feat/` branch.)*

## 4. Links (every one of these must exist)

- [ ] Data-update PR: `<url>`
- [ ] Conflict-resolution PR (with the resolution explanation): `<url>`
- [ ] One "changes requested" review: `<url>`
- [ ] Release PR `dev → staging` and `staging → main`: `<url>` / `<url>`
- [ ] Abandoned `exp/` branch + why it was abandoned: `<url>`

## 5. Screenshots

1. Blocked large file / blocked fake secret (Module 03)
2. Failing CI check (Module 08)
3. Passing CI check (Module 08)

## 6. Retrospective

**What broke:** …
**What we standardised:** …
**What we added to `CONTRIBUTING.md` as a result:** …

## 7. Individual contribution (one paragraph per member)

**Uzair:** …
**Saad:** …
