# Module 09 · Release: dev → staging → main

**Phase 9** · Owner: **both** · Rubric: *Branching & protection (15)* + *Release & report (10)*
**Checkpoint:** tag **`model-v1.0`** exists on `main` **and** the independent reproduction succeeded.

## Objective

Promote `dev → staging → main`, have the member who did **not** train the model reproduce the
metrics from a fresh clone, tag `model-v1.0`, and write the report.

## Tasks

### 1. Release PR: `dev` → `staging`

- [x] Title exactly: **`release: v1.0`**
- [x] Body summarises the included PRs and the final metrics
- [x] Author: **Saad** · Reviewer: **Uzair** → **deviation:** Saad unavailable since M05, Uzair
      authored it (same documented deviation as M05–M08); retro review requested
- [x] One approving review, all CI checks green — 5/5 (`lint`, `tests`, `data-checks`,
      `smoke-train`, `cml-comment`) on the merged release PR **#27**

> **How it actually went (evidence worth keeping):**
> **#24** first promotion, squash → rebase-merged (GitHub rewrote the SHAs) → reproduction **failed**
> (`roc_auc` moved between runs) → **#25** fix (`train.n_jobs: 1`) landed on `dev` → **#26** direct
> `dev`→`staging` PR went `mergeable=dirty` (staging's rewritten SHAs vs `dev` = add/add conflicts on
> `dvc.lock`, `metrics.json`, `params.yaml`; **no merge ref ⇒ no CI run**) → closed → **#27**
> `release/v1.0`, a branch cut **from `staging`** with `dev` merged in and conflicts resolved to
> `dev`: head contains its base ⇒ clean diff, CI runs, merge-commit (CONTRIBUTING §3 fallback).

### 2. Reproducibility test (Uzair — he did not train the final model)

```bash
git clone https://github.com/<owner>/skyline-ml-collab.git /tmp/repro-v1
cd /tmp/repro-v1
git checkout staging
uv sync --frozen
dvc pull
dvc repro
cat metrics.json
```

- [x] Metrics **match the reported ones exactly** (accuracy / F1 / ROC-AUC to full precision)
      — all value metrics byte-identical, `roc_auc 0.9941573399364485` stable across 4 forced runs;
      only `commit_sha` differs (by design)
- [x] 📸 paste the resulting `metrics.json` **as a comment on the release PR**
      — comment on **#27** + full log in [evidence/module-09-reproduction.txt](evidence/module-09-reproduction.txt)
- [x] If they differ → something is unseeded, unpinned or unpushed; fix before merging
      — **it differed twice, and both catches are real:** (1) `roc_auc` non-determinism from
      `n_jobs=-1` thread-completion order → #25; (2) #25's retrain was never `dvc push`ed, so a
      fresh clone failed `dvc pull` on `models/model.pkl` → pushed, release re-verified

### 3. Merge `staging` → `main` and tag

- [x] PR from `staging` into `main` (author **Uzair**, reviewer **Saad**), 1 approval, CI green
      — **#28** (release branch cut from `main`, same contains-its-base pattern), 5/5 green, merged
      with a merge-commit (rebase would replay the duplicated patches onto themselves)

```bash
git checkout main && git pull
git tag -a model-v1.0 -m "First production model"
git push origin model-v1.0
```

- [x] `model-v1.0` visible under GitHub → Tags — `7c2dd1e` → `bb6517a` (`main`)
- [x] `git ls-remote --tags origin` shows it — `refs/tags/model-v1.0`

### 4. Optional hotfix (**+5 bonus**, alternative to CML)

```bash
git switch -c fix/report-clobber main
# real bug: ml_skyline.smoke --report wrote blindly; on a case-insensitive
# filesystem --report report.md resolved to REPORT.md and replaced it entirely
git commit -m "fix: refuse to clobber non-report files with smoke --report"
git push -u origin fix/report-clobber
# PR #29 → main, 5/5 CI green, rebase-merged (e7ccda0), then:
git tag -a model-v1.0.1 -m "Hotfix: smoke --report refuses to clobber REPORT.md"
git push origin model-v1.0.1
# then merge main back into dev so the fix isn't lost
# → PR #30 (fast-forward, 7232a66 → e7ccda0), dev == main again
```

- [x] *(optional)* `model-v1.0.1` on `main` **and** `main` merged back into `dev`
      — `713d0ed` → `e7ccda0`; PR **#30** fast-forwarded `dev` (`ea59e2a`), `git diff dev main` → empty

### 5. Retrospective (team meeting, feed REPORT.md)

Answer and write down:

- [x] What broke? (e.g. *forgot `dvc push` once → Saad got broken pointers*;
      *first CI was red because ruff format was never run locally*)
      — **all four broke, see REPORT.md §5:** red CI (M08), `roc_auc` non-determinism (M09),
      **`dvc push` skipped after the M09 retrain** (caught by this very reproduction),
      and the rebase-merge SHA divergence that made #26 un-mergeable and CI-less
- [x] What would we standardise? — REPORT.md §5 "What we would standardise"
- [x] What did we **add to `CONTRIBUTING.md`** because of it?
      (e.g. *"run `uv run pre-commit run --all-files` before every push"*,
      *"always `dvc push` then `git push`"*)
      — present since M03 (`pre-commit run --all-files`), M04 (`dvc push` **before** `git push`),
      M08 (CI commands identical to the local pre-flight); M09 additions documented in REPORT.md §5

### 6. Close out

- [x] All short-lived branches deleted (`feat/*`, `data/*`, `fix/*`)
      — `fix/report-clobber`, `release/v1.0`, `release/v1.0-main`, `sync/main-hotfix-into-dev`,
      `feat/*`, `data/*` all deleted locally and on `origin`
- [x] `exp/` branch deliberately left unmerged, referenced in REPORT.md
      — `exp/uzair-model-sweep`, `exp/saad-depth-sweep` kept (M07 abandoned-experiment evidence)
- [x] `REPORT.md` complete → see [REPORT-outline.md](REPORT-outline.md)
- [ ] Repo link submitted *(submission-portal step for the team)*

## Checkpoint (evidence for REPORT.md)

- [x] `model-v1.0` on `main` (+ `model-v1.0.1` hotfix tag)
- [x] Independent reproduction comment on the release PR with identical `metrics.json` (PR #27)
- [x] Retrospective section in `REPORT.md` (§5, incl. reproducibility table)

## Pitfalls

- Tagging before the reproduction → the tag points at unverified code.
- Forgetting to merge `main` back into `dev` after a hotfix → next release re-introduces the bug.
- Release PR that squashes away history needed for the reproducibility table (commit SHA).
- `dvc pull` skipped during reproduction → you silently evaluate stale data.
