---
name: check-my-work
description: Read-only senior review of my uncommitted changes (or the files I name), ranked by severity, in a fresh context. Run it as /check-my-work [files or git range].
disable-model-invocation: true
argument-hint: "[files or git range]"
context: fork
agent: reviewer
background: false
---

Review my work on NetSentinel. I'm a student learning to build production-quality data and ML systems.

Target: $ARGUMENTS
If the target above is empty, review all uncommitted changes.

## Current changes

!`git status --short`

!`git diff HEAD --stat`

## How to review

1. Read `CLAUDE.md`, then each changed file in full (untracked files too), not just the diff hunks. Use `git diff HEAD -- <file>` to see what changed.
2. Run `python -m ruff check .` and `python -m pytest -q`, and include the results.
3. Don't edit, create or delete any file, and don't rewrite my code.

## Report

1. **Verdict** in one line.
2. **Issues by severity**: Bug, Design, Test gap, Style. For each: `file:line`, why it matters for NetSentinel, and a hint towards the fix (not the full fix).
3. **Questions** you'd ask me in a real code review.
4. **One lesson**: the single most useful thing I should learn from this review, with an official docs link if one helps.

make no mistakes
