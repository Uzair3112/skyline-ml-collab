# Module 01 · Team and repository setup

**Phase 1** · Owner: **Uzair** · Rubric: *Branching & protection (15)* + *Repo hygiene (10)*
**Checkpoint:** all members can push a branch to the repository.

## Objective

Stand up `skyline-ml-collab` on GitHub with both members as writers, the instructor as viewer,
correct local git identity, and the three long-lived branches ready for Phase 2.

## Tasks

### 1. Confirm team name and dataset with the instructor

- [ ] Team name **`skyline`**, repo **`skyline-ml-collab`**
- [ ] Tell the instructor we chose **Airline Passenger Satisfaction** (not on the PDF's list, but it
      is small, tabular and < ~50 MB) and get approval

### 2. Create the repository (Uzair)

- [ ] GitHub → **New repository → `skyline-ml-collab`**, visibility **public**
      (branch protection/rulesets are reliably free on public repos; private repos need Pro)
- [ ] **Do not** initialise with README/.gitignore — our local history is the source of truth
- [ ] Add collaborators: **Saad → Write**, **instructor → Read**
- [ ] Record the remote URL: `https://github.com/<owner>/skyline-ml-collab.git`

### 3. Rename the local folder (optional, recommended)

Current folder `ml-git-collaboration` matches nothing. Rename so local path, GitHub repo and
project name agree. **Do it before Phase 2** — the venv bakes the old path into `bin/activate`, so
re-sync afterwards.

```bash
cd /home/kali/7th_Semester/mlops/assignment-01
mv ml-git-collaboration skyline-ml-collab
cd skyline-ml-collab
uv sync                      # rebuild .venv against the new path
```

Then update `pyproject.toml`: `name = "skyline-ml-collab"` and the `[project.scripts]` key to match
the package directory under `src/`. *(If we skip the rename, just still fix the project name.)*

### 4. Every member: clone and set identity

```bash
git clone https://github.com/<owner>/skyline-ml-collab.git
cd skyline-ml-collab
git config user.name  "Uzair Tariq"     # Saad uses his own
git config user.email "<your-email>"
```

- [ ] Uzair identity set **and verified** with `git config user.name`
- [ ] Saad identity set **and verified**

> Identity is set **per clone** (`--local`), not globally — Saad must run it in his own clone.

### 5. Fix the branch name (currently `master`, zero commits)

The prepared local repo has **no commits** and sits on `master`. Phase 2 must land on `main`.

```bash
git branch -m main
```

### 6. Assign roles (write them into README.md / CONTRIBUTING.md)

| Role | Uzair | Saad |
|------|:-----:|:----:|
| Data owner — DVC, data checks, dataset updates | ✅ | |
| Model owner — pipeline, configs, experiments | | ✅ |
| Platform owner — pre-commit, environment, releases | ✅ | |
| Platform owner — CI, branch protection | | ✅ |

### 7. Push a branch (the actual checkpoint)

```bash
git switch -c chore/bootstrap
# touch any file, commit, push
git push -u origin chore/bootstrap
```

- [ ] **Uzair** pushed a branch
- [ ] **Saad** pushed a branch (from his clone)
- [ ] Both branches visible on GitHub

> Note: `main`/`staging`/`dev` do not exist yet — they are created in Module 02. This checkpoint
> only proves both members can push *a* branch.

## Checkpoint (evidence for REPORT.md)

- [ ] Screenshot: repo `skyline-ml-collab` with Saad + instructor as collaborators
- [ ] `git log --format='%an %ae'` shows **both** authors

## Pitfalls

- Committing as the wrong person (shared laptop) → history misattributes work; marks get adjusted.
- Creating the repo *with* a README on GitHub → divergent histories on first push.
- Making the repo private then discovering branch protection is unavailable.
