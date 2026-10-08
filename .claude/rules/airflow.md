---
paths:
  - "dags/**"
---

# Airflow rules

- Airflow 3 only. Write DAGs with the Task SDK: `from airflow.sdk import dag, task` (also `DAG`, `Asset`, `task_group`).
- Use `schedule=`. Airflow 2 patterns such as `schedule_interval`, `execution_date` and SubDAGs don't belong here. Treat Airflow 2 tutorials and suggestions as suspect and check the Airflow 3 docs.
- Set `catchup` explicitly on every DAG (it defaults to False in Airflow 3).
- Keep DAGs thin: tasks call functions from the `netsentinel` package. No business logic, database sessions or HTTP calls at module import time.
- Map over the watchlist with dynamic task mapping (`.expand()`), not a Python loop that creates one task per ASN.
- Retries and failure alerts are set per task, and every task is idempotent, so a rerun of the same interval is safe.
