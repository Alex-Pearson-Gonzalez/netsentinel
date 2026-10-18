# Progress: NetSentinel
Updated: 2026-10-18 · Phase: 0 · Week: 1 done → next: Week 2 (ML basics)

## Done this week
- 2026-10-13: Session 1 done. venv on Python 3.14, deps installed (pandas 3.0.6, NumPy 2.5.4, matplotlib 3.11.2). Fixed Windows python.exe alias issue. ADR-010 (Python 3.14) and ADR-011 (venv) logged.
- 2026-10-16: Session 2 done. pyproject.toml (src layout, editable install), ruff and pytest configured, smoke test passing. PostgreSQL 17 in Docker Compose on port 5433, healthy. ADR-015 logged.
- 2026-10-17: Session 3 done. Minimum versions pinned (ruff exact). GitHub Actions CI runs ruff and pytest on every push; first PR merged into main.
- 2026-10-17/18: Session 4. Loaded telecom-pipeline's Postgres (localhost:5433) into pandas via SQLAlchemy + psycopg 3 + python-dotenv (TELECOM_DB_URL in .env). Answered five questions in notebooks/01_telecom_pipeline_pandas.ipynb. New deps added to pyproject.toml. Commit b888143 on feat/telecom-pandas-eda.

## Done before (week 0, setup)
- Plan review: accepted all ten changes
- GitHub repo set up at C:\Users\alexp\dev\netsentinel, with the starter kit; Claude Code ready
- Permission emails sent to RIPE NCC and RouteViews, logged in sources-and-terms.md
- Project instructions updated

## Next three tasks
1. Merge feat/telecom-pandas-eda into main after CI passes
2. W2: ML basics (features vs labels, train/test split, overfitting, precision, recall, F1)
3. W2: one toy scikit-learn model

## Blockers and waiting on
- RIPE NCC reply (sent 2026-10-10)

## Open questions
- Telefónica AS3352 shows ~226 prefixes vs ~8,400 for Orange: what does telecom-pipeline's extract.py count?
- Vodafone AS12430 is flat at 47 prefixes: zero variation makes a z-score divide by zero. Handle in the Phase 3 baseline.
- chore/claude-automations branch unfinished (.github/copilot-instructions.md untracked)

## Numbers
- Networks verified: 0/30 · Days of history: 0 · Tests passing: <run python -m pytest>