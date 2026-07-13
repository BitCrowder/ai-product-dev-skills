---
name: spec-to-implementation-plan
description: Convert product specs, PRDs, tickets, design briefs, technical proposals, or vague requirements into implementation plans with tasks, files, interfaces, tests, risks, and verification steps. Use when the user asks to plan implementation, break down a feature, create an engineering plan, turn a spec into tasks, define milestones, or prepare safe execution before coding.
---

# Spec To Implementation Plan

## 中文简介

**规格转实施计划**：把 PRD、设计说明、技术规格或模糊需求拆成工程实施计划，包括任务、文件、接口、测试、风险、上线和验证步骤。

## Overview

Use this skill to translate requirements into an executable engineering plan. The plan must be small-step, testable, scoped, and explicit enough for another agent or engineer to execute.

Do not start coding from a vague spec. Resolve ambiguity, state assumptions, and define acceptance checks.

## Workflow

1. Extract goals, non-goals, users, acceptance criteria, constraints, and dependencies.
2. Identify affected architecture, files, APIs, data models, UI surfaces, and test suites.
3. Break work into independently reviewable tasks.
4. Define interfaces each task consumes and produces.
5. Add test strategy: unit, integration, E2E, migration, manual QA, or observability.
6. Add risk controls: feature flags, rollback, compatibility, data migration, and monitoring.
7. Produce a sequenced plan with verification commands and expected outcomes.

## Output Contract

Always include:

- requirement summary
- assumptions and open questions
- file/module map
- task breakdown
- interfaces/contracts
- test plan
- risk and rollout plan
- verification checklist

Use `references/templates.md` for implementation-plan format.
