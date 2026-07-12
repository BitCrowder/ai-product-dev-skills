# Microinteraction Motion Designer Design

## Goal

Add a professional Codex skill that turns VibeCoding-style UI motion advice into precise, implementation-ready microinteraction specs for apps, websites, and AI-built interfaces.

## Source Material

The user supplied screenshots describing ten microinteraction patterns:

- staggered list entrance
- press ripple
- skeleton shimmer
- sliding tabs
- crossfade/dissolve
- scroll-linked transformation
- spring drag
- chart growth
- push transition
- state morph

The key principle extracted from the material is that microinteractions should imitate physical rhythm and cause-effect so UI changes feel continuous, responsive, and premium rather than stiff.

## Skill Design

Create `microinteraction-motion-designer` as an independent skill in `ai-product-dev-skills`.

The skill should:

- trigger on requests about UI motion, microinteractions, premium app feel, VibeCoding prompts, animation specs, and frontend motion guidance
- force vague motion adjectives into concrete specs
- include a reusable motion pattern library
- include implementation-ready templates
- include QA, performance, and accessibility checklists
- provide prompts for AI coding tools

## File Structure

- `microinteraction-motion-designer/SKILL.md`: workflow, trigger description, output modes, and quality gates
- `microinteraction-motion-designer/agents/openai.yaml`: UI metadata
- `microinteraction-motion-designer/references/motion-patterns.md`: ten motion patterns and easing guidance
- `microinteraction-motion-designer/references/templates.md`: motion spec and VibeCoding prompt templates
- `microinteraction-motion-designer/references/checklists.md`: product, UX, engineering, and accessibility checks
- `microinteraction-motion-designer/references/examples.md`: compact examples and reusable prompts

## Validation

Run `quick_validate.py`, scan for template TODO text, and verify that every referenced file is linked from `SKILL.md`.
