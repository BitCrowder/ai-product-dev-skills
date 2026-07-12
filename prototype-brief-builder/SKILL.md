---
name: prototype-brief-builder
description: Convert product requirements, PRDs, feature ideas, user flows, sketches, screenshots, or stakeholder notes into prototype-ready briefs for Figma, designers, Codex, Cursor, or frontend implementation. Use when the user asks for a prototype brief, wireframe spec, screen-by-screen UX plan, design handoff, clickable prototype scope, UI flow, component/state inventory, or a build prompt for an app or website prototype.
---

# Prototype Brief Builder

## Overview

Use this skill to transform product intent into a prototype brief that can be executed by a designer, design tool, or coding agent.

The brief must describe what to build, how screens connect, which states exist, what content appears, and what decisions remain unresolved.

## Workflow

### 1. Identify Prototype Purpose

Clarify the prototype type:

- concept test
- usability test
- stakeholder alignment
- sales demo
- engineering handoff
- clickable flow
- high-fidelity product surface

The purpose determines fidelity. Do not over-spec visual polish for a concept test or under-spec states for engineering handoff.

### 2. Extract Product Requirements

Collect:

- target user and scenario
- user goal
- entry point and exit condition
- required screens
- key decisions and actions
- content requirements
- data required on each screen
- platform and viewport
- design system or brand constraints
- technical constraints

If a PRD exists, derive the prototype brief from its requirements and acceptance criteria.

### 3. Define Flow and Screens

Create:

- primary user flow
- alternate flows
- screen inventory
- state inventory
- component inventory
- data and content mapping
- interaction rules

Every screen must have a purpose. Remove screens that do not help validate or communicate the core flow.

### 4. Specify States

For each important screen or component, include:

- default
- empty
- loading
- error
- success
- disabled
- permission or unauthenticated
- edge cases such as long text, no results, or partial data

Use `references/templates.md` for structured tables.

### 5. Define Handoff Detail

For design or engineering handoff, include:

- responsive behavior
- accessibility expectations
- analytics events
- copy requirements
- placeholder versus final content
- visual references
- implementation notes
- open questions

If generating a prompt for a coding agent, make it explicit enough to build without inventing product logic.

### 6. Quality Gate

Read `references/checklists.md` before finalizing.

The prototype brief is not ready if:

- the target test or handoff purpose is unclear
- screens are listed without flow
- states are missing
- content is left as generic filler
- mobile behavior is ignored
- unresolved decisions are hidden

## Output Rules

- Start with prototype purpose and fidelity level.
- Use flow diagrams or numbered steps for navigation.
- Use tables for screen, state, and component inventories.
- Mark assumptions and open questions clearly.
- If visual design is out of scope, say so and focus on structure.

## References

- Read `references/templates.md` for prototype brief structures.
- Read `references/checklists.md` before finalizing.
- Read `references/examples.md` for example invocation and skeletons.
