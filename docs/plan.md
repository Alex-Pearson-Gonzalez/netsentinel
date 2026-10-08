# NetSentinel plan

The technical plan. Personal, business and career notes stay in my Claude Project, because this repo is public.

Decisions behind this plan are recorded in [decisions.md](decisions.md). All ten changes from the plan review (6 Oct 2026) and the full chat assistant (ADR-001) were accepted on 8 Oct 2026.

## Summary

An AI-powered monitor for the routing health of the biggest network companies in Europe and the US, including the DACH countries. It collects BGP and routing data, detects anomalies with ML, uses an AI agent to investigate incidents and write reports, and offers an AI chat assistant you can ask about everything in plain language.

## How it works end to end

1. The pipeline collects routing data for the tracked networks and stores it in PostgreSQL:
   - **State data** (for example, which prefixes a network announces) three times a day, after each RIS snapshot at 00:00, 08:00 and 16:00 UTC (ADR-004).
   - **Fast signals** (BGP update activity in 1-minute bins) more often; later in real time with RIS Live.
2. The ML anomaly detector compares new data against each network's normal behaviour and writes anomalies with a severity score to the database. Example: a network suddenly stops announcing 40% of its prefixes. Known events such as mergers are not flagged as anomalies (ADR-007).
3. For high-severity anomalies, the agent investigates on its own: it re-checks live data, queries the database (including neighbouring and related networks), searches documentation and writes an incident report (what, when, severity, likely cause, evidence).
4. Users chat with the assistant, for example "Which networks were most unstable this week?", "Explain yesterday's incident on AS3320" or "What is a BGP prefix withdrawal?". It answers using text-to-SQL, RAG over docs and the agent's reports. It remembers the conversation, shows its sources, suggests follow-up questions and asks when a question is unclear (ADR-001).

## Building blocks

- Data platform: telecom-pipeline, upgraded with Airflow, multiple sources and, later, streaming.
- A, anomaly detector: pandas, scikit-learn, PyTorch, MLflow.
- B, chat assistant: LLM API and Ollama, embeddings, pgvector, RAG, text-to-SQL, multi-turn chat (conversation memory, follow-up suggestions, sources shown, clarifying questions), evals.
- D, agent: tool calling, a custom agent loop, an MCP server.
- Platform: FastAPI, Docker Compose, Streamlit UI, pytest, GitHub Actions CI/CD, AWS.

D is largely B with more tools: text-to-SQL and doc search become agent tools, and live API calls and report writing are added. The chat can also hand hard questions to the agent.

## Data sources rule

- Every stored data point records which source it came from (ADR-008).
- Paid features use only RIS raw data, RIS Live and RouteViews. RIPEstat, Cloudflare Radar, CAIDA and PeeringDB are used only in free or non-commercial parts until written permission is given. Details in [sources-and-terms.md](sources-and-terms.md).

## Network scope

Types tracked: Tier-1 and transit backbones, national incumbents, and big cable and mobile operators.

The watchlist is a list of **organisations**, each with one or more ASNs (ADR-007).

### Starting list (verify in Week 7)

| Group | Organisations (ASNs) |
| --- | --- |
| Transit | Lumen AS3356 · Arelion AS1299 · Cogent AS174 (+ Sprint AS1239) · NTT AS2914 · GTT AS3257 · Zayo AS6461 · Hurricane Electric AS6939 · Telecom Italia Sparkle AS6762 · Orange international AS5511 |
| Germany | Deutsche Telekom AS3320 · Vodafone Germany AS3209 · Telefónica Germany / O2 AS6805 |
| Switzerland | Swisscom AS3303 · Sunrise AS6730 |
| Austria | A1 Telekom Austria AS8447 |
| UK | BT AS2856 · Virgin Media AS5089 |
| Spain | Telefónica Spain AS3352 · Telefónica international AS12956 · MasOrange (Orange Espagne) AS12479 |
| Pan-European | Vodafone group AS1273 · Liberty Global AS6830 · Colt AS8220 |
| US | AT&T AS7018 · Verizon AS701 · Comcast AS7922 · Charter AS20115 (+ Cox AS22773) · T-Mobile US AS21928 |

Candidates: Tata AS6453 and PCCW AS3491.

Notes to verify in Week 7:
- Sunrise AS6730 has been independent of Liberty Global since Nov 2024.
- The sale of Sparkle AS6762 to MEF and Retelit was still pending at the time of the review.

