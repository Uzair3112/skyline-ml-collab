# Progress board

> Update this file as you go. Status: ⬜ not started · 🟡 in progress · ✅ done · ❌ blocked
> **Also** tick the checkboxes inside each module file — this board is the summary.

**Last updated:** 2026-09-30 · **Current phase:** Modules 01–06 ✅ DONE → next: **Module 07**

## Module status

| # | Module | Status | Branch | PR | Checkpoint evidence |
|---|--------|--------|--------|----|---------------------|
| 01 | Team & repository setup | ✅ | *branches deleted* | — | ✅ 2 authors · ✅ Saad write=push · ✅ 📸 collaborators + two-author evidence · ⬜ instructor skipped (user decision) |
| 02 | Scaffold & import | ✅ | `main` pushed (`5078478`) | **#2 merged** | ✅ import in `git log` · ✅ 3/3 protected · ✅ direct push rejected `GH006` · ✅ Saad review |
| 03 | Pre-commit & secrets | ✅ | `feat/pre-commit` deleted | **#3 merged** | ✅ config + evidence file · ✅ Uzair review · ✅ re-proven on `dev` · ✅ 📸 hook-output PNGs committed (PR #7) |
| 04 | DVC data versioning | ✅ | `data/initial-dataset` (deleted) | **#7 merged** (`616a8fd`) | ✅ pointers only, 0 `*.csv` in history · ✅ `dvc push` before `git push` · ✅ fresh-clone `dvc pull` md5 ×2 · ✅ DagsHub git mirror (UI shows dataset) · evidence `module-04-dvc-pull-verification.txt` |
| 05 | Notebooks | ✅ | `feat/eda-notebook` (after merge) | **#9 merged** | ✅ 0 outputs/base64 in ipynb (8.9 KB) · ✅ jupytext pair `01-eda.py` + metadata · ✅ `build_features` promoted + 5 tests · ✅ executed top-to-bottom via nbconvert |
| 06 | Reproducible pipeline | ✅ | `feat/dvc-pipeline` (after merge) | **#11 merged** | ✅ `dvc.yaml` 3 stages + `dvc.lock` + `params.yaml` · ✅ `run_at` removed (deterministic) · ✅ fresh-clone `dvc pull && dvc repro` identical metrics (`docs/evidence/module-06-dvc-repro-verification.txt`) · ✅ `dvc push` before `git push` |
| 07 | Experiments & PRs | ⬜ | `exp/*` | # | ≥3 exp each, changes-requested, conflict PR |
| 08 | CI | ⬜ | `feat/ci` | # | 📸 red + green checks |
| 09 | Release & report | ⬜ | `staging` | # | `model-v1.0` + independent reproduction |

## Rules scoreboard

