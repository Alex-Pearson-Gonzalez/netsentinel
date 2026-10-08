# NetSentinel starter kit

Claude Code setup and docs templates for the NetSentinel repo. Delete this file once you're set up.

## What's inside

| Path | What it does |
| --- | --- |
| `CLAUDE.md` | Project rules Claude Code loads in every session; it pulls in docs/progress.md |
| `.claude/settings.json` | Shared settings: Explanatory output style; tests and lint run without asking; `git push`, hard resets and `docker compose down` always ask; `.env` is blocked |
| `.claude/skills/` | `/teach`, `/check-my-work` and `/wrap-up` |
| `.claude/agents/reviewer.md` | Read-only reviewer that `/check-my-work` runs in a fresh context |
| `.claude/rules/` | Rules that load only when Claude works in `dags/` or the database code |
| `docs/` | Plan, progress, decisions, data terms, learning log, incident seed list, RIPEstat catalogue |
| `README.md`, `.gitignore`, `.gitattributes`, `.env.example` | Repo basics |

## Set up (about 30 minutes)

1. Install [Git for Windows](https://git-scm.com/downloads/win). Then install Claude Code from PowerShell with `irm https://claude.ai/install.ps1 | iex`, open a new terminal and run `claude --version`.
2. Create `C:\dev\netsentinel` (outside OneDrive) and copy everything from this kit into it, including the hidden `.claude` folder and the dotfiles.
3. Make the first commit and push:
   - `git init -b main`
   - `git add .`
   - `git commit -m "chore: add Claude Code setup and docs templates"`
   - Create an empty GitHub repo called netsentinel, then run `git remote add origin https://github.com/Alex-Pearson-Gonzalez/netsentinel.git` and `git push -u origin main`.
4. Run `claude` in the repo. Run `/memory` to check that CLAUDE.md is loaded, and type `/` to see the three skills.
5. Output style: Explanatory is the project default. Run `/output-style learning` when you want Claude to leave TODO(human) gaps for you, and `/output-style explanatory` to switch back.
6. Permission mode: new sessions start in auto mode. Press Shift+Tab to switch to Manual when you want to approve, and so read, every edit. Use `/plan` before changes that touch several files.
7. First prompt: "Summarise docs/progress.md and propose today's task at the right learning level."

## Privacy

This repo will be public, so docs/plan.md holds only the technical plan. Keep personal, business and career notes in your Claude Project.
