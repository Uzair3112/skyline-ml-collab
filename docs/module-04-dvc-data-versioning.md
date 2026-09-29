# Module 04 · Version the data with DVC

**Phase 4** · Owner: **Uzair** (Data owner), **Saad** (reviewer) · Rubric: *DVC (15)*, *PRs (20)*
**Branch:** `data/initial-dataset` → PR → `dev`
**Checkpoint:** the CSV is **not** in Git history — only its `.dvc` pointer is.

## Objective

Put `train.csv` / `test.csv` under DVC with a **shared** remote (DagsHub) so any teammate can
`dvc pull` and get byte-identical data.

## DVC remote decision: DagsHub (HTTPS — the recipe that actually works)

> **Verified against DVC 3.67.1.** Two commonly-cited shortcuts **do not work**:
> `dvc dagshub-setup` is not a real subcommand, and the `dagshub://` URL scheme is rejected
> (`Unsupported URL type 'dagshub://...'`). `dvc[dagshub]` is not a real extra either.
> Use the plain **HTTPS** remote + HTTP basic auth below — this is what the repo actually uses.

```bash
uv add dvc
dvc remote add -d storage https://dagshub.com/<owner>/skyline-ml-collab.dvc
dvc remote modify --local storage user <dagshub-username>     # -> .dvc/config.local
dvc remote modify --local storage password <dagshub-token>    # -> .dvc/config.local
```

Auth (`user`/`password`) is written into **`.dvc/config.local`** (git-ignored) — never
`.dvc/config`, which must contain only the URL. Verify with `git status`: `config.local` must
never appear as staged. First `dvc push` prompts once to trust the DagsHub host key (`yes`).

### DagsHub git mirror (why the web UI was empty)

DagsHub's UI renders DVC-tracked datasets by parsing the **`.dvc` pointer files from git** — the
pushed storage objects alone are invisible on the website. The DagsHub repo started empty (we only
used it as DVC storage), so we mirrored the code:

```bash
git remote add dagshub https://dagshub.com/<owner>/skyline-ml-collab.git   # creds via git credential store, never in the URL
git push dagshub dev                                                       # became DagsHub's default branch
git push dagshub main
git push dagshub refs/remotes/origin/staging:refs/heads/staging            # no local staging branch
```

- DagsHub default branch = **`dev`** (first push on an empty repo) — pointer files and the rendered
  dataset are visible on the homepage until the Module 09 release puts them on `main`.
- **Sync rule:** GitHub `origin` is the source of truth; after every merge into `dev` (and the M09
  release), also run `git push dagshub dev` (etc.) or the DagsHub page goes stale.

## Tasks

### 1. Branch

```bash
git switch dev && git pull
git switch -c data/initial-dataset
```

### 2. Fetch the data into `data/raw/`

```bash
git clone https://github.com/vrunm/Airline_Passenger_Satisfaction /tmp/starter
cp /tmp/starter/train.csv /tmp/starter/test.csv data/raw/
```

- [x] `data/raw/train.csv` and `data/raw/test.csv` present
- [x] Confirm `.gitignore` ignores `data/` (Module 02) — otherwise step 4 would stage the CSV

### 3. Initialise DVC and track

```bash
dvc init
dvc add data/raw/train.csv data/raw/test.csv
```

### 4. Configure the remote, push, commit

```bash
dvc remote add -d storage https://dagshub.com/<owner>/skyline-ml-collab.dvc   # if not set yet
dvc push                                   # ALWAYS before git push
git add data/raw/*.csv.dvc .dvc/.gitignore .dvc/config .dvcignore
git commit -m "data: track raw airline satisfaction dataset with DVC"
git push -u origin data/initial-dataset
```

> ⚠️ **Never** `git add data/raw/train.csv`. If it gets staged: `git restore --staged` it and
> re-run the commit. If it was ever **committed**, history must be rewritten with `git filter-repo`
> — a follow-up commit does not remove it.

- [x] `git show --stat HEAD` contains only `*.csv.dvc`, `.dvc/*`
- [x] `git log --all -- '*.csv'` returns **nothing** (verified: `git rev-list --objects --all` → 0 `*.csv` objects)
- [x] `dvc push` ran **before** `git push` ("2 files pushed", then `dvc status` → up to date)

### 5. Open the PR — **PR #7** ✅ merged

- [x] Title: `data: track initial dataset with DVC` → base **`dev`**
- [x] Author: **Uzair**, Reviewer: **Saad**
- [x] PR description includes the `.dvc` file hashes, sizes and the DVC remote URL
- [x] Squash-merged into `dev` as **`616a8fd`**; head branch deleted; protection re-verified
      (`approvals=1 · enforce_admins=true · no force-push · no deletions` on all 3 branches)

### 6. Reviewer verification (Saad — this is the real test)

Clean-clone recipe (the `.dvc` pointers are tracked, so no branch switch is needed):

```bash
git clone https://github.com/<owner>/skyline-ml-collab.git /tmp/review-dvc
cd /tmp/review-dvc
# copy .dvc/config.local (auth) from the author — it is git-ignored, so it never travels with the repo
dvc status && dvc pull
ls -la data/raw/            # both CSVs present
md5sum data/raw/*.csv       # compare with the hashes in the PR
```

- [x] **Already proven** with a fresh GitHub clone on Uzair's machine:
  `dvc pull` → *2 files added*; md5 of pointer = clone = local for both files
  (evidence: `docs/evidence/module-04-dvc-pull-verification.txt`)
- [ ] Saad re-runs the same 4 commands in his own clone and confirms the hashes
      — ⬜ **pending Saad** (external, same as his `pre-commit install`); does not block the
      module: the identical check already passed on a clean clone (row above).

## Checkpoint (evidence for REPORT.md)

- [x] `git rev-list --objects --all | grep -c '\.csv$'` → **0**
- [x] `cat data/raw/train.csv.dvc` shows `md5` / `size` (`7795cca…`, 14 873 245 B; test: `e70c499…`, 3 037 688 B)
- [x] Transcript of `dvc push` + fresh-clone `dvc pull` + three-way md5 match:
      `docs/evidence/module-04-dvc-pull-verification.txt`
- [x] Link to this PR (#7) in REPORT.md ("data-versioning PR")

## Pitfalls

- **Broken pointers:** `git push` without `dvc push` → teammates' `dvc pull` fails.
- Credentials in `.dvc/config` (committed) instead of `config.local` / env vars.
- DagsHub token committed → rotate it immediately and treat as a secret leak (M03 guard).
- Using a **local** DVC remote (`dvc remote add -d storage /path`) → Saad can't pull. Not allowed.
