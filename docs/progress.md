# Progress: NetSentinel
Updated: 2026-10-13 · Phase: 0 · Week: 1 (environment and pandas)

## Done this week
- 2026-10-13: Session 1 done. venv on Python 3.14, deps installed (pandas 3.0.6, NumPy 2.5.4, matplotlib 3.11.2). Fixed Windows python.exe alias issue. ADR-010 (Python 3.14) and ADR-011 (venv) logged.

## Done before (week 0, setup)
- Plan review: accepted all ten changes
- GitHub repo set up at C:\Users\alexp\dev\netsentinel, with the starter kit; Claude Code ready
- Permission emails sent to RIPE NCC and RouteViews, logged in sources-and-terms.md
- Project instructions updated
- 2026-10-16: Session 2 done. pyproject.toml (src layout, editable install), ruff and pytest configured, smoke test passing. PostgreSQL 17 in Docker Compose on port 5433, healthy. ADR-015 logged.

## Next three tasks
1. W1: GitHub Actions CI (ruff + pytest on every push), then merge chore/tooling into main
2. W1: load telecom-pipeline tables into pandas and answer five questions
3. W2: ML basics (Phase 0)

## Blockers and waiting on
- RIPE NCC reply (sent 2026-10-10)

## Open questions
- Before v0.1 (W10): trim learning comments in src/ and tests/ with Claude Code; keep only "why" comments. Move useful notes to learning-log.md first. 

## Numbers
- Networks verified: 0/30 · Days of history: 0 · Tests passing: 1