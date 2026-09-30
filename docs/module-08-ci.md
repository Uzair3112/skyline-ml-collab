# Module 08 · CI on every pull request

**Phase 8** · Owner: **Uzair** (Platform A), **Saad** (reviewer) · Rubric: *CI (10)*, *PRs (20)*
**Branch:** `feat/ci` → PR **#18** (merged `e00e790`) → `dev` · proof PR **#19** (closed, unmergeable) ·
close-out PR **#20** · CML bonus PR **#21** (merged `330b89b`) · final close-out PR **#22**
**Checkpoint:** ✅ a deliberately broken test caused a **red check that blocks merging** (HTTP 405 —
`docs/evidence/module-08-merge-blocked.txt`), with 📸 PNG captures now committed:
[`module-08-ci-red.png`](evidence/module-08-ci-red.png) (run `36629822692`: `tests` ✕, Status *Failure*)
· [`module-08-ci-green.png`](evidence/module-08-ci-green.png) (run `36741151650`: 5/5 green, Status *Success*).

## Objective

Every PR into `dev`, `staging` or `main` must pass: lint, unit tests, data checks, smoke train.

## Tasks

### 1. Branch

```bash
git switch dev && git pull
git switch -c feat/ci
```

### 2. `.github/workflows/ci.yml`

```yaml
name: ci

on:
  pull_request:
    branches: [dev, staging, main]

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v5
        with: { enable-cache: true }
      - run: uv sync --frozen
      - run: uv run ruff check .
      - run: uv run ruff format --check .

  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v5
        with: { enable-cache: true }
      - run: uv sync --frozen
      - run: uv run pytest tests/ -q

  data-checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v5
        with: { enable-cache: true }
      - run: uv sync --frozen
      # DVC pull needs credentials; use a committed SAMPLE instead (see note below)
      - run: uv run python -m ml_skyline.data_checks --sample tests/fixtures/sample.csv

  smoke-train:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v5
        with: { enable-cache: true }
      - run: uv sync --frozen
      - run: uv run python -m ml_skyline.smoke --rows 300
```

- [x] lint: `ruff check` + `ruff format --check` → PR #18 job `lint` (green; local pre-flight identical)
- [x] unit tests: `pytest tests/` → 33 tests (22 existing + 11 new in `tests/test_ci_gates.py`)
- [x] data checks: schema, value ranges, null counts → `ml_skyline.data_checks`
- [x] smoke train: a few hundred rows, end to end → `ml_skyline.smoke --rows 300` (12 s)

### 3. Data checks in CI — the DVC problem

CI runners have **no DagsHub credentials**, so `dvc pull` will fail on a fresh PR from a fork.
Solutions (pick one):

- [x] **(simplest, allowed by the PDF)** commit a small fixture
      `tests/fixtures/sample.csv` (~500 rows, **< 1 MB** so pre-commit allows it) and run schema /
      range / null checks against it — **chosen**: 500 rows / 69 KB, byte-slice of the raw export
      (EOL whitespace trimmed by the hook), kept committable by `!tests/fixtures/*.csv`
- [ ] *(better, optional)* use DagsHub secrets + `dvc pull` in the `data-checks` job — requires
      adding `DAGSHUB_TOKEN` as a repo secret; never hardcode it

`data_checks` must verify at minimum:
- [x] expected column names/dtypes present
- [x] `satisfaction` ∈ {`satisfied`, `neutral or dissatisfied`}
- [x] rating columns within `0..5`
- [x] null counts below agreed thresholds (≤ 1 % per column)

### 4. Smoke train

- [x] `smoke` module takes `--rows 300`, runs prepare→train→evaluate on a slice
      (seeded random slice → `read_raw`/`encode_target`/`build_splits` → `build_pipeline` → 5 metrics)
- [x] finishes in < ~2 min (measured **12 s**), exits non-zero if metrics are NaN / pipeline throws
      (also rejects values outside 0..1; `--report report.md` writes a markdown metrics table for CML)

### 5. Bonus: CML metrics comment (+5) — ✅ done (PR #21, merged `330b89b`)

> ⚠️ **Correction to the original sketch below:** `iterative/report-pull-request@v2` **does not
> exist** (GitHub API 404). The real CML path is `iterative/setup-cml@v2` + the `cml` CLI, and
> `--pr` is deprecated — current syntax is `--target=pr` (default is `pr` anyway).

