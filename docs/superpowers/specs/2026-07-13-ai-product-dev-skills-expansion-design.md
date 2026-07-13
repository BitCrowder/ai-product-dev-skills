# AI Product Dev Skills Expansion Design

## Goal

Expand the `ai-product-dev-skills` repository with missing general-purpose skills from the AI product manager and AI developer workflow list, while skipping duplicates and overly specialized skills.

## Existing Skills Kept

The repository already includes:

- `prd-builder`
- `competitive-research-brief`
- `prototype-brief-builder`
- `issue-to-pr`
- `ai-app-eval-builder`
- `launch-readiness-checklist`
- `microinteraction-motion-designer`

## Added Skills

Add 12 practical, general-purpose skills:

- `roadmap-prioritizer`
- `feature-discovery-interviewer`
- `metric-diagnosis`
- `experiment-designer`
- `stakeholder-update-writer`
- `user-feedback-synthesizer`
- `codebase-onboarding`
- `spec-to-implementation-plan`
- `bug-debugging-playbook`
- `code-review-assistant`
- `test-generator`
- `refactor-with-safety`

## Deferred Skills

Do not add `rag-debugger` or `agent-observability-triage` in this expansion. They are useful but more specialized than the user's current request for broadly useful skills.

## Structure

Each added skill includes:

- `SKILL.md`: precise trigger description, workflow, output contract
- `agents/openai.yaml`: user-facing metadata
- `references/templates.md`: reusable output templates
- `references/checklists.md`: validation checklist
- `references/examples.md`: compact example invocation and output skeleton

## Validation

Run `quick_validate.py` on every new skill. Scan for generated TODO text and verify reference files exist.
