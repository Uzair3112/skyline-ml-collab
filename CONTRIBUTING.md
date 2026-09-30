# Contributing to `skyline-ml-collab`

Team `skyline` — **Uzair Tariq** (Data owner · Platform A) and **Muhammad Saad Sabir**
(Model owner · Platform B). Everyone codes **and** reviews.

These rules were decided once, as a team, and apply to every pull request.

---

## 1. Branching model

Work moves in **one direction only**: short-lived branches → `dev` → `staging` → `main`.
Only `main` represents production.

| Branch | Purpose | Created from | Merges into | After merge |
|--------|---------|--------------|-------------|-------------|
| `main` | Production: released, tagged models only | — | — | protected forever |
| `staging` | Release candidate, reproduced before release | `main` | `main` | protected |
| `dev` | Integration of finished work | `staging` | `staging` | protected |
| `feat/<name>` | Production code: features, pipeline changes | `dev` | `dev` | delete |
| `data/<name>` | Dataset updates tracked with DVC | `dev` | `dev` | delete |
| `exp/<member>-<idea>` | Exploration; **never merged directly** | `dev` | *nothing* — cherry-pick the winner into a `feat/` | may be abandoned |
| `fix/<name>` | Urgent fix to production | `main` | `main`, then back into `dev` | delete |

Examples:

```bash
git switch -c feat/pre-commit dev
git switch -c data/remove-duplicates dev
git switch -c exp/saad-max-depth dev
git fetch && git rebase origin/dev          # keep short-lived branches from drifting
```

**Never push directly to `dev`, `staging` or `main`.** All changes arrive through a reviewed pull
request with passing CI. (The single exception is the initial import that created `main`.)

---

## 2. Commit messages — Conventional Commits

```
<type>: <lower-case summary, imperative mood, no full stop>
```

| Type | Use for |
|------|---------|
| `feat:` | new production code or pipeline steps |
| `fix:` | bug fixes |
| `data:` | dataset changes (`data: drop 12 duplicate rows`) |
| `exp:` | experiment-only changes (`exp: try max_depth=8`) |
| `test:` | adding or fixing tests |
| `ci:` | workflow / CI changes |
| `chore:` | tooling, config, dependencies, scaffolding |
| `docs:` | documentation only |
| `refactor:` | behaviour-preserving rewrites |

Good: `feat: add scaling step` · `data: remove duplicate rows` · `exp: try max_depth=8`

- One logical change per commit; keep them small and reviewable.
- Never commit on a teammate's behalf and never rewrite their commits.

---

## 3. Merge strategy (decided once)

- **PRs into `dev` are squash-merged.** The whole branch becomes one commit on `dev`, keeping
  `dev`'s history linear and readable.
- **PRs into `staging` and `main` are rebase-merged** (or merge-commit if rebase is impossible),
  so the release history keeps the shape of the branch that was reproduced.
- **Release branches (`release/<version>`)** — added after Module 09. Once a rebase/squash merge has
  *rewritten* commit SHAs, a direct `dev → staging` or `staging → main` PR reports
  `mergeable=dirty`, and GitHub then creates **no merge ref — so no CI run starts at all**. Fix:
  cut `release/<version>` **from the base branch**, merge the source into it (resolve conflicts to
  the newer side), verify `git diff release/<version> <source>` is empty, then open the PR. The head
  always contains its base, so the diff is clean, CI runs, and the merge-commit fallback applies.
  Release PRs **#27** and **#28** follow this; the release tag is only cut after the independent
  reproduction passes.
- **Sync back from `main`** — after any hotfix, merge `main` back into `dev` in the same session
  (PR #30), otherwise the next release re-introduces the bug.

Squash-merge message follows the same Conventional Commit format as above.

---

## 4. Data and model rules (DVC)

1. **`dvc push` before `git push`** whenever data or models changed. A pushed `.dvc` pointer with
   no corresponding object breaks every teammate's `dvc pull`.
   *Added after Module 09:* a plain `dvc status` only checks the **local** cache. After any
   `dvc repro`/`dvc repro -f` run `dvc status -c` (cloud) and `dvc push` — the release reproduction
   failed on exactly this (#25 retrained the model, the new `model.pkl` object was never pushed).
2. Never `git add` a dataset, checkpoint or model file. `.gitignore` blocks `*.csv`, `*.pkl`, … and
   `pre-commit` blocks any file over 1 MB. If one lands in history, remove it with
   `git filter-repo` — a follow-up commit is not enough.
3. Credentials never go in `.dvc/config`. Keep them in `.dvc/config.local` or environment variables.
4. To move between data versions: `git checkout <sha> && dvc checkout`.

---

## 5. Reproducibility rules

1. **Never run an experiment on uncommitted code** — the SHA logged with the run would not match
   the code that produced it.
2. Every hyperparameter, split ratio and seed lives in `params.yaml`, never hardcoded in Python.
3. Set seeds for splitting, shuffling, model initialisation and sampling.
4. Fit preprocessing (imputers, scalers, encoders) on the **training split only**.
5. Notebooks: restart the kernel and *Run All* before opening a PR. Outputs are stripped by
   `nbstripout`; every notebook has a `.py:percent` jupytext pair.
6. **Any metric that accumulates over threads or floats must be deterministic.**
   `RandomForestClassifier` runs with `train.n_jobs: 1` (a `params.yaml` knob) because
   `predict_proba` is summed in thread-**completion** order — with `n_jobs=-1`, `roc_auc` changed
   between identical runs (Module 09, caught by the release reproduction). Prove it: run
   `dvc repro -f` twice and check that only `commit_sha` moves.

---

## 6. Pull requests and review

- Title describes the change; the body uses `.github/pull_request_template.md`.
- **Every PR is assigned to the teammate as reviewer.**
- The reviewer fills in the review checklist as a PR comment and **checks out the branch at least
  once for any PR that touches the pipeline** — do not approve without running it.
- Request changes at least once when something is genuinely wrong; resolve conflicts by
  `git fetch && git rebase origin/dev`, then explain the resolution in the PR.
- Target: each member authors ≥ 2 merged PRs and reviews ≥ 2.

---

## 7. Local setup

```bash
git clone git@github.com:Uzair3112/skyline-ml-collab.git
cd skyline-ml-collab
uv sync                 # reproducible environment from uv.lock
pre-commit install      # ruff, nbstripout, large-file and secret guards
dvc pull                # dataset, once DVC is configured (Module 04)

python -m ml_skyline.prepare && python -m ml_skyline.train && python -m ml_skyline.evaluate
pytest
ruff check . && ruff format --check .
```

Before every push run `pre-commit run --all-files`.