```yaml
  cml-comment:
    runs-on: ubuntu-latest
    needs: [lint, tests, data-checks, smoke-train]
    if: github.event.pull_request.head.repo.full_name == github.repository
    permissions:
      contents: read
      pull-requests: write
      issues: write
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v5
        with:
          enable-cache: true
      - uses: iterative/setup-cml@v2
      - run: uv sync --frozen
      - run: uv run python -m ml_skyline.smoke --rows 300 --data tests/fixtures/sample.csv --report cml-report.md
      - name: Publish metrics table as a PR comment
        env:
          REPO_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: cml comment create cml-report.md --target=pr
```

- [x] *(bonus)* CML posts the metrics table as a PR comment → **+5 bonus** — proven live on
      PR #21 (run `36741151650`, job `cml-comment` success, comment by `github-actions[bot]`;
      evidence `docs/evidence/module-08-cml-comment.txt`)
- [x] Not a required status check + fork guard → the bonus **cannot block a merge**
- [x] ~~Alternatively take the **hotfix bonus** in Module 09~~ — bonus taken here instead

### 6. Prove CI fails

```bash
echo "def test_broken(): assert 1 == 2" >> tests/test_ci_gate.py
git add tests/test_ci_gate.py
git commit -m "test: deliberately break CI to prove the gate"
git push -u origin feat/ci
```

- [x] PR shows a **red** `tests` check — commit `c60fdfd` on PR #18; `lint`/`data-checks`/
      `smoke-train` stayed green → `docs/evidence/module-08-ci-red.txt`
      (run `36629822692`, log: `FAILED tests/test_ci_gate.py::test_broken - assert 1 == 2`)
- [x] 📸 screenshot (red check) for REPORT.md → [`docs/evidence/module-08-ci-red.png`](evidence/module-08-ci-red.png)
      (Actions run page: Status *Failure*, `tests` ✕ with "Process completed with exit code 1",
      other three green)
- [x] Then delete the broken test, commit, and show a **green** PR — commit `9495a97`, all four
      checks success → `docs/evidence/module-08-ci-green.txt`
- [x] 📸 screenshot (passing check) for REPORT.md → [`docs/evidence/module-08-ci-green.png`](evidence/module-08-ci-green.png)
      (Actions run page: Status *Success*, 5/5 jobs green incl. `cml-comment`)

### 7. Make the checks required

After `feat/ci` merged into `dev` (PR #18, `e00e790`):

- [x] Branch protection on `main`, `staging`, `dev`: **required status checks** =
      `lint`, `tests`, `data-checks`, `smoke-train` — applied to all three (verified by GET)
- [x] "Require branches to be up to date before merging" — enabled (`strict: true`)
- [x] Verify: a PR with a failing check **cannot** be merged (checkpoint) — **PR #19**
      (red `tests`) → `PUT /pulls/19/merge` as admin, no relaxation → **HTTP 405
      MethodNotAllowed** → `docs/evidence/module-08-merge-blocked.txt`; PR #19 closed unmerged

> ⚠️ Gotcha shipped with this: the self-merge script's **restore payload must now re-include
> `required_status_checks`** — restoring the old (null) payload would silently drop the gate on
> every subsequent merge. New merge template created for PR #20+.

## Checkpoint (evidence for REPORT.md)

- [x] 📸 failing CI check screenshot → `docs/evidence/module-08-ci-red.png` (+ `module-08-ci-red.txt`)
- [x] 📸 passing CI check screenshot → `docs/evidence/module-08-ci-green.png` (+ `module-08-ci-green.txt`)
- [x] Required status checks enabled on all three protected branches (`strict: true`, 4 contexts)
- [x] Bonus: CML metrics comment posted on PR #21 → `docs/evidence/module-08-cml-comment.txt`
      (run `36741151650`, `cml-comment` job green)

## Pitfalls

- Workflow only triggers on `push` → no CI on PRs (the PDF requires `pull_request`).
- `uv sync` without `--frozen` silently updates deps → CI ≠ local.
- Data-check job that needs secrets but none configured → always-red CI.
- Not running `ruff format` before pushing → the `format --check` job fails and blocks everything.
