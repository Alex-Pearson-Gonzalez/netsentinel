# NetSentinel plan

The technical plan. Personal, business and career notes stay in my Claude Project, because this repo is public.

## Proposed changes from the plan review (6 Oct 2026)

Tick each change I accept, write an ADR for it in docs/decisions.md, then update the plan below. The reasoning is in the plan review doc.

- [ ] Add a v0.1 slice at the end of Phase 1 (20 Dec 2026) and move the scale-up phase after Phase 7.
- [ ] Use native PostgreSQL partitioning now and decide on TimescaleDB later, since Amazon RDS doesn't offer it.
- [ ] Poll RIPEstat state data three times a day; take fast signals from bgp-update-activity, and later RIS Live.
- [ ] Measure transit networks by transited prefixes, neighbours, update rates and leaks, not originated prefixes.
- [ ] Keep an incident catalogue from the start, seeded with the Level(3) 2020 outage and the Verizon 2019 leak.
- [ ] Track organisations rather than single ASNs, and log mergers as known events.
- [ ] Build paid features only on RIS raw data, RIS Live and RouteViews.
- [ ] Treat Cloudflare Radar as a competitor; compete on explanation quality and published evaluation.
- [ ] Treat registry text as untrusted input, and review anything that names a company before it goes public.
- [ ] Use Claude at a set learning level per task, with docs/ as the shared memory.

## Summary

An AI-powered monitor for the routing health of the biggest network companies in Europe and the US, including the DACH countries. It collects BGP and routing data, detects anomalies with ML, uses an AI agent to investigate incidents and write reports, and offers an LLM assistant you can ask about everything in plain language.

## How it works end to end

1. Every hour (later in real time), the pipeline collects routing data for the tracked networks and stores it in PostgreSQL.
2. The ML anomaly detector compares new data against each network's normal behaviour and writes anomalies with a severity score to the database. Example: a network suddenly stops announcing 40% of its prefixes.
3. For high-severity anomalies, the agent investigates on its own: it re-checks live data, queries the database (including neighbouring and related networks), searches documentation and writes an incident report (what, when, severity, likely cause, evidence).
4. Users chat with the assistant, for example "Which networks were most unstable this week?", "Explain yesterday's incident on AS3320" or "What is a BGP prefix withdrawal?". It answers using text-to-SQL, RAG over docs and the agent's reports.

## Building blocks

- Data platform: telecom-pipeline, upgraded with Airflow, multiple sources and streaming.
- A, anomaly detector: pandas, scikit-learn, PyTorch, MLflow.
- B, assistant: LLM API and Ollama, embeddings, pgvector, RAG, text-to-SQL, evals.
- D, agent: tool calling, a custom agent loop, an MCP server.
- Platform: FastAPI, Docker Compose, Streamlit UI, pytest, GitHub Actions CI/CD, AWS.

D is largely B with more tools: text-to-SQL and doc search become agent tools, and live API calls and report writing are added.

## Network scope

Types tracked: Tier-1 and transit backbones, national incumbents, and big cable and mobile operators.

### Starting list (verify in Week 7)

| Group | Networks |
| --- | --- |
| Transit | Lumen AS3356 · Arelion AS1299 · Cogent AS174 · NTT AS2914 · GTT AS3257 · Zayo AS6461 · Hurricane Electric AS6939 · Telecom Italia Sparkle AS6762 · Orange international AS5511 |
| Germany | Deutsche Telekom AS3320 · Vodafone Germany AS3209 · Telefónica Germany / O2 AS6805 |
| Switzerland | Swisscom AS3303 · Sunrise AS6730 |
| Austria | A1 Telekom Austria AS8447 |
| UK | BT AS2856 |
| Spain | Telefónica Spain AS3352 · Telefónica international AS12956 |
| Pan-European | Vodafone group AS1273 · Liberty Global AS6830 |
| US | AT&T AS7018 · Verizon AS701 · Comcast AS7922 · Charter AS20115 · T-Mobile US AS21928 |

Candidates from the review: MasOrange (Orange Espagne) AS12479, Virgin Media AS5089, Colt AS8220, Tata AS6453 and PCCW AS3491. Sibling ASNs to model under their organisation: Sprint AS1239 under Cogent, and Cox AS22773 under Charter.

### Growth stages

1. Core, about 30 networks: Phases 1–4. Small enough to debug and validate the model by hand.
2. Expansion, about 60–80 networks: after the scale-up phase.
3. Full, 100–150 networks: before launch. Adds France, Italy, the Netherlands, the Nordics and second-tier operators.

### Design rules

- Build for 150 from day one, even while tracking 30.
- The watchlist lives in the database or a config file, never in code. No code assumes a fixed number of networks.
- Select the "biggest" networks with data, not by hand: CAIDA AS Rank (customer cone size), APNIC per-country user estimates, and a rule such as "top N per country plus the top 15 transit networks globally". Growing the list is a parameter change.

