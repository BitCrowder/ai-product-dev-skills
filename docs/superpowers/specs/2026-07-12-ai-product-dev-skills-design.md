# AI Product Dev Skills Design

## Goal

Create six production-quality Codex skills for an AI product/development workflow: PRD creation, competitive research, prototype briefs, issue-to-PR execution, AI app evaluation design, and launch readiness.

## Design Principles

- Each skill must be independently triggerable and useful on its own.
- Each skill must produce structured artifacts, not generic prompt prose.
- Each skill must separate known facts, assumptions, open questions, and recommended decisions.
- Each skill must include explicit quality gates so another agent can judge whether the output is complete.
- Each skill must use progressive disclosure: concise `SKILL.md`, deeper reusable templates in `references/`.
- Each skill must avoid pretending evidence exists. Research-heavy outputs must cite sources or mark claims as assumptions.

## Skill Set

- `prd-builder`: Convert product ideas, notes, customer problems, or stakeholder requests into a PRD with goals, users, scope, requirements, stories, acceptance criteria, metrics, risks, and open questions.
- `competitive-research-brief`: Create evidence-based competitor and market briefs with source tracking, comparison matrices, positioning analysis, gaps, and confidence levels.
- `prototype-brief-builder`: Convert product requirements into a prototype-ready brief with flows, screens, components, states, content, interactions, responsive needs, and handoff checklist.
- `issue-to-pr`: Convert issues or bug reports into an implementation plan, code-change strategy, tests, verification, and PR summary, while preserving GitHub linkage and review readiness.
- `ai-app-eval-builder`: Design eval plans for LLM, RAG, and agent applications with datasets, rubrics, graders, failure taxonomy, regression workflow, and acceptance thresholds.
- `launch-readiness-checklist`: Prepare product or feature launches with cross-functional readiness checks, risks, rollback plans, analytics, support, communications, and go/no-go decision output.

## Repository Structure

Each skill folder contains:

- `SKILL.md`: trigger description, workflow, required outputs, and quality gates
- `agents/openai.yaml`: user-facing metadata
- `references/templates.md`: reusable artifact templates
- `references/checklists.md`: review and validation checks
- `references/examples.md`: minimal example prompts and output skeletons where useful

## Validation

Run `quick_validate.py` on each skill folder. Also inspect every `SKILL.md` for placeholder text and verify that each reference file is linked from the skill body.
