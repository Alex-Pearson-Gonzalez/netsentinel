---
name: wrap-up
description: End-of-session wrap-up that updates docs/progress.md and drafts decision and learning-log entries. Run it as /wrap-up.
disable-model-invocation: true
allowed-tools:
  - Edit(docs/**)
  - Bash(git status *)
  - Bash(git log *)
  - Bash(git diff *)
---

Wrap up this session.

1. **Check what happened.** Run `git status` and `git log --oneline -10`, and use what we did in this conversation.
2. **Update `docs/progress.md`**, keeping its structure: set today's date, move finished items to "Done this week", set the next three tasks, and update blockers, open questions and numbers.
3. **Decisions.** If we chose between real options, draft an ADR for `docs/decisions.md` using its template and show it to me. Add it only after I say yes.
4. **Learning log.** Draft one `docs/learning-log.md` entry from my point of view (what I learned, what confused me). Save it only after I've corrected it.
5. **Commit message.** Suggest a conventional commit message for the docs changes. Don't commit or push.
6. **Summary.** Finish with three lines: done, next, blocked.

make no mistakes
