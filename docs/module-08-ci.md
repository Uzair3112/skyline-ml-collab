# Module 08 · CI on every pull request

**Phase 8** · Owner: **Uzair** (Platform A), **Saad** (reviewer) · Rubric: *CI (10)*, *PRs (20)*
**Branch:** `feat/ci` → PR → `dev`
**Checkpoint:** a deliberately broken test causes a **red check that blocks merging**. 📸

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

- [ ] lint: `ruff check` + `ruff format --check`
- [ ] unit tests: `pytest tests/`
- [ ] data checks: schema, value ranges, null counts
- [ ] smoke train: a few hundred rows, end to end

### 3. Data checks in CI — the DVC problem

CI runners have **no DagsHub credentials**, so `dvc pull` will fail on a fresh PR from a fork.
Solutions (pick one):

- [ ] **(simplest, allowed by the PDF)** commit a small fixture
      `tests/fixtures/sample.csv` (~500 rows, **< 1 MB** so pre-commit allows it) and run schema /
      range / null checks against it
- [ ] *(better, optional)* use DagsHub secrets + `dvc pull` in the `data-checks` job — requires
      adding `DAGSHUB_TOKEN` as a repo secret; never hardcode it

`data_checks` must verify at minimum:
- [ ] expected column names/dtypes present
- [ ] `satisfaction` ∈ {`satisfied`, `neutral or dissatisfied`}
- [ ] rating columns within `0..5`
- [ ] null counts below agreed thresholds

### 4. Smoke train

- [ ] `smoke` module takes `--rows 300`, runs prepare→train→evaluate on a slice
- [ ] finishes in < ~2 min, exits non-zero if metrics are NaN / pipeline throws

### 5. Bonus: CML metrics comment (+5)

```yaml
  cml-comment:
    runs-on: ubuntu-latest
    needs: [lint, tests, data-checks, smoke-train]
    steps:
      - uses: actions/checkout@v4
      - uses: iterative/setup-cml@v2
      - uses: astral-sh/setup-uv@v5
      - run: uv sync --frozen
      - run: uv run python -m ml_skyline.smoke --rows 300 --report report.md
      - name: Publish metrics
        uses: iterative/report-pull-request@v2
        with:
          path: report.md
```

- [ ] *(optional)* CML posts the metrics table as a PR comment → **+5 bonus**
- [ ] Alternatively take the **hotfix bonus** in Module 09

### 6. Prove CI fails

```bash
echo "def test_broken(): assert 1 == 2" >> tests/test_ci_gate.py
git add tests/test_ci_gate.py
git commit -m "test: deliberately break CI to prove the gate"
git push -u origin feat/ci
```

- [ ] PR shows a **red** `tests` check
- [ ] 📸 screenshot (red check) for REPORT.md
- [ ] Then delete the broken test, commit, and show a **green** PR
- [ ] 📸 screenshot (passing check) for REPORT.md

### 7. Make the checks required

After `feat/ci` merges into `dev`:

- [ ] Branch protection on `main`, `staging`, `dev`: **required status checks** =
      `lint`, `tests`, `data-checks`, `smoke-train`
- [ ] "Require branches to be up to date before merging" — optional but good
- [ ] Verify: a PR with a failing check **cannot** be merged (checkpoint)

## Checkpoint (evidence for REPORT.md)

- [ ] 📸 failing CI check screenshot
- [ ] 📸 passing CI check screenshot
- [ ] Required status checks enabled on all three protected branches

## Pitfalls

- Workflow only triggers on `push` → no CI on PRs (the PDF requires `pull_request`).
- `uv sync` without `--frozen` silently updates deps → CI ≠ local.
- Data-check job that needs secrets but none configured → always-red CI.
- Not running `ruff format` before pushing → the `format --check` job fails and blocks everything.
