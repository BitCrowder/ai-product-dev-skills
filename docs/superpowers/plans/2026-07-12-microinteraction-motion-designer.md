# Microinteraction Motion Designer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a professional Codex skill for UI microinteraction design and implementation-ready motion specs.

**Architecture:** Add one independent skill folder to the existing `ai-product-dev-skills` repository. Keep the main workflow in `SKILL.md` and detailed reusable material in `references/`.

**Tech Stack:** Codex skill format, Markdown, YAML, `init_skill.py`, `quick_validate.py`, GitHub CLI/API.

## Global Constraints

- Skill name must be `microinteraction-motion-designer`.
- Skill must include `SKILL.md`, `agents/openai.yaml`, and reference files.
- Skill description must precisely trigger on UI motion, microinteractions, VibeCoding prompts, animation specs, and frontend implementation guidance.
- No template TODO text may remain.
- Skill must pass `quick_validate.py`.

---

### Task 1: Scaffold Skill

**Files:**
- Create: `microinteraction-motion-designer/`

- [x] Run `init_skill.py microinteraction-motion-designer --resources references`.
- [x] Confirm generated skill folder contains `SKILL.md`, `agents/openai.yaml`, and `references/`.

### Task 2: Write Skill Content

**Files:**
- Modify: `microinteraction-motion-designer/SKILL.md`
- Modify: `microinteraction-motion-designer/agents/openai.yaml`
- Create: `microinteraction-motion-designer/references/motion-patterns.md`
- Create: `microinteraction-motion-designer/references/templates.md`
- Create: `microinteraction-motion-designer/references/checklists.md`
- Create: `microinteraction-motion-designer/references/examples.md`

- [x] Replace generated TODO content.
- [x] Add precise trigger description.
- [x] Add workflow, output modes, and quality gates.
- [x] Add ten motion patterns from the screenshot material.
- [x] Add motion spec and VibeCoding prompt templates.
- [x] Add QA, performance, and accessibility checklists.

### Task 3: Validate and Publish

**Files:**
- Read: `microinteraction-motion-designer/**`

- [x] Run `quick_validate.py`.
- [x] Scan for template TODO text.
- [ ] Commit local changes.
- [ ] Upload changes to `BitCrowder/ai-product-dev-skills`.
- [ ] Verify remote file tree.
