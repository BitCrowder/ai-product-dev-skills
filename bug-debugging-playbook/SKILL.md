---
name: bug-debugging-playbook
description: Systematically debug bugs, regressions, crashes, flaky tests, broken UI flows, production incidents, unexpected behavior, and failing builds. Use when the user asks to fix a bug, investigate a failure, reproduce an issue, find root cause, debug tests, inspect logs, or create a minimal safe fix with regression coverage.
---

# Bug Debugging Playbook

## 中文简介

**系统化 Bug 调试手册**：用于排查 Bug、崩溃、回归、失败测试或异常行为。它会先复现问题、建立假设、定位根因，再给出最小修复和回归验证。

## Overview

Use this skill to debug before fixing. The workflow emphasizes reproduction, evidence, hypotheses, root cause, minimal change, and regression verification.

Do not patch symptoms just because the likely fix is obvious. First prove what is failing.

## Workflow

1. Capture the symptom, expected behavior, actual behavior, environment, version, and reproduction steps.
2. Reproduce or create the closest failing test/log/trace.
3. Identify the last known good state, recent changes, and affected boundaries.
4. Generate hypotheses and rank by evidence.
5. Inspect the smallest relevant code path.
6. Apply the minimal fix.
7. Add or update regression tests.
8. Verify original symptom and surrounding behavior.
9. Document root cause, fix, tests, and residual risk.

## Output Contract

Always include:

- reproduction status
- evidence gathered
- hypotheses considered
- root cause
- fix summary
- regression test
- verification commands
- remaining risk

Use `references/templates.md` and `references/checklists.md`.