### Known events (not anomalies)

| Date | Event |
| --- | --- |
| Nov 2023 | Colt–Lumen EMEA |
| 15 Nov 2024 | Sunrise spin-off from Liberty Global |
| Feb 2026 | AT&T–Lumen consumer fibre |
| 20 Aug 2026 | Charter–Cox |

### Growth stages

1. Core, about 30 networks: Phases 1–4. Small enough to debug and validate the model by hand.
2. Expansion, about 60–80 networks: after the scale-up phase.
3. Full, 100–150 networks: before launch. Adds France, Italy, the Netherlands, the Nordics and second-tier operators.

### Design rules

- Build for 150 from day one, even while tracking 30.
- The watchlist lives in the database or a config file, never in code. No code assumes a fixed number of networks.
- Select the "biggest" networks with data, not by hand: CAIDA AS Rank (customer cone size), APNIC per-country user estimates, and a rule such as "top N per country plus the top 15 transit networks globally". Growing the list is a parameter change.

## How I work

- Each task has a learning level: either I write the code and Claude reviews it, or Claude helps more.
- `docs/` is the shared memory between my Claude Project and Claude Code: this plan, decisions, progress, the incident catalogue and the learning log.

## Phases

Each phase ends with something working and presentable.

### Schedule (10–12 hours a week)

| Week | Dates | Focus |
| --- | --- | --- |
| W1 | 12–18 Oct | Phase 0: environment and pandas |
| W2 | 19–25 Oct | Phase 0: ML basics |
| W3 | 26 Oct–1 Nov | Phase 0: LLM basics |
| W4 | 2–8 Nov | Phase 1: RIPEstat signals |
| W5 | 9–15 Nov | Phase 1: schema and migrations |
| W6 | 16–22 Nov | Phase 1: adapters and ingestion |
| W7 | 23–29 Nov | Phase 1: watchlist verification |
| W8 | 30 Nov–6 Dec | Phase 1: backfill and data quality |
| W9 | 7–13 Dec | Phase 1: Airflow 3 |
| W10 | 14–20 Dec | Phase 1: v0.1 slice and write-up |

### Phase 0: foundations

- ML basics: training, features vs labels, overfitting, train/test split, metrics (precision, recall, F1).
- pandas and NumPy fluency.
- LLM basics: tokens, context windows, temperature, embeddings, calling an LLM API from Python.
- Mini-exercises: one toy scikit-learn model and one LLM API call.

### Phase 1: data expansion (ends with v0.1)

- Explore the RIPEstat API to choose signals: announced prefixes over time, BGP update counts, routing visibility and more.
- Choose signals per network type (ADR-005):
  - transit networks: transited prefixes, number of neighbours, update rates, leaks
  - incumbents and cable/mobile operators: originated prefixes as a main signal
- Build a source adapter layer: each provider is a plug-in that converts its data into a normalised, country-agnostic schema, and records the source of every data point. RIPEstat is the first adapter.
- Redesign the database for time series, with timestamped metrics per ASN, using native PostgreSQL partitioning by time (ADR-003).
- Store organisations: start with an organisation column on the ASN table (ADR-007).
- Collection schedule: state data three times a day, fast signals from `bgp-update-activity` (ADR-004).
- Backfill several months of history.
- Start the incident catalogue in [incident-catalogue.md](incident-catalogue.md), seeded with the Level(3) outage (30 Aug 2020, 10:03–14:30 UTC) and the Verizon route leak (24 Jun 2019, 10:34–12:39 UTC), and fetch the data around each incident (ADR-006).
- Orchestrate collection with Airflow.
- Build the data-driven watchlist selection and verify the starting list.
- Email RIPE NCC and RouteViews about commercial use.
- **v0.1 (by 20 Dec 2026):** a small version that works from start to finish on the core watchlist, plus a short write-up (ADR-002).

### Phase 2: exploration and features

- EDA in Jupyter: plots, distributions, daily and weekly patterns.
- Grow the incident catalogue with real past incidents found in the data.
- Feature engineering: rolling averages, rate of change, deviation from each network's own baseline.

### Customer discovery (after Phase 2)

- Talk to 5–10 potential users (smaller ISPs, hosting companies, businesses that depend on the big carriers) about how they monitor routing today and whether explained "upstream provider" alerts would be worth paying for.

