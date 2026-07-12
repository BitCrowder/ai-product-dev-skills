---
name: issue-to-pr
description: Convert GitHub issues, bug reports, feature requests, Linear/Jira tickets, TODOs, or product requirements into implementation-ready plans, code changes, tests, verification evidence, and pull request descriptions. Use when the user asks to work an issue, fix a bug from an issue, implement a ticket, prepare a PR, link a PR to an issue, create a PR summary, or turn product requirements into a safe engineering change.
---

# Issue To PR

## Overview

Use this skill to move from an issue or ticket to a review-ready pull request with minimal scope, clear evidence, and traceable verification.

The goal is not just to write code. The goal is to preserve intent, reduce regression risk, and make review easy.

## Workflow

### 1. Resolve Context

Identify:

- repository and branch
- issue or ticket source
- expected behavior
- actual behavior
- acceptance criteria
- affected users or systems
- reproduction steps
- related PRs, commits, logs, screenshots, or tests

If the issue is ambiguous, ask focused questions or write explicit assumptions before editing.

### 2. Classify the Work

Classify as:

- bug fix
- feature
- refactor
- test-only change
- documentation
- operational or configuration change

The classification determines verification. A bug fix needs reproduction and regression testing. A feature needs acceptance criteria and coverage. A refactor needs behavior preservation.

### 3. Plan Before Editing

Produce a short implementation plan:

- files likely to change
- interfaces or contracts affected
- tests to add or update
- migration or compatibility concerns
- risks and rollback
- out-of-scope changes

Keep the plan narrow. Do not opportunistically refactor unrelated code.

### 4. Implement Safely

Follow repository conventions. Prefer:

- smallest behavior-preserving change
- tests before or alongside implementation
- local helpers over new abstractions unless repeated complexity justifies it
- structured parsers/APIs over brittle string manipulation
- explicit error handling where the issue involves failure modes

Never overwrite unrelated user changes.

### 5. Verify

Run the most relevant verification commands:

- targeted unit or integration tests
- regression test for the original issue
- build or typecheck when changed code is compiled
- lint when repository uses linting
- manual/browser verification for UI changes

Capture command names and outcomes. If verification cannot run, state why and what remains unverified.

### 6. Prepare PR

Use `references/templates.md` for the PR description.

The PR summary must include:

- linked issue or ticket
- problem
- solution
- files or areas changed
- tests run
- screenshots or evidence for UI changes
- risks and rollout notes
- follow-up work if any

For GitHub, use closing keywords only when the PR should close the issue after merge.

### 7. Quality Gate

Read `references/checklists.md` before finalizing. The work is not PR-ready if:

- the issue intent is unclear
- no verification was run or explained
- acceptance criteria are not mapped to changes
- unrelated refactors are mixed in
- PR description omits risk or test evidence

## Output Rules

- Lead with findings, plan, or changed behavior depending on user request.
- Include exact verification commands and results.
- Link issue references when available.
- Mark assumptions.
- Keep PR description concise but review-complete.

## References

- Read `references/templates.md` for implementation plan and PR body templates.
- Read `references/checklists.md` before finalizing or opening a PR.
- Read `references/examples.md` for sample issue-to-PR outputs.
