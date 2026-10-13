# Progress: NetSentinel
Updated: 2026-10-13 · Phase: 0 · Week: 1 (environment and pandas)

## Done this week
- 2026-10-13: Session 1 done. venv on Python 3.14, deps installed (pandas 3.0.6, NumPy 2.5.4, matplotlib 3.11.2). Fixed Windows python.exe alias issue. ADR-011 (venv) and ADR-012 (Python 3.14) logged.

## Done before (week 0, setup)
- Plan review: accepted all ten changes
- GitHub repo set up at C:\Users\alexp\dev\netsentinel, with the starter kit; Claude Code ready
- Permission emails sent to RIPE NCC and RouteViews, logged in sources-and-terms.md
- Project instructions updated

## Next three tasks
1. W1: pyproject.toml, ruff, pytest, Postgres in Docker Compose
2. W1: GitHub Actions CI (ruff + pytest on every push)
3. W1: load telecom-pipeline tables into pandas and answer five questions

## Blockers and waiting on
- RIPE NCC reply (sent 2026-10-10)
- RouteViews: replied 2026-10-12 pointing to its published commercial terms; I answered, waiting for their response

## Open questions
- Keep requirements.txt, or move dependencies into pyproject.toml? (decide in Session 2)

## Numbers
- Networks verified: 0/30 · Days of history: 0 · Tests passing: 0