---
name: experiment-designer
description: Design A/B tests, holdouts, beta rollouts, feature flags, pricing tests, onboarding experiments, lifecycle experiments, and product validation plans. Use when the user asks to test a hypothesis, design an experiment, compare variants, define success metrics, calculate risks, create rollout plans, avoid invalid tests, or decide whether a product change should ship.
---

# Experiment Designer

## Overview

Use this skill to convert a product hypothesis into a valid experiment with success metrics, guardrails, target population, variants, rollout, risks, and decision rules.

The goal is not just to "run an A/B test"; the goal is to learn a decision-relevant truth with acceptable risk.

## Workflow

1. Define the hypothesis, user segment, product change, and decision the experiment will support.
2. Choose experiment type: A/B test, multivariate, holdout, switchback, staged rollout, beta, fake door, concierge, or qualitative prototype test.
3. Define primary metric, secondary metrics, guardrails, and minimum practical effect.
4. Specify population, eligibility, randomization unit, exposure event, and exclusion rules.
5. Design variants and ensure only intended variables change.
6. Identify risks: sample pollution, novelty effects, seasonality, network effects, instrumentation gaps, ethics, and user harm.
7. Write launch, monitoring, stopping, and decision rules.
8. Produce analysis and communication plan.

## Output Contract

Always include:

- hypothesis
- experiment type and rationale
- variants
- audience and randomization
- metrics and guardrails
- duration or sample considerations
- risks and mitigations
- decision rules
- rollout and rollback plan

Use `references/templates.md` for experiment specs and `references/checklists.md` for validity checks.
