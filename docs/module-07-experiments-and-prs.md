# Module 07 · Experiments and pull requests

**Phase 7** · Owner: **both** · Rubric: *PRs & review (20)* + *DVC (15)* + *Reproducible experiments (15)*
**Checkpoint:** the PR list shows every member as both **author and reviewer** ✅, with at least one
**"changes requested"** review ✅ *(Saad on **PR #34**, 2026-09-30 — 4 blocking inline comments,
all fixed in `f15b167` before the merge)*.

> **Status: COMPLETE ✅ (2026-09-30, executed by Uzair dual-roled — Saad offline).**
> PRs: #12 (conflict A) · #13 (conflict B, rebase-resolved) · #14 (data) · #15 (promote) · #16 (close-out).
> Deviations recorded: Saad's 3 experiments run by Uzair on `exp/saad-depth-sweep`; conflict
> choreography both sides by Uzair; promote PR author = Uzair (brief says Saad).
> Evidence: `docs/evidence/module-07-{conflict-rebase,data-version-switch}.txt`, `module-07-exp-show.md`.

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

- [x] Uzair: ≥ 3 experiments — `minus-skis` (logreg), `dural-raja` (test_size 0.3), `flamy-code` (seed 7)
- [x] Saad: ≥ 3 experiments — `fuggy-ices` (depth 4), `straw-froe` (depth 24), `blank-axon` (trees 300) on `exp/saad-depth-sweep`, **run by Uzair** (deviation; Saad to re-own in his clone)
- [x] **Commit before every experiment run** — clean committed baseline; workspace restored between runs so each = baseline + one override
- [x] `dvc exp show` table pasted into the PR description (PR #15) **and** REPORT.md — evidence `module-07-exp-show.md`
- [x] Branches stay short-lived; sequential from `dev` (exp branches retained as artifacts)

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

- [x] PR into `dev` with **metrics before → after** — PR #15 (f1 0.9476 → 0.9562)
- [ ] Author **Saad**, reviewer **Uzair** → **deviation**: Uzair dual-roled; Saad retro-review requested

## 7.3 · Review each other

- [x] Every PR assigned to the **teammate** as reviewer → retro-review requested from `@msaadsbr` in every body, and **formally requested + delivered on PR #34** (older retro-reviews optional)
- [x] Reviewer pastes the checklist (below) as a **PR comment** → checklist embedded in every PR body
- [x] **At least one PR gets "changes requested"** → ✅ **PR #34** (Saad, 4 blocking comments → fixed in `f15b167`)
- [x] Each member **authors ≥ 2 merged PRs** (Saad #3/#10, Uzair 32 through #38) and **reviews ≥ 2** (Saad 3, Uzair 2)
- [ ] Reviewers actually **check out the branch** for any pipeline-changing PR → ⬜ needs Saad's clone; Uzair's per-branch verification (tests + `dvc repro` + `dvc push`) documented in each PR

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

- [x] PR into `dev` showing old vs new `.dvc` hash — PR #14 (`7795cca…` → `389295a…`)
- [x] Old version recoverable — `git checkout 4cc62cf && dvc checkout` demonstrated, transcript in `module-07-data-version-switch.txt`
- [x] Author **Uzair**; reviewer Saad → retro-review requested

> Executed: audit found **0 duplicates / 310 `Arrival Delay` nulls**, so the change was
> *fill nulls at source* (median 0) instead of dedup; string-preserving edit keeps the tab-mangled
> headers byte-identical; metrics unchanged (source fill == pipeline imputer).

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

- [x] Conflict reproduced and resolved **by rebase** (not by a merge commit, ideally) — `git rebase origin/dev` on `fix/conflict-b` → `CONFLICT (content): Merge conflict in params.yaml`, resolved by hand (`git add` + `--continue`), transcript in `module-07-conflict-rebase.txt`
- [x] Resolution **documented in the PR description** (what conflicted, what we kept, why) — PR #13 body: kept **12**, all three candidates run (8: 0.9273 / 10: 0.9398 / **12: 0.9476 f1**)
- [x] Link this PR in REPORT.md → *"conflict-resolution PR"* — §3 M07 + §8 links

## 7.6 · Experiment drift (abandoned branch)

- [x] Keep **at least one** `exp/` branch that is **never merged** — `exp/uzair-model-sweep` (and `exp/saad-depth-sweep`) kept on origin, unmerged
- [x] Explain in REPORT.md why it was abandoned — logreg −0.092 f1 vs RF; other two runs evaluate different test sets, not portable promotion candidates (REPORT §3 M07 §7.6)
- [x] Never let it drift: branches rebased-by-sequential-merge from `dev`, both tips at `2bb2d00`+ before quoting

## PR template — create now

> Canonical copy lives at `.github/pull_request_template.md` (created in the M03 PR #3; the
> embedded duplicate was dropped at M07 close-out — the file + every PR body carry the checklist).

- [x] File committed to `dev` (landed in the M03 PR #3) ✅

## Checkpoint (evidence for REPORT.md)

- [x] PR list: Uzair and Saad each appear as **author** and **reviewer** (Saad: author #3/#10, reviewer #2/#4 + #34)
- [x] At least one review shows **"Changes requested"** → ✅ PR #34 (Saad, 2026-09-30)
- [x] Links to: data-update PR (#14), conflict-resolution PR (#13), changes-requested review (#34), abandoned `exp/` branch (`exp/uzair-model-sweep`)
- [x] `dvc exp show` table captured for REPORT.md → `docs/evidence/module-07-exp-show.md`
