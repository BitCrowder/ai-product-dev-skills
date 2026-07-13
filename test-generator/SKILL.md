---
name: test-generator
description: Generate focused tests for features, bug fixes, code paths, APIs, UI flows, edge cases, regressions, and refactors. Use when the user asks to add tests, improve coverage, write unit tests, create integration tests, reproduce a bug with a regression test, test frontend states, identify test gaps, or design a test plan before implementation.
---

# Test Generator

## Overview

Use this skill to create meaningful tests tied to behavior and risk. Tests should prove requirements, catch regressions, and document edge cases.

Do not add broad snapshot or superficial tests when a smaller behavioral test can catch the real failure.

## Workflow

1. Identify behavior under test, public interface, risk, and existing test conventions.
2. Classify test level: unit, integration, component, E2E, contract, regression, property, or manual QA.
3. List happy paths, boundaries, empty states, errors, permissions, concurrency, and data variations.
4. Write tests using local framework patterns.
5. For bug fixes, create a failing regression test first when feasible.
6. Run targeted tests and record results.
7. Explain coverage and remaining gaps.

## Output Contract

Always include:

- behavior under test
- test cases and rationale
- files to test
- test level
- setup/mocks/fixtures
- commands to run
- expected results
- remaining gaps

Use `references/templates.md` and `references/checklists.md`.
