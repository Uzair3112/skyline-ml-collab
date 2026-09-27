# Module 09 · Release: dev → staging → main

**Phase 9** · Owner: **both** · Rubric: *Branching & protection (15)* + *Release & report (10)*
**Checkpoint:** tag **`model-v1.0`** exists on `main` **and** the independent reproduction succeeded.

## Objective

Promote `dev → staging → main`, have the member who did **not** train the model reproduce the
metrics from a fresh clone, tag `model-v1.0`, and write the report.

## Tasks

### 1. Release PR: `dev` → `staging`

- [ ] Title exactly: **`release: v1.0`**
- [ ] Body summarises the included PRs and the final metrics
- [ ] Author: **Saad** · Reviewer: **Uzair**
- [ ] One approving review, all CI checks green

### 2. Reproducibility test (Uzair — he did not train the final model)

```bash
git clone https://github.com/<owner>/skyline-ml-collab.git /tmp/repro-v1
cd /tmp/repro-v1
git checkout staging
uv sync
dvc pull
dvc repro
cat metrics.json
```

- [ ] Metrics **match the reported ones exactly** (accuracy / F1 / ROC-AUC to full precision)
- [ ] 📸 paste the resulting `metrics.json` **as a comment on the release PR**
- [ ] If they differ → something is unseeded, unpinned or unpushed; fix before merging

### 3. Merge `staging` → `main` and tag

- [ ] PR from `staging` into `main` (author **Uzair**, reviewer **Saad**), 1 approval, CI green

```bash
git checkout main && git pull
git tag -a model-v1.0 -m "First production model"
git push origin model-v1.0
```

- [ ] `model-v1.0` visible under GitHub → Tags
- [ ] `git ls-remote --tags origin` shows it

### 4. Optional hotfix (**+5 bonus**, alternative to CML)

```bash
git switch -c fix/metrics-rounding main
# small real bug: e.g. metrics rounded before reporting
git commit -am "fix: stop rounding metrics before writing metrics.json"
git push -u origin fix/metrics-rounding
# PR → main, 1 approval, CI green, then:
git tag -a model-v1.0.1 -m "Hotfix: metrics rounding"
git push origin model-v1.0.1
# then merge main back into dev so the fix isn't lost
git switch dev && git pull && git merge main && git push
```

- [ ] *(optional)* `model-v1.0.1` on `main` **and** `main` merged back into `dev`

### 5. Retrospective (team meeting, feed REPORT.md)

Answer and write down:

- [ ] What broke? (e.g. *forgot `dvc push` once → Saad got broken pointers*;
      *first CI was red because ruff format was never run locally*)
- [ ] What would we standardise?
- [ ] What did we **add to `CONTRIBUTING.md`** because of it?
      (e.g. *"run `uv run pre-commit run --all-files` before every push"*,
      *"always `dvc push` then `git push`"*)

### 6. Close out

- [ ] All short-lived branches deleted (`feat/*`, `data/*`, `fix/*`)
- [ ] `exp/` branch deliberately left unmerged, referenced in REPORT.md
- [ ] `REPORT.md` complete → see [REPORT-outline.md](REPORT-outline.md)
- [ ] Repo link submitted

## Checkpoint (evidence for REPORT.md)

- [ ] `model-v1.0` on `main`
- [ ] Independent reproduction comment on the release PR with identical `metrics.json`
- [ ] Retrospective section in `REPORT.md`

## Pitfalls

- Tagging before the reproduction → the tag points at unverified code.
- Forgetting to merge `main` back into `dev` after a hotfix → next release re-introduces the bug.
- Release PR that squashes away history needed for the reproducibility table (commit SHA).
- `dvc pull` skipped during reproduction → you silently evaluate stale data.
