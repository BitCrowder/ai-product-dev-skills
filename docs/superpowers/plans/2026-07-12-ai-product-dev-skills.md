# AI Product Dev Skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build, validate, and publish six engineering-grade Codex skills for AI product and development workflows.

**Architecture:** Use one public repository containing six independent skills. Each skill keeps execution instructions in `SKILL.md` and detailed reusable output structures in `references/`.

**Tech Stack:** Codex skill format, Markdown, YAML, GitHub CLI, `quick_validate.py`.

## Global Constraints

- Skill names use lowercase hyphen-case.
- Every skill has `SKILL.md`, `agents/openai.yaml`, and at least two reference files.
- No generated Skill file may contain TODO placeholders.
- Every Skill must pass `quick_validate.py`.
- Publish to a public GitHub repository named `ai-product-dev-skills`.

---

### Task 1: Scaffold Skills

**Files:**
- Create: `prd-builder/`
- Create: `competitive-research-brief/`
- Create: `prototype-brief-builder/`
- Create: `issue-to-pr/`
- Create: `ai-app-eval-builder/`
- Create: `launch-readiness-checklist/`

- [x] Run `init_skill.py` once per skill with `--resources references`.
- [x] Confirm every folder contains `SKILL.md`, `agents/openai.yaml`, and `references/`.

### Task 2: Write Skill Instructions

**Files:**
- Modify: each skill's `SKILL.md`

- [x] Replace template TODO content.
- [x] Add trigger-optimized YAML descriptions.
- [x] Add workflow, output contract, quality gates, and reference routing.

### Task 3: Add References

**Files:**
- Create: `references/templates.md`
- Create: `references/checklists.md`
- Create: `references/examples.md`

- [x] Add artifact templates for each skill.
- [x] Add validation checklists for each skill.
- [x] Add concise example invocation and output skeletons.

### Task 4: Validate

**Files:**
- Read: all skill folders

- [x] Run `quick_validate.py` on every skill.
- [x] Search for TODO placeholders.
- [x] Confirm reference files are linked from `SKILL.md`.

### Task 5: Publish

**Files:**
- Read: full repository tree

- [x] Initialize local git repository.
- [x] Commit all files.
- [x] Create public GitHub repo `BitCrowder/ai-product-dev-skills`.
- [x] Push or upload files.
- [x] Verify remote visibility and file tree.