## Phases

Each phase ends with something working and presentable.

### Phase 0: foundations

- ML basics: training, features vs labels, overfitting, train/test split, metrics (precision, recall, F1).
- pandas and NumPy fluency.
- LLM basics: tokens, context windows, temperature, embeddings, calling an LLM API from Python.
- Mini-exercises: one toy scikit-learn model and one LLM API call.

### Phase 1: data expansion

- Explore the RIPEstat API to choose signals: announced prefixes over time, BGP update counts, routing visibility and more.
- Build a source adapter layer: each provider is a plug-in that converts its data into a normalised, country-agnostic schema. RIPEstat is the first adapter.
- Redesign the database for time series, with timestamped metrics per ASN.
- Backfill several months of history.
- Orchestrate collection with Airflow.
- Build the data-driven watchlist selection and verify the starting list.
- Email RIPE NCC and RouteViews about commercial use.

### Phase 2: exploration and features

- EDA in Jupyter: plots, distributions, daily and weekly patterns.
- Find real past incidents in the data.
- Feature engineering: rolling averages, rate of change, deviation from each network's own baseline.

### Customer discovery (after Phase 2)

- Talk to 5–10 potential users (smaller ISPs, hosting companies, businesses that depend on the big carriers) about how they monitor routing today and whether explained "upstream provider" alerts would be worth paying for.

### Phase 3: anomaly detection models

- Baseline first: a statistical rule such as a z-score. Every ML model must beat it.
- Classic ML: Isolation Forest and forecasting-based detection.
- Deep learning: a small PyTorch autoencoder.
- Per-network baselines: huge networks announce thousands of prefixes, so a 2% change can matter.
- Graph analysis with NetworkX of the relationships between tracked networks, to detect cascading events and route leaks spreading from one network to others.
- Evaluation: a labelled test set from real incidents, synthetic anomaly injection and a numeric comparison of all models.
- Experiment tracking with MLflow.

### Phase 4: serving and MLOps

- Package the best model and run it automatically in the Airflow pipeline.
- FastAPI endpoints such as `/anomalies` and `/asn/{id}/health`.
- Model versioning with the MLflow registry.
- pytest tests and GitHub Actions CI on every push.

### Scale-up phase (after Phase 4)

- Add RouteViews as a second source. Its collectors sit in different places from RIPE's, which helps for US networks.
- Add RIS Live real-time streaming, filtered to the watchlist.
- Process MRT archive files with BGPKIT or pybgpstream.
- Move to TimescaleDB (still PostgreSQL), with data partitioning.
- Add an optional message queue (Kafka or Redis Streams) between ingestion and the detector.
- Use agreement between sources to make anomalies more trustworthy.
- Expand the watchlist to about 60–80 networks.

### Phase 5: LLM assistant, part 1 (RAG)

- Documents: RIPE docs, key BGP RFCs and the project's own docs.
- Chunking and embeddings stored in pgvector inside Postgres.
- Retrieval → prompt → answer with citations.
- Ollama (free, local) for development and a hosted API for the demo, switchable with one config change.

### Phase 6: LLM assistant, part 2 (text-to-SQL and evals)

- The LLM writes SQL from the schema, the system runs it, and the LLM explains the result.
- Safety: a read-only database user, query validation, row limits.
- A router that decides whether a question needs SQL, docs or both.
- Evals: 50+ test questions with expected answers, automatic accuracy scoring and a comparison of models and prompts.
- A Streamlit chat UI.

### Phase 7: the agent

- Build the agent loop by hand first, without frameworks.
- Tools: `query_database`, `search_docs`, `fetch_live_ripestat` (and other sources), `get_neighbor_networks`, `write_incident_report`.
- Triggered automatically by high-severity anomalies.
- Cross-network investigation, for example "Lumen had an incident; which tracked European networks were affected downstream?"
- Guardrails: a step limit, a cost limit and a log of every decision.
- Evaluate it on known past incidents.
- Optional: rebuild it with an agent framework and compare, and expose the tools as an MCP server.

### Phase 8: cloud, observability and product features

- Docker Compose locally, then AWS.
- Monitoring: model drift, LLM cost and latency, agent success rate.
- Product features: user accounts and multi-tenancy, per-customer watchlists, email and Telegram alerts, Stripe in test mode (currencies and EU VAT), reports in several languages (ES, EN, CA, DE), RDAP across all five regional internet registries, GDPR basics (EU hosting, privacy policy), and UTC storage with local display.

### Phase 9: portfolio polish

- README with an architecture diagram, results tables and limitations.
- Demo video: anomaly → agent investigates → the assistant answers questions.
- A write-up or LinkedIn post per phase, with headline metrics.

### Phase 10: launch

- Open-source release, a landing page and the public dashboard.
- Posts in networking communities and on LinkedIn.
- A free beta with a few customers.
- Expand to 100–150 networks.
