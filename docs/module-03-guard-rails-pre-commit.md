# Module 03 · Guard rails: pre-commit and secrets

**Phase 3** · Owner: **Saad** (author), **Uzair** (reviewer) · Rubric: *Repo hygiene (10)*, *PRs (20)*
**Branch:** `feat/pre-commit` → PR → `dev`
**Checkpoint:** committing a 5 MB file or a fake API key is blocked. **Screenshot it.**

## Objective

Make it structurally impossible to commit junk: bad formatting, dirty notebooks, huge files, or
secrets.

## Tasks

### 1. Branch

```bash
git switch dev && git pull
git switch -c feat/pre-commit
```

### 2. `.pre-commit-config.yaml` (minimum set required by the PDF)

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.16.9
    hooks:
      - id: ruff            # lint, --fix
      - id: ruff-format

  - repo: https://github.com/kynan/nbstripout
    rev: 0.8.1
    hooks:
      - id: nbstripout
        files: \.ipynb$

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: check-added-large-files
        args: ["--maxkb=1024"]        # 1 MB limit
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: check-yaml
      - id: check-merge-conflict
      - id: detect-private-key

  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.28.0
    hooks:
      - id: gitleaks            # secret scanner (alternative: detect-secrets)
```

- [ ] `ruff` (lint + format)
- [ ] `nbstripout`
- [ ] `check-added-large-files` at **1 MB**
- [ ] secret scanner (`gitleaks` **or** `detect-secrets`)
- [ ] pin `rev:` tags — never `main`

Add ruff config to `pyproject.toml` so CI (M08) and hooks agree:

```toml
[tool.ruff]
line-length = 100
src = ["src", "tests"]

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]
```

### 3. Every member installs the hooks

```bash
uv run pre-commit install
uv run pre-commit run --all-files     # fix anything it flags, commit the fixes
```

- [ ] Uzair: `pre-commit install` ✅
- [ ] Saad: `pre-commit install` ✅

### 4. Prove the guards work (before opening the PR)

```bash
# large file must be blocked
dd if=/dev/zero of=big.bin bs=1M count=5
git add big.bin      # → pre-commit fails: file larger than 1 MB
rm big.bin

# fake secret must be blocked
echo 'API_KEY = "sk-1234567890AAAAAAAAAAAAAAAA"' > leak.py
git add leak.py      # → gitleaks fails
rm leak.py
```

- [ ] 5 MB file blocked
- [ ] fake API key blocked
- [ ] **📸 screenshot both for REPORT.md**

### 5. Open the PR

```bash
git add .pre-commit-config.yaml pyproject.toml
git commit -m "chore: add pre-commit hooks (ruff, nbstripout, large files, secrets)"
git push -u origin feat/pre-commit
```

- [ ] PR title: `chore: add pre-commit guard rails` → base **`dev`**
- [ ] Use the PR template (create `.github/pull_request_template.md` now — content in Module 07)
- [ ] **Uzair reviews**: checks out the branch, runs `uv run pre-commit run --all-files`,
      fills the checklist as a PR comment
- [ ] Squash-merge into `dev`, delete `feat/pre-commit`

## Checkpoint

- [ ] `.pre-commit-config.yaml` on `dev`
- [ ] Screenshot: blocked large file + blocked secret
- [ ] PR merged with a real review from Uzair

## Pitfalls

- Hooks installed in only one clone → the other member commits dirty files.
- `check-added-large-files` at a huge limit → pointless; must be **1 MB**.
- Committing `pre-commit` config but never running `--all-files`, so legacy files stay dirty and
  Module 08's `ruff format --check` goes red.
