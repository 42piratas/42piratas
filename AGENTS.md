# 42piratas

The GitHub profile repository for `@42piratas` — its `README.md` is what renders on the profile
page. There is no application here. Alongside the README the repository holds `safety.pig` (ASCII
art, no function), the shared `.claude/` hook set, and the LGTM gate caller.

**The integration branch is `master`, not `main`** — the only repository in the fleet where that is
true. Branch and open a PR as everywhere else.

## Crew

The roles this project is worked by, and what each one needs. **No personas live here** — an agent
arrives already knowing who it is, and reads this project to learn the project.

| Role | What this project needs from it |
|------|---------------------------------|
| Content | The README is public first-person copy. The operator validates any wording change before it ships |
| Sysadmin | Branch protection on `master`, and making LGTM a required check rather than advisory |

No engineer, architect, reviewer or data role is in use: there is nothing built here to review.

**After any context loss, re-read your anchor under `~/.agent-anchors/42piratas/`** (canon §17).
None exists yet — no persona has held a session in this repository.

## Key files

- `README.md` — the profile copy; the only user-facing artifact
- `MEMO-CODEX-URGENT.md` — untracked and still open: wire the LGTM gate and make it required on `master`
- `.github/workflows/lgtm.yml` — the gate caller
- `.claude/` — the fleet hook set and settings