### Phase 3: anomaly detection models

- Baseline first: a statistical rule such as a z-score. Every ML model must beat it.
- Classic ML: Isolation Forest and forecasting-based detection.
- Deep learning: a small PyTorch autoencoder.
- Per-network baselines: huge networks announce thousands of prefixes, so a 2% change can matter.
- Graph analysis with NetworkX of the relationships between tracked networks, to detect cascading events and route leaks spreading from one network to others.
- Evaluation: a labelled test set from the incident catalogue, synthetic anomaly injection and a numeric comparison of all models. Known events must not be flagged.
- Experiment tracking with MLflow.

### Phase 4: serving and MLOps

- Package the best model and run it automatically in the Airflow pipeline.
- FastAPI endpoints such as `/anomalies` and `/asn/{id}/health`.
- Model versioning with the MLflow registry.
- pytest tests and GitHub Actions CI on every push.

### Phase 5: chat assistant, part 1 (RAG)

- Documents: RIPE docs, key BGP RFCs and the project's own docs.
- Chunking and embeddings stored in pgvector inside Postgres.
- Retrieval → prompt → answer with citations.
- Ollama (free, local) for development and a hosted API for the demo, switchable with one config change.

### Phase 6: chat assistant, part 2 (text-to-SQL, chat features and evals)

- The LLM writes SQL from the schema, the system runs it, and the LLM explains the result.
- Safety: a read-only database user, query validation, row limits.
- A router that decides whether a question needs SQL, docs or both.
- A Streamlit chat UI with four chat features (ADR-001):
  1. conversation memory within a chat ("And did it affect BT?" works)
  2. 1–3 follow-up suggestions after each answer
  3. sources shown: database, document or incident report
  4. clarifying questions when a question is ambiguous (e.g. "Telefónica")
- Keep long chats inside the context window, e.g. by summarising older messages.
- Evals: 50+ test questions with expected answers, plus a few multi-turn test conversations, automatic accuracy scoring and a comparison of models and prompts.

### Phase 7: the agent

- Build the agent loop by hand first, without frameworks.
- Tools: `query_database`, `search_docs`, `fetch_live_ripestat` (and other sources), `get_neighbor_networks`, `write_incident_report`.
- Triggered automatically by high-severity anomalies.
- The chat can hand hard questions to the agent ("Investigate this for me").
- Cross-network investigation, for example "Lumen had an incident; which tracked European networks were affected downstream?"
- Guardrails: a step limit, a cost limit and a log of every decision.
- Safety (ADR-009): registry text is untrusted data, never instructions; a human reviews anything public that names a company.
- Evaluate it on the incident catalogue.
- Optional: rebuild it with an agent framework and compare, and expose the tools as an MCP server.

### Scale-up phase (after Phase 7)

- Add RouteViews as a second source. Its collectors sit in different places from RIPE's, which helps for US networks.
- Add RIS Live real-time streaming, filtered to the watchlist.
- Process MRT archive files with BGPKIT or pybgpstream.
- Revisit TimescaleDB if partitioning is no longer enough (ADR-003).
- Add an optional message queue (Kafka or Redis Streams) between ingestion and the detector.
- Use agreement between sources to make anomalies more trustworthy.
- Expand the watchlist to about 60–80 networks.

### Phase 8: cloud, observability and product features

- Docker Compose locally, then AWS.
- Monitoring: model drift, LLM cost and latency, agent success rate.
- Product features: user accounts and multi-tenancy, saved chats per user account, per-customer watchlists, email and Telegram alerts, Stripe in test mode (currencies and EU VAT), reports and chat answers in several languages (ES, EN, CA, DE), RDAP across all five regional internet registries, GDPR basics (EU hosting, privacy policy), and UTC storage with local display.

### Phase 9: portfolio polish

- README with an architecture diagram, results tables and limitations.
- Publish the evaluation results (detector, assistant and agent), so the quality can be checked.
- Demo video: anomaly → agent investigates → the assistant answers questions.
- A write-up or LinkedIn post per phase, with headline metrics.

### Phase 10: launch

- Open-source release, a landing page and the public dashboard. Public incident summaries that name a company are reviewed by a human first.
- Posts in networking communities and on LinkedIn.
- A free beta with a few customers.
- Expand to 100–150 networks.
