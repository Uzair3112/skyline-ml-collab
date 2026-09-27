# Module 04 · Version the data with DVC

**Phase 4** · Owner: **Uzair** (Data owner), **Saad** (reviewer) · Rubric: *DVC (15)*, *PRs (20)*
**Branch:** `data/initial-dataset` → PR → `dev`
**Checkpoint:** the CSV is **not** in Git history — only its `.dvc` pointer is.

## Objective

Put `train.csv` / `test.csv` under DVC with a **shared** remote (DagsHub) so any teammate can
`dvc pull` and get byte-identical data.

## DVC remote decision: DagsHub

```bash
uv add "dvc[dagshub]"
dvc dagshub-setup        # configures dagshub://<owner>/skyline-ml-collab/data, token in .dvc/config.local
```

`dvc dagshub-setup` writes the auth token into **`.dvc/config.local`** (git-ignored) — never
`.dvc/config`. Verify with `git status`: `config.local` must not appear as staged.

Manual fallback if the subcommand is unavailable:

```bash
dvc remote add -d storage dagshub://<owner>/skyline-ml-collab/data
dvc remote modify --local storage auth_type dagshub
dvc remote modify --local storage user <dagshub-username>
dvc remote modify --local storage password <token>
```

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

- [ ] `data/raw/train.csv` and `data/raw/test.csv` present
- [ ] Confirm `.gitignore` ignores `data/` (Module 02) — otherwise step 4 would stage the CSV

### 3. Initialise DVC and track

```bash
dvc init
dvc add data/raw/train.csv data/raw/test.csv
```

### 4. Configure the remote, push, commit

```bash
dvc remote add -d storage dagshub://<owner>/skyline-ml-collab/data   # if not set by setup
dvc push                                   # ALWAYS before git push
git add data/raw/*.csv.dvc data/.gitignore .dvc/config .dvcignore
git commit -m "data: track raw airline satisfaction dataset with DVC"
git push -u origin data/initial-dataset
```

> ⚠️ **Never** `git add data/raw/train.csv`. If it gets staged: `git restore --staged` it and
> re-run the commit. If it was ever **committed**, history must be rewritten with `git filter-repo`
> — a follow-up commit does not remove it.

- [ ] `git show --stat HEAD` contains only `*.csv.dvc`, `data/.gitignore`, `.dvc/*`
- [ ] `git log --all -- '*.csv'` returns **nothing**
- [ ] `dvc push` ran **before** `git push`

### 5. Open the PR

- [ ] Title: `data: track initial dataset with DVC` → base **`dev`**
- [ ] Author: **Uzair**, Reviewer: **Saad**
- [ ] PR description includes the `.dvc` file hashes and the DVC remote name

### 6. Reviewer verification (Saad — this is the real test)

```bash
git clone https://github.com/<owner>/skyline-ml-collab.git /tmp/review-dvc
cd /tmp/review-dvc && git switch data/initial-dataset
uv sync
dvc pull
ls -la data/raw/            # both CSVs present
md5sum data/raw/*.csv       # compare with the hashes in the PR
```

- [ ] Saad confirms the data arrives
- [ ] Squash-merge into `dev`, delete `data/initial-dataset`

## Checkpoint (evidence for REPORT.md)

- [ ] `git rev-list --objects --all | grep -c train.csv` → **0**
- [ ] `cat data/raw/train.csv.dvc` shows `md5` / `size` / `nfiles`
- [ ] 📸 screenshot of `dvc push` output + reviewer's `dvc pull`
- [ ] Link to this PR in REPORT.md ("data-versioning PR")

## Pitfalls

- **Broken pointers:** `git push` without `dvc push` → teammates' `dvc pull` fails.
- Credentials in `.dvc/config` (committed) instead of `config.local` / env vars.
- DagsHub token committed → rotate it immediately and treat as a secret leak (M03 guard).
- Using a **local** DVC remote (`dvc remote add -d storage /path`) → Saad can't pull. Not allowed.
