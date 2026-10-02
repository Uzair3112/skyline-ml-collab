# Progress board

> Update this file as you go. Status: ⬜ not started · 🟡 in progress · ✅ done · ❌ blocked
> **Also** tick the checkboxes inside each module file — this board is the summary.

**Last updated:** 2026-09-30 · **Current phase:** Modules **01–09 all complete** → next: final review of `REPORT.md` + submission

## Module status

| # | Module | Status | Branch | PR | Checkpoint evidence |
|---|--------|--------|--------|----|---------------------|
| 01 | Team & repository setup | ✅ | *branches deleted* | — | ✅ 2 authors · ✅ Saad write=push · ✅ 📸 collaborators + two-author evidence · ⬜ instructor skipped (user decision) |
| 02 | Scaffold & import | ✅ | `main` pushed (`5078478`) | **#2 merged** | ✅ import in `git log` · ✅ 3/3 protected · ✅ direct push rejected `GH006` · ✅ Saad review |
| 03 | Pre-commit & secrets | ✅ | `feat/pre-commit` deleted | **#3 merged** | ✅ config + evidence file · ✅ Uzair review · ✅ re-proven on `dev` · ✅ 📸 hook-output PNGs committed (PR #7) |
| 04 | DVC data versioning | ✅ | `data/initial-dataset` (deleted) | **#7 merged** (`616a8fd`) | ✅ pointers only, 0 `*.csv` in history · ✅ `dvc push` before `git push` · ✅ fresh-clone `dvc pull` md5 ×2 · ✅ DagsHub git mirror (UI shows dataset) · evidence `module-04-dvc-pull-verification.txt` |
| 05 | Notebooks | ✅ | `feat/eda-notebook` (after merge) | **#9 merged** | ✅ 0 outputs/base64 in ipynb (8.9 KB) · ✅ jupytext pair `01-eda.py` + metadata · ✅ `build_features` promoted + 5 tests · ✅ executed top-to-bottom via nbconvert |
| 06 | Reproducible pipeline | ✅ | `feat/dvc-pipeline` (after merge) | **#11 merged** | ✅ `dvc.yaml` 3 stages + `dvc.lock` + `params.yaml` · ✅ `run_at` removed (deterministic) · ✅ fresh-clone `dvc pull && dvc repro` identical metrics (`docs/evidence/module-06-dvc-repro-verification.txt`) · ✅ `dvc push` before `git push` |
| 07 | Experiments & PRs | ✅ | `exp/*` (kept), others deleted | **#12–#16 merged** | ✅ 6 experiments (`dvc exp show` evidence) · ✅ conflict reproduced+resolved by rebase (#12→#13) · ✅ data update + version-switch demo (#14) · ✅ winner promoted (#15) · ✅ `exp/uzair-model-sweep` abandoned unmerged · ⬜ Saad's changes-requested review + his own 3 exps (account, pending) |
| 08 | CI | ✅ | `feat/ci`, `proof/red-gate` (deleted) | **#18, #21 merged** (`e00e790`, `330b89b`) | ✅ 4-job PR workflow (`uv sync --frozen`) · ✅ fixture-based data-checks (no DVC secrets) · ✅ smoke 12 s · ✅ 33 tests · ✅ red→green on #18 · ✅ required checks ×3 (strict) · ✅ failing-check merge → **405** (#19) · ✅ **CML bonus** — `cml-comment` job posts metrics table on PRs (#21, run `36741151650`) · ✅ 📸 PNG red/green committed (`module-08-ci-{red,green}.png`) · evidence `docs/evidence/module-08-*.txt` |
| 09 | Release & report | ✅ | `release/*`, `sync/*` (deleted), `exp/*` kept | **#23, #24, #25, #26✂, #27, #28, #29, #30** | ✅ release PRs `release: v1.0` (#27 → `staging` `a110753`, #28 → `main` `bb6517a`), 5/5 CI green each · ✅ **`model-v1.0`** on `main` + **`model-v1.0.1`** hotfix (`e7ccda0`) · ✅ independent reproduction on a **fresh clone**: every value metric byte-identical, `roc_auc 0.9941573399364485` stable ×4 · ✅ reproduction **caught 2 real defects** (`n_jobs=-1` thread order → #25; `dvc push` never run after the retrain) · ✅ #26 closed (rebase-merge SHA divergence ⇒ `dirty` + no CI) → release-branch pattern · ✅ hotfix `--report` clobber + 2 tests (#29) and `main` fast-forwarded back into `dev` (#30) · ✅ DagsHub mirrored (`dev`/`staging`/`main` + both tags) · evidence `docs/evidence/module-09-reproduction.txt` |

