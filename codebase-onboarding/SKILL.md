---
name: codebase-onboarding
description: Quickly understand and explain unfamiliar codebases, repositories, services, apps, libraries, or monorepos. Use when the user asks to onboard to a repo, summarize architecture, find entry points, explain how to run tests, identify key modules, map data flow, inspect risks, create a developer orientation, or produce next-step guidance before making code changes.
---

# Codebase Onboarding

## Overview

Use this skill to build a practical mental model of a codebase before changing it. The output should help a developer know where to start, what matters, how to run it, and what risks exist.

Do not summarize every file. Prioritize architecture, entry points, workflows, dependencies, ownership boundaries, tests, and likely change areas.

## Workflow

1. Inspect repository structure with fast file search.
2. Identify tech stack, package managers, build scripts, test commands, and runtime entry points.
3. Read README, configuration, package manifests, routes, app entry files, and test setup.
4. Map major modules and data/control flow.
5. Identify external dependencies, environment variables, persistence, APIs, background jobs, and deployment surfaces.
6. Identify risk areas: missing tests, large files, unclear boundaries, deprecated dependencies, secrets handling, and fragile scripts.
7. Produce an onboarding brief with "start here" guidance and next investigation steps.

## Output Contract

Always include:

- repo purpose and stack
- how to run/build/test
- architecture map
- key directories and entry points
- data/control flow
- important dependencies and config
- test coverage orientation
- risks and unknowns
- suggested next steps

Use `references/templates.md` and validate with `references/checklists.md`.
