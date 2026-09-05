# 42piratas

The GitHub profile repository for `@42piratas` — its `README.md` is what renders on the profile
page. There is no application here. The rest of the repository is `safety.pig` (ASCII art, no
function), the shared `.claude/` hook set, `.pi/` settings, and the LGTM gate caller.

## How work flows

**The integration branch is `master`, not `main`.** Branch, work from a worktree under
`.worktrees/`, open a PR against `master`. The LGTM gate runs on every PR. The `.claude/` CLU
guards enforce worktree-only writes and refuse a self-merge, but only while a CLU run is active.

`master` is **not** branch-protected and the gate is **not** a required check — see Key files.

## Crew

The roles this project is worked by, and what each one needs. **No personas live here** — an agent
arrives already knowing who it is, and reads this project to learn the project.

| Role | What this project needs from it |
|------|---------------------------------|
| Content | The README is public first-person copy. The operator validates any wording change before it ships |
| Sysadmin | Branch protection on `master`, and making the LGTM gate a required check rather than advisory |

No engineer, architect, reviewer or data role is in use: there is nothing built here to review.

**After any context loss, re-read your anchor under `~/.agent-anchors/42piratas/`** (canon §17).
None exists yet — no persona has held a session in this repository.

## Key files

- `README.md` — the profile copy; the only user-facing artifact
- `.github/workflows/lgtm.yml` — the gate caller. Wired and passing; still advisory, because `master` carries no branch protection and so no required check
- `MEMO-CODEX-URGENT.md` — untracked. Its gate item is done; its branch-protection item is still open
- `.claude/`, `.pi/` — the fleet hook set and settings
