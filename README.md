# NetSentinel

AI-powered monitoring of BGP routing health for large European and US networks.

> Work in progress: Phase 0, October 2026. The first demo (v0.1) is planned for December 2026.

## What it will do

- Collect routing data for about 30 large networks, growing to 150, from public BGP data sources.
- Detect anomalies per network with statistical baselines and ML models, evaluated against real past incidents.
- Investigate high-severity anomalies with an AI agent that writes evidence-based incident reports.
- Answer questions in plain language through an LLM assistant (RAG and text-to-SQL).

## Planned stack

Python · PostgreSQL · SQLAlchemy · Docker · Airflow 3 · pandas · scikit-learn · PyTorch · MLflow · FastAPI · pgvector

## Status

- Current phase and next steps: [docs/progress.md](docs/progress.md)
- Architecture decisions: [docs/decisions.md](docs/decisions.md)
- Data sources, terms and required credits: [docs/sources-and-terms.md](docs/sources-and-terms.md)