## Rules scoreboard

| Requirement | Target | Status |
|-------------|--------|--------|
| Uzair authored merged PRs | ≥ 2 | **29 / 2** ✅ (PR #2, #4, #5, #6, #7, #8, #9, #11, #12, #13, #14, #15, #16, #17, #18, #20, #21, #22, #23, #24, #25, #27, #28, #29, #30, #31, #32, #33, #34) |
| Uzair reviewed PRs | ≥ 2 | **2 / 2** ✅ (PR #3, #10) |
| Saad authored merged PRs | ≥ 2 | **2 / 2** ✅ (PR #3, #10) |
| Saad reviewed PRs | ≥ 2 | **3 / 2** ✅ (PR #2, PR #4, PR #34 → **changes requested**) |
| "Changes requested" reviews | ≥ 1 | **1 / 1** ✅ (Saad on **PR #34**, 2026-09-30: 4 blocking inline comments — DVC auth missing, bare `dvc` instead of `uv run`, inaccurate "one tree" claim, wrong `commit_sha` wording — all addressed in `f15b167`, CI 5/5) |
| Experiments per member | ≥ 3 | Uzair **3 / 3** ✅ (`exp/uzair-model-sweep`) · Saad 3 run on `exp/saad-depth-sweep` **by Uzair** (deviation recorded; his own runs pending his clone) |
| Protected branches | `main`, `staging`, `dev` | **3 / 3** ✅ |
| Required CI checks on | all 3 branches | **3 / 3** ✅ (`lint, tests, data-checks, smoke-train`, strict — failing PR merge proven 405) |
| Release tag | `model-v1.0` on `main` | ✅ `refs/tags/model-v1.0` → `bb6517a` (also `model-v1.0.1` → `e7ccda0`) |
| Independent reproduction | matches exactly | ✅ fresh clone of `staging` @ `a110753`: all value metrics byte-identical (only `commit_sha` differs, by design) — comment on PR #27 + `docs/evidence/module-09-reproduction.txt` |
| `REPORT.md` | complete | ✅ **complete** — M01–M09, reproducibility table (commit SHAs + tags), retrospective §5 |
| Bonus | CML comment **or** `model-v1.0.1` | ✅ **both** — CML comment (M08, PR #21) **and** the `model-v1.0.1` hotfix (M09, PR #29 → `main` → PR #30 back into `dev`) |

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
| **"Changes requested" review (≥1)** | Saad | ✅ **PR #34** (2026-09-30) — 4 blocking inline comments on the README release/reproduce sections; fixed in `f15b167`, CI 5/5. The one rubric item that needed his account is done |
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

### ⚠️ Open in Module 07 — **DONE ✅** (dual-role execution; Saad's account items pending)

| # | Item | Owner | Status |
|---|------|-------|--------|
| 1 | 7.5 conflict choreography: round A `6→10` PR #12 merged (`c92949c`), round B rebased into it → **CONFLICT** → resolved keeping **12** (evidence beats both) → PR #13 merged (`4cc62cf`) | Uzair | ✅ evidence `module-07-conflict-rebase.txt` |
| 2 | 7.4 data update: fill **310 `Arrival Delay` nulls at source** (median 0), pointer `7795cca…` → `389295a…`, version-switch demo (`checkout`+`dvc checkout` ×2, hashes verified) → PR #14 merged (`2bb2d00`) | Uzair | ✅ evidence `module-07-data-version-switch.txt` |
| 3 | 7.1 experiments ≥3 each: 6 runs — `minus-skis`/`dural-raja`/`flamy-code` (Uzair) + `fuggy-ices`/`straw-froe`/`blank-axon` (Saad's dimension, run by Uzair) | Uzair | ✅ evidence `module-07-exp-show.md`; **Saad's own 3 runs pending his clone** |
| 4 | 7.2 promote winner `straw-froe` (depth 24, f1 0.9476→0.9562) → PR #15 merged (`f97069b`) | Uzair | ✅ (brief says author=Saad → deviation recorded) |
| 5 | 7.6 abandoned branch: `exp/uzair-model-sweep` (and `exp/saad-depth-sweep`) **kept unmerged** — logreg −0.09 f1, other runs non-comparable splits | Uzair | ✅ rationale in REPORT §M07 |
| 6 | 7.3 reviews: every PR asks `@msaadsbr` for retro-review; **changes-requested delivered later on PR #34** | Saad | ✅ changes-requested · retro-reviews ⬜ pending |
| 7 | Close-out: REPORT/PROGRESS/module-07/docs README synced → PR #16 | Uzair | ✅ (this PR) |

### ✅ Open in Module 09 — **DONE** (release + reproduction + report + Saad's changes-requested review)

| # | Item | Owner | Status |
|---|------|-------|--------|
| 1 | Release PR `dev` → `staging`, title exactly `release: v1.0` — three attempts: **#24** merged (then the reproduction failed) · **#25** the fix · **#26** closed (see below) · **#27** from a `release/v1.0` branch cut *off* `staging` → clean diff, **5/5 CI green**, merge-commit → `staging` = `a110753` | Uzair | ✅ (brief says author=Saad → deviation recorded) |
| 2 | Independent reproduction in a **brand-new clone** of `staging` (`uv sync --frozen` + `dvc pull` + `dvc repro` + `dvc repro -f`) → **all value metrics byte-identical** (`roc_auc 0.9941573399364485` stable ×4); only `commit_sha` differs (by design) → posted as a comment on #27 | Uzair | ✅ (brief says the *non*-trainer runs it → Saad unavailable, Uzair in a clean clone) |
| 3 | Reproduction's two catches: **(a)** `roc_auc` moved between runs — `RandomForestClassifier(n_jobs=-1)` accumulates `predict_proba` in thread-completion order → `train.n_jobs: 1` + 2 tests (#25); **(b)** #25's retrain was never `dvc push`ed → fresh clone failed `dvc pull` on `models/model.pkl` → pushed, re-verified | Uzair | ✅ evidence `module-09-reproduction.txt` |
| 4 | `staging` → `main`: **#28** (release branch cut off `main`, resolved to `staging`, merge-commit) → `main` = `bb6517a`, tree == `staging` · tag **`model-v1.0`** pushed | Uzair | ✅ |
| 5 | Optional hotfix (+5): `smoke --report` clobbered `REPORT.md` on case-insensitive FS → **#29** refuses to overwrite a non-smoke-report file (exit 2) + 2 tests → rebase-merged `e7ccda0` → tag **`model-v1.0.1`** | Uzair | ✅ |
| 6 | `main` merged back into `dev`: **#30** (fast-forward `7232a66 → e7ccda0`) → `git diff dev main` empty, so the hotfix cannot be lost by the next release | Uzair | ✅ |
| 7 | DagsHub mirror: `dev`/`staging`/`main` + both tags pushed | Uzair | ✅ |
| 8 | Retrospective → `REPORT.md` §5 (reproducibility table, what broke, what we would standardise) | Uzair | ✅ |
| 9 | Close-out: short-lived branches deleted (`fix/*`, `release/*`, `sync/*`), `exp/*` kept, REPORT/module-09/PROGRESS/docs README synced → this PR | Uzair | ✅ |
| 10 | **Saad's changes-requested review (rubric ≥1)** — reviewed the README release/reproduce section on **PR #34** with 4 blocking inline comments (missing DVC auth setup, bare `dvc` instead of `uv run`, inaccurate "one tree" claim, wrong `commit_sha` wording) → all fixed in `f15b167` | Saad | ✅ 2026-09-30 · ⬜ optional: retro-reviews of #27/#28 |
| 11 | README gains **Release status** + **Reproduce the release** (4 commands, expected metrics at full precision, evidence link) → PR #34 merged (`e14a558`) | Uzair | ✅ 5/5 CI green |

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
| 2026-09-30 | **PR #11 merged** (`9b3dfe0`) — M06 done; branch deleted; DagsHub `dev` synced; `dvc repro` up-to-date on post-merge `dev` |
| 2026-09-30 | **M07 conflict choreography (Uzair dual-role):** round A `max_depth 6→10` → PR #12 merged (`c92949c`); round B branched *before* the merge (`6→8`) → PR #13 opened → `git rebase origin/dev` reproduced the conflict on `params.yaml` → resolved keeping **12** after running all three candidates (8: f1 0.9273 < 10: 0.9398 < **12: 0.9476**) → `dvc repro -f` at resolution commit → force-push → PR #13 merged (`4cc62cf`) |
| 2026-09-30 | **M07 data update:** string-preserving fill of 310 `Arrival Delay` nulls at source (median 0 == pipeline imputer) → pointer `7795cca…`→`389295a…`; `dvc push` (2 socket-timeout retries) before `git push`; repro → metrics byte-identical (only `commit_sha` moved); version-switch demo verified both hashes → PR #14 merged (`2bb2d00`) |
| 2026-09-30 | **M07 experiments:** 6 runs (3 on `exp/uzair-model-sweep`: logreg/test_size 0.3/seed 7 · 3 on `exp/saad-depth-sweep`: depth 4/24/trees 300, run by Uzair); `dvc exp run` applies results to workspace → restored baseline between runs; winner **`straw-froe` depth 24 (f1 0.95615)**; `dvc exp show -a --md` evidence committed on the saad branch (`dfbed05`); both `exp/*` branches pushed and **kept unmerged** |
| 2026-09-30 | **PR #15 merged** (`f97069b`) — winner promoted (`dvc exp apply straw-froe`), dev baseline f1 0.94756 → **0.95615**; pipeline up-to-date after merge; promote branch deleted |
| 2026-09-30 | **M07 close-out (Uzair):** REPORT/PROGRESS/module-07/docs README + conflict evidence synced → PR #16 (`313cf20`) |
| 2026-09-30 | **M07 evidence gap fixed:** `module-07-exp-show.md` existed only on `exp/saad-depth-sweep`, not on `dev` (REPORT referenced it) → cherry-picked onto dev → PR #17 (`f9a2c7e`) |
| 2026-09-30 | **M08 build (Uzair):** `feat/ci` — `.github/workflows/ci.yml` (4 jobs on `pull_request`, `uv sync --frozen`, concurrency cancel); `ml_skyline.data_checks` (schema/labels/0..5 ranges/1% nulls) against committed **69 KB fixture** `tests/fixtures/sample.csv` (500-row raw slice, no DVC secrets needed); `ml_skyline.smoke --rows 300` (12 s, NaN/exception → exit 1, `--report` for CML); +11 tests → **33 total**; local pre-flight identical to CI commands |
| 2026-09-30 | **PR #18 CI run:** all 4 checks green on first push (`89dfeb4`) → red proof `c60fdfd` (broken test → `tests` FAILURE, others green) → evidence captured → green restore `9495a97` → **PR #18 merged** (`e00e790`) |
| 2026-09-30 | **Required status checks enabled ×3** (`lint, tests, data-checks, smoke-train`, strict) on `main`/`staging`/`dev`; **merge-block proof:** PR #19 (red `tests`) `PUT /merge` → **HTTP 405** → PR #19 closed, branch deleted; merge-script restore payload updated to keep `required_status_checks` |
| 2026-09-30 | **M08 close-out (Uzair):** REPORT/PROGRESS/module-08/docs README + red/green/405 evidence synced → PR #20 — 📸 PNG screenshots of the check pages still to be captured by Uzair |
| 2026-09-30 | **M08 bonus (Uzair):** `cml-comment` job added to `ci.yml` (`iterative/setup-cml@v2` + `ml_skyline.smoke --report` + `cml comment create --target=pr`; the doc's sketched `iterative/report-pull-request@v2` action **404s — does not exist**); fork guard + non-required so it can never block a merge → PR **#21**, all 5 checks green, metrics table posted by `github-actions[bot]` → squash-merged `330b89b`, protection restored ×3, DagsHub `dev` synced, branch deleted |
| 2026-09-30 | **M08 final close-out (Uzair):** 📸 PNG screenshots captured headless from the Actions run pages — red `module-08-ci-red.png` (run 36629822692: Status Failure, `tests` ✕) + green `module-08-ci-green.png` (run 36741151650: Success, 5/5 incl. `cml-comment`); CML evidence `module-08-cml-comment.txt`; `--pr` → `--target=pr` (deprecation); module-08/PROGRESS/REPORT synced → this PR |
| 2026-09-30 | **M09 prep:** PR #23 squash-merged `5432e49` — `metrics.json.commit_sha` re-logged so it matches the released code; **#24** `release: v1.0` rebase-merged → `staging` = `7c691d7` (tree identical to `dev`); DagsHub `staging` synced |
| 2026-09-30 | **M09 reproduction attempt 1 — FAILED:** fresh clone + `dvc pull` (md5s matched) + `dvc repro` clean, but `roc_auc` moved run-to-run (`…3446515221`, `…3399364484`, `…3399364483`, `…3493665958`) — `n_jobs=-1` accumulates `predict_proba` in thread-**completion** order → **PR #25**: `params.yaml train.n_jobs: 1`, `build_model` reads it, +2 regression tests → verified 4/4 identical → squash-merged `7232a66` |
| 2026-09-30 | **M09 PR #26 closed:** direct `dev`→`staging` reported `mergeable=dirty` — #24's rebase had landed **rewritten SHAs** on `staging`, so `dvc.lock`/`metrics.json`/`params.yaml` are add/add + content conflicts, and with no merge ref GitHub starts **no CI run** (confirmed: 0 check-runs on `7232a66`) → superseded by the release-branch pattern |
| 2026-09-30 | **M09 release PR #27** (head `release/v1.0` = `origin/staging` + merged `dev`, conflicts resolved to `dev`; `git diff release/v1.0 dev` empty): clean diff → **5/5 CI green** → merge-commit → **`staging` = `a110753`**, tree == `dev`; protection restored (approvals 1, strict checks ×4, enforce_admins) |
| 2026-09-30 | **M09 reproduction attempt 2 — caught defect (b):** fresh clone's `dvc pull` failed on `models/model.pkl` — #25's `dvc repro -f` retrained (pickle bytes differ with `n_jobs=1`) but only local `dvc status` was run, never `dvc push` → pushed from the authoring clone (`dvc status -c` → *in sync*) → `dvc pull` OK → plain `dvc repro` = "up to date" + clean tree → `dvc repro -f` = **only `commit_sha` changed** → every value metric byte-identical, `roc_auc 0.9941573399364485` stable on a 4th run → **comment posted on #27**, evidence `docs/evidence/module-09-reproduction.txt` |
| 2026-09-30 | **M09 promotion #28:** release branch cut from `main` + merged `staging` (5 conflicts resolved to `staging`; verified `git diff` empty, no file exists on `main` that `staging` lacks) → **5/5 CI green** → merge-commit → **`main` = `bb6517a`**, tree == `staging` · annotated tag **`model-v1.0`** (`7c2dd1e`) pushed |
| 2026-09-30 | **M09 optional hotfix (+5):** `smoke --report <path>` wrote blindly, so `--report report.md` resolved to **`REPORT.md`** on case-insensitive filesystems (already listed under REPORT "Known issues", handled only by convention) → **PR #29** `fix: refuse to clobber non-report files` (`REPORT_HEADER` guard, exit 2, original content untouched; +2 tests → **37 total**) → rebase-merged `e7ccda0` → tag **`model-v1.0.1`** (first tag attempt landed on the PR head `b7a7a32` because `main` wasn't checked out — deleted and re-cut on `e7ccda0`) |
| 2026-09-30 | **M09 merge-back #30:** `main` → `dev` was a **fast-forward** (`bb6517a` already contains all of `dev` through `staging`/`bc2207b`) → 5/5 CI green → merged `ea59e2a`; `git diff dev main` → **empty**; DagsHub `dev`/`main` + `model-v1.0.1` pushed; short-lived branches deleted (`fix/report-clobber`, `release/v1.0`, `release/v1.0-main`, `sync/main-hotfix-into-dev`), `exp/*` kept |
| 2026-09-30 | **M09 close-out (Uzair):** `module-09-release.md` checkboxes ticked, PROGRESS + docs README scoreboard + REPORT (reproducibility table, §5 retrospective) synced → this PR |
| 2026-10-01 | **Docs promoted to the default branch:** #31 (close-out, squash `826159f`) → `dev` · #32 `dev`→`staging` → `39f3220` · #33 `staging`→`main` → `5b4c4b0`; all three trees identical, DagsHub re-synced; `release/docs-*` and `docs/module-09-closeout` branches deleted — the full `REPORT.md` now sits on GitHub's default branch |
| 2026-09-30 | **Saad delivers the rubric's "changes requested" review** on **PR #34** (README release + reproduce sections): 4 blocking inline comments — (1) a fresh clone cannot `dvc pull` (auth lives in git-ignored `.dvc/config.local`, README silent), (2) bare `dvc`/`pre-commit` are not on `PATH` after `uv sync` → use `uv run`, (3) `model-v1.0` vs `main` do **not** share one tree (v1.0.1 hotfix + docs), (4) the `commit_sha` sentence contradicted what the commands actually do |
| 2026-10-02 | **All 4 review comments fixed in `f15b167`** (auth block added to *Getting started* per `module-04` recipe, every tool through `uv run`, tree claim reworded to `params.yaml`+`dvc.lock` identity, `commit_sha` wording taken from the reviewer) → 5/5 CI green → replied inline on each comment → re-requested his approval (still offline) → merged with the **documented approval-rule relaxation** (protection restored + verified on `dev`) → `e14a558` |
