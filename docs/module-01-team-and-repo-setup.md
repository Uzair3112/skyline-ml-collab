# Module 01 · Team and repository setup

**Phase 1** · Owner: **Uzair** · Rubric: *Branching & protection (15)* + *Repo hygiene (10)*
**Checkpoint:** all members can push a branch to the repository.

## Objective

Stand up `skyline-ml-collab` on GitHub with both members as writers, the instructor as viewer,
correct local git identity, and the three long-lived branches ready for Phase 2.

## Tasks

### 1. Confirm team name and dataset with the instructor — ✅ done

- [x] Team name **`skyline`**, repo **`skyline-ml-collab`**
- [x] Tell the instructor we chose **Airline Passenger Satisfaction** (not on the PDF's list, but it
      is small, tabular and < ~50 MB) and get approval

### 2. Create the repository (Uzair) — ✅ done

- [x] GitHub → **New repository → `skyline-ml-collab`**, visibility **public**
      (branch protection/rulesets are reliably free on public repos; private repos need Pro)
- [x] **Do not** initialise with README/.gitignore — our local history is the source of truth
- [x] Add collaborators: **Saad → Write**, **instructor → Read**
- [x] Remote URL: `git@github.com:Uzair3112/skyline-ml-collab.git`

> **Local SSH note:** this machine has two GitHub identities. `~/.ssh/config` maps
> `github-uzair3112` → the repo owner's key, while plain `github.com` authenticates as *Uzair599*.
> `origin` is stored as the canonical URL above, and a **repo-local** rewrite
> (`git config url."git@github-uzair3112:".insteadOf "git@github.com:"`) routes it through the
> correct key. Pushes are authored as **Uzair3112**. Saad's clone needs no such rule.

### 3. Rename the local folder — ✅ done

Current folder `ml-git-collaboration` matches nothing. Rename so local path, GitHub repo and
project name agree. **Do it before Phase 2** — the venv bakes the old path into `bin/activate`, so
re-sync afterwards.

```bash
cd /home/kali/7th_Semester/mlops/assignment-01
mv ml-git-collaboration skyline-ml-collab
cd skyline-ml-collab
uv sync --reinstall            # rebuild .venv AND every console-script shebang
```

Then update `pyproject.toml`: `name = "skyline-ml-collab"` and the `[project.scripts]` key to match
the package directory under `src/`. *(If we skip the rename, just still fix the project name.)*

**Applied:**
- [x] Folder renamed → `assignment-01/skyline-ml-collab`
- [x] `uv sync --reinstall` (a plain `uv sync` leaves `pytest`/`pre-commit` shebangs pointing at the
      old path — **must** be `--reinstall` or a fresh `.venv`)
- [x] `pyproject.toml` → `name = "skyline-ml-collab"`, new description
- [x] removed the broken `[project.scripts] ml-git-collaboration = "ml_git_collaboration:main"`
      (pointed at a module and `main()` that never existed)
- [x] `src/ml_git_collaboration/` → `src/ml_skyline/`, wired up with
      `[tool.uv.build-backend] module-name = "ml_skyline"`
- [x] `uv sync` builds and `import ml_skyline` works

### 4. Every member: clone and set identity

```bash
git clone git@github.com:Uzair3112/skyline-ml-collab.git
cd skyline-ml-collab
git config user.name  "Uzair Tariq"     # Saad uses his own
git config user.email "<your-email>"
```

- [x] Uzair identity set **and verified** with `git config user.name` → `Uzair Tariq`
- [x] **Saad** identity set **and verified** (in his own clone) — `Muhammad Saad Sabir <saadsbr789@gmail.com>`, set with `git config --local` (per-clone, not global)

> Identity is set **per clone** (`--local`), not globally — Saad must run it in his own clone.

### 5. Fix the branch name (currently `master`, zero commits) — ✅ done

The prepared local repo had **no commits** and sat on `master`. Phase 2 must land on `main`.

```bash
git branch -m main
```

- [x] `HEAD` → `refs/heads/main`

### 6. Assign roles (written into `README.md`)

| Role | Uzair | Saad |
|------|:-----:|:----:|
| Data owner — DVC, data checks, dataset updates | ✅ | |
| Model owner — pipeline, configs, experiments | | ✅ |
| Platform owner — pre-commit, environment, releases | ✅ | |
| Platform owner — CI, branch protection | | ✅ |

- [x] Roles table committed in `README.md`

### 7. Push a branch (the actual checkpoint)

```bash
git switch -c chore/bootstrap
# touch any file, commit, push
git push -u origin chore/bootstrap
```

- [x] **Uzair** pushed a branch → `chore/bootstrap` (`6e16d66 docs: add team roles, module plan and progress board`)
- [x] **Saad** pushes a branch (from his clone) — `chore/saad-setup`
- [x] Branch visible on GitHub

> Note: `main`/`staging`/`dev` do not exist on the remote yet — they are created in Module 02. This
> checkpoint only proves both members can push *a* branch.
>
> ⚠️ **Phase 2 housekeeping:** because `chore/bootstrap` was the first branch pushed, GitHub made it
> the **default branch**. In Phase 2: push `main`, then *Settings → Branches → default branch →
> `main`*, and delete **`chore/bootstrap`** and **`chore/saad-setup`** (both are ancestors of `main`).

## Checkpoint (evidence for REPORT.md)

- [x] 📸 Screenshot: *Settings → Collaborators* showing **Muhammad Saad Sabir (`msaadsbr`) · Collaborator** →
      [`docs/evidence/module-01-collaborators.png`](evidence/module-01-collaborators.png)
      (instructor not added — skipped by team decision; graded from the repo alone)
- [x] 📸 Screenshot: `git log --format='%an <%ae>' … | sort -u` showing **both authors** →
      [`docs/evidence/module-01-two-authors.png`](evidence/module-01-two-authors.png)
- [x] `git log --format='%an %ae'` shows **both** authors:
      `Uzair Tariq <uzairtariq.pakistani@gmail.com>` ·
      `Muhammad Saad Sabir <saadsbr789@gmail.com>`
- [x] **Write access proven empirically** — Saad pushed `chore/saad-setup` (`214269f`) himself;
      no API token or screenshot needed to show it

## Module 01 close-out

| Item | Result |
|------|--------|
| Team / repo | `skyline` → `Uzair3112/skyline-ml-collab` (public) |
| Members' SSH identities | Uzair → `Uzair3112` (via repo-local URL rewrite) · Saad → `msaadsbr` |
| Local `main` | `214269f`, 3 commits, **2 authors** ✅ |
| Branches on remote | `chore/bootstrap` (`8fc1ef3`), `chore/saad-setup` (`214269f`) — both to be deleted in Module 02 |
| Outstanding | ✅ none — collaborators + two-author screenshots committed under `docs/evidence/` |
| Next | **Module 02** — scaffold, initial import pushed to `main`, create `staging` + `dev`, branch protection, `CONTRIBUTING.md` |

> `main` is deliberately **not pushed yet**: the PDF says Phase 2 is the only time anyone pushes
> directly to `main`, so all 3 documentation commits go up with the Phase 2 scaffold push.

## Pitfalls

- Committing as the wrong person (shared laptop) → history misattributes work; marks get adjusted.
- Creating the repo *with* a README on GitHub → divergent histories on first push.
- Making the repo private then discovering branch protection is unavailable.
- A member editing files on `main` locally while the other pushes to a `chore/*` branch → divergence;
  always fast-forward `main` onto the teammate's branch first
  (`git fetch && git switch main && git merge --ff-only origin/<branch>`).
