# Module 07 · Experiments and pull requests

**Phase 7** · Owner: **both** · Rubric: *PRs & review (20)* + *DVC (15)* + *Reproducible experiments (15)*
**Checkpoint:** the PR list shows every member as both **author and reviewer**, with at least one
**"changes requested"** review.

This is where most of the collaboration marks live. Six sub-tasks.

---

## 7.1 · Experiments (≥ 3 per member)

Each member works on their own branch **from `dev`**:

```bash
git switch dev && git pull
git switch -c exp/uzair-lr-baseline     # Uzair
git switch -c exp/saad-max-depth        # Saad
```

Run at least **three** experiments each, e.g. for Saad:

```bash
uv run dvc exp run --set-param train.max_depth=4
uv run dvc exp run --set-param train.max_depth=10
uv run dvc exp run --set-param train.n_estimators=300 --set-param train.max_depth=12
uv run dvc exp show
```

Uzair can vary the model / split instead:

```bash
uv run dvc exp run --set-param train.model=logreg
uv run dvc exp run --set-param split.test_size=0.3
uv run dvc exp run --set-param seed=7
```

- [ ] Uzair: ≥ 3 experiments
- [ ] Saad: ≥ 3 experiments
- [ ] **Commit before every experiment run** (never experiment on uncommitted code)
- [ ] `dvc exp show` table pasted into the PR description **and** REPORT.md
- [ ] Branches stay short-lived; **rebase on `dev` often**: `git fetch && git rebase origin/dev`

> Need changes to `params.yaml` for experiments? Edit on the exp branch only. Two members editing
> the same line of `params.yaml` is exactly how we stage the conflict task (7.5).

## 7.2 · Promote the winner

```bash
uv run dvc exp apply <best-exp-name>
uv run dvc repro                    # refresh metrics.json
git switch dev && git pull
git switch -c feat/promote-best-model
# bring over the applied params.yaml + metrics.json changes
git add params.yaml metrics.json dvc.lock
git commit -m "feat: promote best experiment (max_depth=10, f1 0.95 → 0.96)"
git push -u origin feat/promote-best-model
```

- [ ] PR into `dev` with **metrics before → after**
- [ ] Author **Saad**, reviewer **Uzair**

## 7.3 · Review each other

- [ ] Every PR assigned to the **teammate** as reviewer
- [ ] Reviewer pastes the checklist (below) as a **PR comment**
- [ ] **At least one PR gets "changes requested"** during the project
- [ ] Each member **authors ≥ 2 merged PRs** and **reviews ≥ 2**
- [ ] Reviewers actually **check out the branch** for any pipeline-changing PR (PDF: never approve
      without running it)

## 7.4 · Data update (Data owner = Uzair)

Branch `data/remove-duplicates` from `dev`. Modify the dataset — e.g. drop duplicated rows, fix
`Arrival Delay` nulls at source, or add rows.

```bash
git switch -c data/remove-duplicates
# edit data/raw/train.csv (or regenerate via a script)
dvc add data/raw/train.csv
dvc push
git add data/raw/train.csv.dvc
git commit -m "data: drop 0 duplicate rows and fill 398 Arrival Delay nulls"
git push -u origin data/remove-duplicates
```

**Demonstrate version switching in the PR description:**

```bash
git checkout <old-sha> && dvc checkout      # old data version
git checkout data/remove-duplicates && dvc checkout   # new data version
md5sum data/raw/train.csv                   # hashes differ
```

- [ ] PR into `dev` showing old vs new `.dvc` hash
- [ ] Old version recoverable (this is 15 % of the grade)
- [ ] Author **Uzair**, reviewer **Saad**

## 7.5 · Resolve a real conflict

Deliberately:

1. **Saad** changes line `train.max_depth: 6` → `10` in `params.yaml`, opens a PR into `dev`,
   gets reviewed and **merged**.
2. **Uzair**, on a branch created *before* that merge, changes the **same line** to `8`, opens a PR.
3. Uzair updates:

```bash
git fetch && git rebase origin/dev
# CONFLICT in params.yaml → resolve by hand, keeping a sensible value
git add params.yaml && git rebase --continue
```

- [ ] Conflict reproduced and resolved **by rebase** (not by a merge commit, ideally)
- [ ] Resolution **documented in the PR description** (what conflicted, what we kept, why)
- [ ] Link this PR in REPORT.md → *"conflict-resolution PR"*

## 7.6 · Experiment drift (abandoned branch)

- [ ] Keep **at least one** `exp/` branch that is **never merged**
- [ ] Explain in REPORT.md why it was abandoned
      (e.g. *`exp/uzair-lr-baseline`: logistic regression under-performed RandomForest and would
      have required a preprocessing rewrite — not worth porting, so the branch was left unmerged
      and deleted after the report.*)
- [ ] Never let it drift forever: `git fetch && git rebase origin/dev` before quoting it

## PR template — create now

`.github/pull_request_template.md`:

```markdown
## What changed and why

## Metrics (before → after)

## Review checklist
- [ ] No data leakage (no target or future information in features)
- [ ] Splits are fixed; preprocessing fit on training data only
- [ ] No hardcoded paths; runs on a teammate's machine
- [ ] Seeds set for shuffling, initialisation and sampling
- [ ] Metric computed the way the team reports it
- [ ] dvc push done before git push (if data or models changed)
- [ ] Notebook restarted and run top to bottom (if notebooks changed)
- [ ] Style and naming (linter passes)
```

- [ ] File committed to `dev` (put it in the M03 PR or a tiny `docs:` PR)

## Checkpoint (evidence for REPORT.md)

- [ ] PR list: Uzair and Saad each appear as **author** and **reviewer**
- [ ] At least one review shows **"Changes requested"**
- [ ] Links to: data-update PR, conflict-resolution PR, one changes-requested review, abandoned
      `exp/` branch
- [ ] `dvc exp show` table captured for REPORT.md
