---
name: prd-builder
description: Create rigorous product requirements documents from ideas, stakeholder notes, user problems, customer feedback, feature requests, prototypes, or meeting notes. Use when the user asks for a PRD, product spec, feature spec, requirements doc, user stories, acceptance criteria, success metrics, MVP scope, product planning, or wants to turn a rough product idea into an engineering-ready product brief.
---

# PRD Builder

## 中文简介

**PRD 生成器**：把模糊产品想法、用户问题或会议笔记整理成工程可用的 PRD，包括目标、用户、范围、需求、指标、风险、验收标准和待确认问题。

## Overview

Use this skill to turn ambiguous product ideas into review-ready PRDs with clear goals, user needs, requirements, scope boundaries, success metrics, risks, and acceptance criteria.

The output must help design, engineering, data, and business stakeholders make decisions. Do not produce a polished essay that hides uncertainty.

## Workflow

### 1. Build Context First

Collect or infer:

- product or feature idea
- target users and jobs-to-be-done
- user problem and current workaround
- business goal
- trigger or source of the request
- existing evidence, data, feedback, or customer quotes
- constraints such as platform, timeline, compliance, team, and dependencies
- non-goals and out-of-scope areas

If major context is missing, ask up to 7 focused questions. If the user wants speed, proceed with labeled assumptions.

### 2. Separate Evidence From Assumptions

Create these sections before writing requirements:

- **Known facts:** directly supplied or sourced information
- **Assumptions:** plausible but unverified claims
- **Open questions:** decisions or evidence needed before build
- **Product risks:** usability, technical, data, business, legal, support, or go-to-market risks

Do not convert assumptions into requirements without labeling them.

### 3. Define the Product Decision

State:

- why this should exist now
- who it serves first
- what user behavior should change
- what business or product metric should move
- what a deliberately small v1 includes
- what a later version may include

Use a prioritization frame when scope is contested: MoSCoW, RICE, impact/effort, or must/should/could.

### 4. Write the PRD

Use `references/templates.md` for the full PRD template. Include:

- summary
- goals and non-goals
- personas or user segments
- problem statement
- user stories or jobs
- functional requirements
- non-functional requirements
- UX and content requirements
- analytics and success metrics
- dependencies
- rollout or migration notes
- risks and mitigations
- acceptance criteria
- launch or readiness requirements

Keep requirements testable. Prefer "The user can..." and "The system must..." over vague adjectives.

### 5. Add Acceptance Criteria

For every core requirement, include acceptance criteria in Given/When/Then or checklist form.

Acceptance criteria must cover:

- happy path
- empty state
- error state
- permission or eligibility edge cases
- analytics event if measurement matters
- accessibility or responsive behavior when relevant

### 6. Quality Gate

Before returning the PRD, run the checklist in `references/checklists.md`.

The PRD is not ready if:

- the target user is unclear
- the success metric is missing
- requirements cannot be tested
- scope includes everything the user mentioned
- assumptions are hidden
- engineering dependencies are not named
- launch or support impact is ignored

## Output Rules

- Start with a concise executive summary.
- Use tables for requirements, metrics, risks, and open questions.
- Mark unresolved decisions clearly.
- If the user asks for a shorter output, preserve the decision-critical sections and move detail into appendices.
- If the user provides source material, quote sparingly and summarize the evidence.

## References

- Read `references/templates.md` when drafting the PRD artifact.
- Read `references/checklists.md` before finalizing.
- Read `references/examples.md` when the user wants sample phrasing or a lightweight example.
