---
name: teach
description: Level-0 lesson on one concept, tied to NetSentinel, with a two-question quiz. Run it as /teach <concept>.
disable-model-invocation: true
argument-hint: "[concept]"
---

Teach me **$ARGUMENTS** as it applies to NetSentinel. I know Python, SQL and basic networking; I'm new to most ML and LLM topics.

1. **Intuition first.** What problem it solves and the mental model, in 3–5 bullets.
2. **One worked example from this project.** Use a recorded response in `tests/fixtures/`, a table from our schema, or a realistic BGP case. Keep any code under 20 lines and runnable.
3. **Pitfalls.** Two or three mistakes that would bite this project in particular.
4. **Quiz.** Ask me two questions that test understanding, not recall. Then stop and wait for my answers.
5. **Feedback.** Say what I got right, correct what I missed, and give me one follow-up exercise I can finish in under 30 minutes.
6. **Log it.** Draft a `docs/learning-log.md` entry in its template, written from my point of view. Save it only after I've corrected or approved it.

Rules:
- Don't write project code during a lesson.
- Link only to official docs or sources you're sure exist.
- If the concept depends on facts that change (a library API, an ASN owner, a licence), say whether you checked them this session.

make no mistakes
