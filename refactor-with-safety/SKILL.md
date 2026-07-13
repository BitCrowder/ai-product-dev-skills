---
name: refactor-with-safety
description: Plan and execute safe refactors that preserve behavior while improving structure, naming, boundaries, duplication, performance, or maintainability. Use when the user asks to refactor code, clean up architecture, split large files, reduce duplication, extract helpers, modernize code, improve readability, or change internal structure without changing user-visible behavior.
---

# Refactor With Safety

## Overview

Use this skill to refactor without accidental behavior changes. The workflow locks behavior first, changes structure in small steps, and verifies after each meaningful change.

Do not mix broad refactors with feature changes unless explicitly requested.

## Workflow

1. Define refactor goal and behavior that must remain unchanged.
2. Inspect current tests and add characterization tests if coverage is weak.
3. Identify seams, dependencies, side effects, and public contracts.
4. Plan small reversible steps.
5. Refactor one boundary at a time.
6. Run targeted tests after each step.
7. Compare behavior and document any intentional differences.
8. Stop when complexity is meaningfully reduced; do not polish endlessly.

## Output Contract

Always include:

- refactor goal
- non-goals
- behavior-preservation plan
- files and boundaries
- test/verification plan
- step sequence
- rollback strategy
- risk notes

Use `references/templates.md` and `references/checklists.md`.
