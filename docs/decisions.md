# Decisions

Architecture decision records (ADRs), newest first. Write one whenever we choose between real options. Status is proposed, accepted, or superseded by ADR-NNN.

## Template

```markdown
## ADR-NNN: <the decision in a few words>
Date: YYYY-MM-DD · Status: proposed
Context: what forces the decision.
Options: (a) … (b) … (c) …
Decision: which option, and the main reason.
Consequences: what gets easier, what gets harder.
Revisit when: the signal that would reopen it.
```

## Due soon

- ADR-010: time-series schema (Week 5)
- ADR-011: HTTP client, retries and rate limiting for source adapters (Week 6)
- ADR-012: watchlist selection rule (Week 7)

## ADR-009: Agent safety rules
Date: 2026-10-08 · Status: accepted
Context: The agent (Phase 7) reads text from internet registries, such as network and company descriptions. Anyone can write that text, including text designed to trick an AI into doing something (prompt injection). The agent also writes incident reports, and a wrong public report that blames a real company could cause real problems.
Options: (a) let the agent read registry text freely and publish reports automatically; (b) treat registry text as untrusted data and have a human review public reports that name a company.
Decision: (b). Registry text is data the agent can read and quote but never follows as instructions. I review anything public that names a company before it is published.
Consequences: Easier: protection against prompt injection and against publishing wrong accusations. Harder: public reports are not instant; they wait for my review.
Revisit when: the agent has a long, measured record of accurate reports on known incidents and a reliable automatic check exists.

## ADR-008: Build paid features only on clearly licensed data
Date: 2026-10-08 · Status: accepted
Context: Not all data sources allow commercial use. RIPEstat's terms forbid paid use without written permission from RIPE NCC, and Cloudflare Radar, CAIDA and PeeringDB have their own terms. (My reading of the terms, not legal advice; to be confirmed with each provider.)
Options: (a) use any source for anything and ask later; (b) use only clearly licensed sources for paid features and keep the rest for free or non-commercial parts.
Decision: (b). Paid features use only RIS raw data, RIS Live and RouteViews, crediting RIPE NCC / RIS and acknowledging RouteViews as they ask. RIPEstat, Cloudflare Radar, CAIDA and PeeringDB stay in free or non-commercial parts until I get written permission.
Consequences: Easier: no risk of selling data I'm not allowed to sell. Harder: every stored data point must record its source so paid features can filter by it, so the adapter layer must add this from the start.
Revisit when: a provider gives written permission or changes its terms.

## ADR-007: Track organisations, not single ASNs, and log mergers as known events
Date: 2026-10-08 · Status: accepted
Context: One company can own several ASNs (Autonomous System Numbers, the ID of each network), e.g. Sprint AS1239 under Cogent and Cox AS22773 under Charter. Mergers and spin-offs cause big routing changes that are expected, not anomalies.
Options: (a) a flat list of ASNs; (b) organisations that each own one or more ASNs, with mergers and spin-offs stored as dated events.
Decision: (b). Known events so far: Colt–Lumen EMEA (Europe, Middle East and Africa), Nov 2023; Sunrise spin-off from Liberty Global, 15 Nov 2024; AT&T–Lumen consumer fibre, Feb 2026; Charter–Cox, 20 Aug 2026.
Consequences: Easier: fewer false alarms, and reports describe companies the way people know them. Harder: more database tables. To keep Phase 1 simple, start with an organisation column on the ASN table and split it out later.
Revisit when: the single column can't represent an ownership change correctly.

## ADR-006: Keep an incident catalogue from the start
Date: 2026-10-08 · Status: accepted
Context: To prove the anomaly detector (Phase 3) and the agent (Phase 7) work, I need real past incidents with known times to test against. The original plan only looked for them in Phase 2.
Options: (a) look for incidents during EDA in Phase 2; (b) keep a catalogue from Phase 1 and grow it over time.
Decision: (b). Each entry records what happened, which networks, start and end time in UTC, and sources. Seeded with the Level(3) outage (30 Aug 2020, 10:03–14:30 UTC) and the Verizon route leak (24 Jun 2019, 10:34–12:39 UTC).
Consequences: Easier: a labelled test set exists before any model, and it doubles as the agent's test set. Harder: the normal backfill covers only a few recent months, so the data around each catalogued incident must be fetched separately.
Revisit when: never dropped; only the way it is stored may change.

