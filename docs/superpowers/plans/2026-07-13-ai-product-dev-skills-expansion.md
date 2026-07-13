# AI Product Dev Skills Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add 12 broadly useful product and developer workflow skills to the existing public skill repository.

**Architecture:** Each skill is an independent Codex skill folder with a concise `SKILL.md`, UI metadata, and three reference files for templates, checklists, and examples.

**Tech Stack:** Codex Skill format, Markdown, YAML, `init_skill.py`, `quick_validate.py`, GitHub CLI/API.

## Global Constraints

- Do not rewrite existing completed skills.
- Skip duplicates: `prototype-brief-builder` and `launch-readiness-checklist` already exist.
- Skip overly specialized additions in this batch: `rag-debugger` and `agent-observability-triage`.
- Every added skill must pass `quick_validate.py`.
- No generated TODO text may remain.

---

### Task 1: Scaffold Missing Skills

**Files:**
- Create: 12 new skill folders

- [x] Create standard skill folders with `init_skill.py`.
- [x] Include `references/` for each folder.

### Task 2: Write Product Workflow Skills

**Files:**
- Create/modify: product-side skill folders

- [x] Write `roadmap-prioritizer`.
- [x] Write `feature-discovery-interviewer`.
- [x] Write `metric-diagnosis`.
- [x] Write `experiment-designer`.
- [x] Write `stakeholder-update-writer`.
- [x] Write `user-feedback-synthesizer`.

### Task 3: Write Developer Workflow Skills

**Files:**
- Create/modify: developer-side skill folders

- [x] Write `codebase-onboarding`.
- [x] Write `spec-to-implementation-plan`.
- [x] Write `bug-debugging-playbook`.
- [x] Write `code-review-assistant`.
- [x] Write `test-generator`.
- [x] Write `refactor-with-safety`.

### Task 4: Validate and Publish

**Files:**
- Read: all added skill folders

- [x] Run `quick_validate.py` on each new skill.
- [x] Scan for TODO/template residue.
- [ ] Commit local changes.
- [ ] Upload changes to GitHub.
- [ ] Verify remote file tree.
