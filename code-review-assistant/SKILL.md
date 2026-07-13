---
name: code-review-assistant
description: Perform senior-engineer code reviews for pull requests, diffs, patches, or changed files. Use when the user asks to review code, inspect a PR, find bugs, assess risk, check tests, evaluate architecture, review frontend behavior, review API changes, or produce actionable review findings with severity and file/line references.
---

# Code Review Assistant

## Overview

Use this skill to review code for correctness, regressions, missing tests, security-sensitive behavior, data loss, performance, accessibility, and maintainability.

Lead with findings. Do not spend the review praising code or summarizing changes unless there are no issues.

## Workflow

1. Understand the intended behavior and changed surface.
2. Inspect the diff and nearby code paths.
3. Prioritize bugs, regressions, edge cases, missing tests, and contract breaks.
4. Verify claims against code, tests, and runtime assumptions.
5. Assign severity: blocker, high, medium, low.
6. Provide concise findings with file/line, why it matters, and suggested fix.
7. List test gaps and residual risk.

## Output Contract

Always include:

- findings first, ordered by severity
- exact file/line references when available
- impact and reproduction reasoning
- suggested fix
- open questions
- test gaps
- brief summary only after findings

Use `references/templates.md` for review format and `references/checklists.md`.
