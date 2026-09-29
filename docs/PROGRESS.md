# Progress board

> Update this file as you go. Status: ⬜ not started · 🟡 in progress · ✅ done · ❌ blocked
> **Also** tick the checkboxes inside each module file — this board is the summary.

**Last updated:** 2026-09-29 · **Current phase:** Modules 01–03 ✅ DONE (verified on `dev`) → next: **Module 04**

## Module status

| # | Module | Status | Branch | PR | Checkpoint evidence |
|---|--------|--------|--------|----|---------------------|
| 01 | Team & repository setup | ✅ | *branches deleted* | — | ✅ 2 authors · ✅ Saad write=push · ⬜ instructor skipped (user decision) |
| 02 | Scaffold & import | ✅ | `main` pushed (`5078478`) | **#2 merged** | ✅ import in `git log` · ✅ 3/3 protected · ✅ direct push rejected `GH006` · ✅ Saad review |
| 03 | Pre-commit & secrets | ✅ | `feat/pre-commit` deleted | **#3 merged** | ✅ config + evidence file · ✅ Uzair review · ✅ re-proven on `dev` · ⬜ 📸 screenshots |
| 04 | DVC data versioning | ⬜ | `data/initial-dataset` | # | CSV absent from git history |
| 05 | Notebooks | ⬜ | `feat/eda-notebook` | # | no outputs in PR diff |
| 06 | Reproducible pipeline | ⬜ | `feat/dvc-pipeline` | # | fresh-clone `dvc repro` identical metrics |
| 07 | Experiments & PRs | ⬜ | `exp/*` | # | ≥3 exp each, changes-requested, conflict PR |
| 08 | CI | ⬜ | `feat/ci` | # | 📸 red + green checks |
| 09 | Release & report | ⬜ | `staging` | # | `model-v1.0` + independent reproduction |

## Rules scoreboard

| Requirement | Target | Status |
|-------------|--------|--------|
| Uzair authored merged PRs | ≥ 2 | **2 / 2** ✅ (PR #2, PR #4) |
| Uzair reviewed PRs | ≥ 2 | **1 / 2** (PR #3) |
| Saad authored merged PRs | ≥ 2 | **1 / 2** (PR #3) |
| Saad reviewed PRs | ≥ 2 | **2 / 2** ✅ (PR #2, PR #4) |
| "Changes requested" reviews | ≥ 1 | 0 / 1 |
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
| 📸 Optional screenshots: collaborators page, protection rules | Uzair | ⬜ not required by `REPORT.md` |
| DagsHub account created + `dvc dagshub-setup` run | Uzair | ⬜ (Module 04) |

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
| 9 | 📸 Screenshot both blocked commits for REPORT.md | Uzair + Saad | ⬜ (transcripts in `docs/evidence/`, images manual) |
| 10 | Delete merged branches: `feat/pre-commit`, `claude/lucid-mendel-7k6uqi`, `docs/module-02-closeout`, `docs/progress-m03-complete` | Uzair | ✅ (housekeeping with the M03 close-out PR) |
| 11 | Re-prove both guard rails **on `dev`** after the merge | Uzair | ✅ `docs/evidence/module-03-reverify-on-dev.txt` |

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

(End of file - total 176 lines)