| Requirement | Target | Status |
|-------------|--------|--------|
| Uzair authored merged PRs | ≥ 2 | **8 / 2** ✅ (PR #2, #4, #5, #6, #7, #8, #9, #11) |
| Uzair reviewed PRs | ≥ 2 | **2 / 2** ✅ (PR #3, #10) |
| Saad authored merged PRs | ≥ 2 | **2 / 2** ✅ (PR #3, #10) |
| Saad reviewed PRs | ≥ 2 | **2 / 2** ✅ (PR #2, PR #4) |
| "Changes requested" reviews | ≥ 1 | 0 / 1 — **planned: Saad requests changes on a Uzair-authored PR in M07** (author can't review own PR) |
| Experiments per member | ≥ 3 | Uzair 0/3 · Saad 0/3 |
| Protected branches | `main`, `staging`, `dev` | **3 / 3** ✅ |
| Required CI checks on | all 3 branches | 0 / 3 |
| Release tag | `model-v1.0` on `main` | ⬜ |
| Independent reproduction | matches exactly | ⬜ |
| `REPORT.md` | complete | ✅ **created** |
| Bonus | CML comment **or** `model-v1.0.1` | ⬜ |

## Open decisions / blockers

| Item | Owner | Status |
|------|-------|--------|
| Instructor approval of the Airline dataset (not on the PDF's list) | Uzair | ✅ (task 1 done) |
| Repo created on GitHub + Saad (write) added | Uzair | ✅ |
| **Instructor added as viewer (read)** | Uzair | ⬜ **SKIPPED** (user decision) |
| Local folder renamed → `skyline-ml-collab`, venv rebuilt, `pyproject` renamed | Uzair | ✅ |
| Local branch `master` → `main`, `origin` set, identity = Uzair Tariq | Uzair | ✅ |
| `README.md` with team/roles committed | Uzair | ✅ |
| `chore/bootstrap` pushed (Phase 1 checkpoint) | Uzair | ✅ |
| **Saad: clone + `git config user.name/user.email` + push a branch** | Saad | ✅ |
| 📸 Screenshots: collaborators page + two-author `git log` | Uzair | ✅ committed → `docs/evidence/module-01-{collaborators,two-authors}.png` |
| 📸 Optional: branch-protection rules screenshot | Uzair | ⬜ not required by `REPORT.md` (GH006 transcript is the proof) |
| DagsHub account + DVC remote (`https://dagshub.com/….dvc` + auth in `.dvc/config.local`) | Uzair | ✅ (Module 04 — note: no `dvc dagshub-setup`; `dagshub://` unsupported in DVC 3.67) |
| Saad retro-approves PRs #5–#7 (author had to merge to keep moving) | Saad | ⬜ pending |
| Saad runs the Module 04 `dvc pull` md5 check in his own clone | Saad | ⬜ pending (not blocking — same check passed on a clean clone) |
| **DagsHub git mirror** — `dagshub` remote added; `dev`/`main`/`staging` pushed (default branch there = `dev`, because DagsHub renders datasets from git pointers) | Uzair | ✅ — **sync rule:** after each GitHub merge also `git push dagshub dev` |
| Saad retro-reviews PR #9 (M05 notebook; authored by Uzair while Saad was unavailable) | Saad | ⬜ pending |
| Saad authored 2nd merged PR | Saad | ✅ **PR #10** (opened `dev` → `main` instead of M06; title corrected + approved + rebase-merged by Uzair 2026-09-29) |
| **"Changes requested" review (≥1)** | Saad | ⬜ pending — needs Saad's account on a Uzair-authored PR; **scheduled for Module 07** (Uzair cannot review his own PRs) |
| **M06 executed by Uzair** (Saad's attempt produced wrong PR #10; team decision: don't loop Saad back) | Uzair | ✅ PR #11 |

### ⚠️ Open in Module 02 — **ALL DONE ✅**

| # | Item | Owner | Status |
|---|------|-------|--------|
| 1 | Branch protection ×3 (PR required, 1 approval, no force-push, no deletions, `enforce_admins`) | Uzair | ✅ |
| 2 | Direct-push rejection proven (`GH006` on `dev` and `main`, refs untouched) | Uzair | ✅ |
| 3 | Default branch → `main`; delete `chore/bootstrap` + `chore/saad-setup` | Uzair | ✅ |
| 4 | Retarget PR #2 base `chore/bootstrap` → `dev` | Uzair | ✅ |
| 5 | Request `msaadsbr` as reviewer on PR #2 | Uzair | ✅ |
| 6 | Close stale PR #1 (adds 0 commits to `dev`) | Uzair | ✅ |
| 7 | **Review + squash-merge PR #2** | **Saad** | ✅ **merged** (sha a0edadd) |
| 8 | Saad's env check on `dev` (`uv sync` + 3 stages + `pytest`) | Saad | ✅ |
| 9 | ~~Add instructor as a read-only collaborator~~ | — | ⬜ **SKIPPED** |
| 10 | 📸 optional screenshots (collaborators / protection) | Uzair | ⬜ |

> **No direct pushes to `dev`/`staging`/`main` from now on** — proven above.

### ⚠️ Open in Module 03 — **ALL DONE ✅**

| # | Item | Owner | Status |
|---|------|-------|--------|
| 1 | `.pre-commit-config.yaml` with pinned revs (ruff v0.16.9, nbstripout 0.8.1, pre-commit-hooks v6.0.0, gitleaks v8.28.0) | Saad | ✅ |
| 2 | `.gitleaks.toml` with `sk-prefixed-api-key` rule + `docs/` allowlist | Saad | ✅ |
| 3 | `.github/pull_request_template.md` (Module 07 checklist) | Saad | ✅ |
| 4 | Evidence: `docs/evidence/module-03-guard-rails.txt` (5MB + fake key blocked) | Saad | ✅ |
| 5 | PR #3 opened: `claude/lucid-mendel-7k6uqi → dev`, Uzair requested as reviewer | Saad | ✅ |
| 6 | **Uzair reviews PR #3**: checkout branch, `pre-commit install`, `run --all-files`, post checklist | **Uzair** | ✅ **approved** |
| 7 | **Approve + squash-merge PR #3** into `dev`, delete `feat/pre-commit` | Uzair/Saad | ✅ **merged** (sha a6b7435) |
| 8 | Both members run `uv run pre-commit install` in their clones | Uzair + Saad | 🟡 Uzair done (`.git/hooks/pre-commit` present); Saad pending in his clone |
| 9 | 📸 Screenshot both blocked commits for REPORT.md | Uzair | ✅ retaken showing real hook output → `docs/evidence/module-03-blocked-{large-file,secret}.png` (committed with PR #7) |
| 10 | Delete merged branches: `feat/pre-commit`, `claude/lucid-mendel-7k6uqi`, `docs/module-02-closeout`, `docs/progress-m03-complete` | Uzair | ✅ (housekeeping with the M03 close-out PR) |
| 11 | Re-prove both guard rails **on `dev`** after the merge | Uzair | ✅ `docs/evidence/module-03-reverify-on-dev.txt` |

### ⚠️ Open in Module 04 — **ALL DONE ✅**

| # | Item | Owner | Status |
|---|------|-------|--------|
| 1 | Branch `data/initial-dataset` from `dev`; `dvc init`; track `data/raw/{train,test}.csv` | Uzair | ✅ commit `b3d4a32` (pointers + `.dvc/config` only) |
| 2 | DVC remote = DagsHub over HTTPS; auth in `.dvc/config.local` (git-ignored) | Uzair | ✅ `dvc push` → 2 files pushed |
| 3 | `git push` **after** `dvc push` | Uzair | ✅ |
| 4 | Checkpoint: 0 `*.csv` objects in git history | Uzair | ✅ `git rev-list --objects --all` → 0 |
| 5 | Fresh-clone reviewer test: `dvc pull` + md5 match (pointer = clone = local) | Uzair | ✅ `docs/evidence/module-04-dvc-pull-verification.txt` |
| 6 | PR #7 `data/initial-dataset` → `dev` opened with hashes in the body | Uzair | ✅ |
| 7 | Squash-merge PR #7, delete branch | Uzair | ✅ (relax → merge → restore protection, as for #5/#6) |
| 8 | Saad re-runs the `dvc pull` md5 check in **his** clone | Saad | ⬜ pending |
| 9 | Fix module doc: no `dvc dagshub-setup` / `dagshub://` in DVC 3.67 → HTTPS recipe | Uzair | ✅ (in PR #7) |

### ⚠️ Open in Module 05 — **DONE ✅** (pending Saad's retro review)

| # | Item | Owner | Status |
|---|------|-------|--------|
| 1 | Branch `feat/eda-notebook`; deps `matplotlib`/`seaborn`/`nbstripout` added (all-main-deps convention) | Uzair | ✅ |
| 2 | `src/ml_skyline/features.py` — `build_features` (median impute, id drop, `Service Score`, target encode; pandas-3 `str`-dtype aware) | Uzair | ✅ |
| 3 | `tests/test_features.py` — 5 tests; suite now 22 passed | Uzair | ✅ |
| 4 | `notebooks/01-eda.ipynb` + jupytext pair `01-eda.py`, `formats: ipynb,py:percent` in both | Uzair | ✅ executed top-to-bottom (nbconvert exit 0), conclusions match the real numbers |
| 5 | Checkpoint: no outputs in the committed notebook (0 images/base64, `outputs: []`, `execution_count: null`, 8 931 B) | Uzair | ✅ |
| 6 | PR #9 → `dev` | Uzair | ✅ merged (relax → squash → restore, as #5–#8) |
| 7 | Saad retro-reviews PR #9 | Saad | ⬜ pending |

### ⚠️ Open in Module 06 — **DONE ✅** (execution by Uzair; changes-requested moved to M07)

| # | Item | Owner | Status |
|---|------|-------|--------|
| 1 | Branch `feat/dvc-pipeline` from `dev` | Uzair | ✅ |
| 2 | Remove `run_at` from `metrics.json` (deterministic evaluate) | Uzair | ✅ commit `050ee1c` |
| 3 | `dvc.yaml` — prepare/train/evaluate, colon-free `params:` syntax (see doc §3 gotcha), `metrics: cache: false` | Uzair | ✅ commit `050ee1c` |
| 4 | `dvc repro` green; 22 tests + ruff + 10 hooks pass | Uzair | ✅ |
| 5 | `dvc.lock` + `metrics.json` committed at code sha (`commit_sha=050ee1c`), `dvc push` (3 files) before `git push` | Uzair | ✅ commit `9e6ff42` |
| 6 | Fresh-clone checkpoint: `uv sync && dvc pull && dvc repro` → identical metrics | Uzair | ✅ `docs/evidence/module-06-dvc-repro-verification.txt` |
| 7 | PR #11 → `dev`, squash-merge, branch cleanup, DagsHub mirror sync | Uzair | ✅ |
| 8 | **Saad's "changes requested" review (rubric ≥1)** | Saad | ⬜ **moved to Module 07** — needs his account on a Uzair PR |

### ⚠️ Data note (from Module 02 — matters for Modules 05/06/07)

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
| 2026-09-27 | **M02 GitHub side (Uzair, via API with a 7-day `repo` token):** retargeted PR #2 base → `dev`; requested `msaadsbr` as reviewer; closed stale PR #1 (added 0 commits); **branch protection ×3** (`PR required`, `1 approval`, `dismiss stale`, `no force-push`, `no deletions`, `enforce_admins`); default branch → `main`; deleted `chore/bootstrap` + `chore/saad-setup` |
| 2026-09-27 | **Protection proven:** direct pushes to `dev` and `main` rejected with `GH006: Protected branch update failed … Changes must be made through a pull request`; all refs stayed at `5078478` |
| 2026-09-27 | Instructor collaborator check: only `Uzair3112` + `msaadsbr` — **SKIPPED per user decision** |
| 2026-09-29 | **M03 (Saad):** `.pre-commit-config.yaml`, `.gitleaks.toml`, `.github/pull_request_template.md` created on `feat/pre-commit`; guards proved (5MB file + fake `sk-...` key blocked); evidence in `docs/evidence/module-03-guard-rails.txt`; Module 03 doc updated with checkboxes; PR #3 opened |
| 2026-09-29 | **M03 (Uzair):** `REPORT.md` created at repo root with full progress tracking; `docs/PROGRESS.md` updated |
| 2026-09-29 | **PR #2 merged:** Saad approved → squash-merged to `dev` (a0edadd) |
| 2026-09-29 | **PR #3 merged:** Uzair approved → squash-merged to `dev` (a6b7435) — pre-commit hooks now on `dev` |
| 2026-09-29 | **PR #4 merged:** `docs/progress-m03-complete` approved by Saad → merged (c63b5f2) — Uzair now 2/2 authored, Saad 2/2 reviewed |
| 2026-09-29 | **M03 close-out (Uzair):** guard rails re-proven on `dev` (5 MB + `sk-…` blocked), `pre-commit run --all-files` green after EOF fix, suite 16 passed/1 skipped + ruff clean, merged/stale remote branches deleted, docs + `REPORT.md` scoreboard synced (branch `docs/module-03-closeout` → PR) |
| 2026-09-29 | **PR #5 merged** (`f5a3d8b`) — close-out docs landed; protection relaxed→merged→restored and re-verified (`approvals=1 · enforce_admins=true · no force-push`), `staging`/`main` untouched |
| 2026-09-29 | **M01 evidence committed:** `docs/evidence/module-01-collaborators.png` (msaadsbr · Collaborator) + `module-01-two-authors.png` (both authors in `git log`) → PR #6 |
| 2026-09-29 | **PR #6 merged** (`922ac9a`) — M01 evidence on `dev`; stale remote branches deleted; only `main`/`staging`/`dev` remain |
| 2026-09-29 | **M04 (Uzair):** `data/initial-dataset` from `dev`; `dvc init` + track both CSVs; DagsHub remote over **HTTPS** (DVC 3.67 has no `dvc dagshub-setup` and rejects `dagshub://`); auth written only to `.dvc/config.local` (git-ignored); `dvc push` → 2 files → commit `b3d4a32` → pushed |
| 2026-09-29 | **M04 reviewer test:** fresh GitHub clone → `dvc status` shows deleted outs → `dvc pull` (2 files added) → md5 pointer = clone = local for both CSVs; `git rev-list --objects --all` → 0 `*.csv` objects → evidence `docs/evidence/module-04-dvc-pull-verification.txt` |
| 2026-09-29 | **PR #7 opened** `data/initial-dataset` → `dev` with hashes/sizes + checklist; M03 hook-output PNGs + module-04 doc correction + trackers staged into the same PR |
| 2026-09-29 | **PR #7 merged** (`616a8fd`) — relax → squash → restore protection, re-verified (`approvals=1 · enforce · no force-push · no deletions` ×3); `data/initial-dataset` deleted (local + remote); post-merge `dev` green (pre-commit + 17 tests) |
| 2026-09-29 | **DagsHub fix:** repo on dagshub.com was `empty=True` (storage-only) so its UI showed no dataset — added `dagshub` git remote and mirrored `dev`/`main`/`staging` (default branch there = `dev`); pointer `train.csv.dvc` now served publicly with matching md5 → dataset visible on the DagsHub homepage |
| 2026-09-29 | **M05 (Uzair):** `feat/eda-notebook` — deps added (`matplotlib`, `seaborn`, `nbstripout`); `features.py` promoted (`build_features` + 5 unit tests, pandas-3 dtype fix); `notebooks/01-eda.ipynb` + `.py` pair authored, executed top-to-bottom (103 904 rows · 310 missing delays · 0 duplicates · 43.3 % satisfied · Online boarding r=0.50 top), conclusions written from the actual outputs, stripped to 8 931 B with 0 image payloads |
| 2026-09-29 | **PR #9 opened** — `feat: EDA notebook with jupytext pair and tested feature helper` → `dev`; 22 tests + ruff + pre-commit all green on the branch |
| 2026-09-29 | **PR #9 merged** (`ff05906`) — M05 done; DagsHub mirror synced; M06 brief written for Saad (owner per `00-overview.md:102`) |
| 2026-09-29 | **Saad's M06 attempt → wrong PR #10** (`dev` → `main`, M05-styled title, no `feat/dvc-pipeline` branch, no `dvc.yaml` anywhere) |
| 2026-09-29 | **PR #10 handled per team decision (no re-looping Saad):** title corrected → Uzair submitted the full review checklist + **APPROVED** (his 2nd review, Saad authored it → his 2nd PR) → **rebase-merged** into `main` (`86299fe`, CONTRIBUTING §3) → local `main` + DagsHub mirror synced; protection re-verified ×3 |
| 2026-09-30 | **M06 (Uzair):** `feat/dvc-pipeline` — `run_at` removed (determinism); `dvc.yaml` wired (3 stages); two DVC gotchas solved live: `- seed:`-style params entries mean "file named seed" → colon-free keys; metrics need `cache: false` to stay git-tracked; commits `050ee1c` (code) + `9e6ff42` (lock+metrics, `commit_sha` matches code commit); `dvc push` 3 files; fresh-clone checkpoint PASS → evidence `docs/evidence/module-06-dvc-repro-verification.txt`; PR #11 opened |

(End of file - total 176 lines)