## ADR-005: Measure transit networks by what they carry, not only what they originate
Date: 2026-10-08 · Status: accepted
Context: Transit networks (e.g. Lumen AS3356, Arelion AS1299) mainly carry other networks' traffic. The prefixes (blocks of IP addresses) they originate themselves are a small part of what they do.
Options: (a) originated prefix counts for every network; (b) extra transit metrics for transit networks.
Decision: (b). For transit networks, measure transited prefixes (routes passing through them), number of neighbours, update rates and leaks. Incumbents and cable/mobile operators keep originated prefixes as a main signal.
Consequences: Easier: a much better signal for the most important networks. Harder: these metrics need AS paths (the list of networks a route passes through), so they are harder to compute.
Revisit when: EDA in Phase 2 shows a metric adds no useful signal.

## ADR-004: Poll state data three times a day; get fast signals separately
Date: 2026-10-08 · Status: accepted
Context: The plan said to collect every hour, but RIPEstat state data comes from RIS (Routing Information Service) snapshots taken every 8 hours, at 00:00, 08:00 and 16:00 UTC (Coordinated Universal Time). Hourly polling would download the same snapshot about 8 times.
Options: (a) hourly polling; (b) state data three times a day plus a separate fast-signal source.
Decision: (b). Collect state data after each snapshot, leaving a margin for processing. Take fast signals from RIPEstat's bgp-update-activity endpoint (1-minute bins). Add RIS Live (real-time stream) in the scale-up phase.
Consequences: Easier: no wasted API calls, and the data matches how the source updates. Harder: state data has at most 8-hour resolution. RIPEstat needs permission for paid use (ADR-008), so paid features will need RIS raw data or RIS Live instead.
Revisit when: RIS changes its snapshot schedule or RIS Live is added.

## ADR-003: Native PostgreSQL partitioning now; decide on TimescaleDB later
Date: 2026-10-08 · Status: accepted
Context: The metrics table stores timestamped values for every tracked network, so it will grow large. The plan said to move to TimescaleDB (a PostgreSQL extension for time-series data), but Amazon RDS (Relational Database Service, AWS's managed database) does not offer it.
Options: (a) TimescaleDB now; (b) native PostgreSQL partitioning now, TimescaleDB decision later.
Decision: (b). Split the metrics table into smaller pieces by time, e.g. one partition per month.
Consequences: Easier: works the same locally (Docker) and on RDS, with no extra extension. Harder: future partitions must be created by me (e.g. a scheduled job), and there are no TimescaleDB extras such as automatic compression.
Revisit when: queries get slow despite partitioning, or I move off RDS to a host that supports TimescaleDB.

## ADR-002: Add a v0.1 slice and move the scale-up phase later
Date: 2026-10-08 · Status: accepted
Context: The original plan put the scale-up phase (RouteViews, RIS Live, MRT files, TimescaleDB, a message queue, 60–80 networks) right after Phase 4, before the AI parts. That means months of infrastructure before the main idea works end to end, while I'm applying for summer 2027 internships now.
Options: (a) keep the original order; (b) end Phase 1 with a small end-to-end v0.1 and move scale-up after Phase 7.
Decision: (b). v0.1 by 20 Dec 2026 on the core watchlist, with a short write-up. Scale-up moves after Phase 7 (the agent).
Consequences: Easier: a presentable project by December, and the AI parts (the main learning goal) come sooner. Harder: streaming and message-queue skills (RIS Live, Kafka or Redis Streams) come later.
Revisit when: an internship I'm targeting clearly asks for streaming experience before Phase 7 is reached.

## ADR-001: Make the assistant a full AI chat assistant
Date: 2026-10-06 · Status: accepted
Context: The original plan described the assistant (building block B) as "question in, answer out". Each question was handled on its own, with no memory of earlier messages. That works, but it feels like a search box, not a conversation.
Options: (a) single question-and-answer, no memory; (b) a full chat assistant with conversation features.
Decision: (b). Five chat features: (1) conversation memory, so earlier messages in the same chat count ("And did it affect BT?" works); (2) follow-up suggestions, 1–3 next questions after each answer; (3) sources shown, so every answer says whether it came from the database, a document or an incident report; (4) clarifying questions when a question is ambiguous (e.g. "Telefónica" could mean several networks); (5) answers in ES, EN, CA or DE. Phase 6 adds features 1–4 to the Streamlit chat. Phase 7 lets the chat hand hard questions to the agent ("Investigate this for me"). Phase 8 adds feature 5 and saved chats per user account.
Consequences: Easier: more useful, feels like a real product, stronger CV line. Harder: more work in Phase 6 (managing chat history and the context window, the maximum text an LLM can read at once), e.g. summarising older messages in long chats. The eval set needs a few multi-turn test conversations (several back-and-forth messages) on top of the 50 single questions.
Revisit when: evals show that chat history makes answers less accurate, or LLM cost per conversation gets too high.
