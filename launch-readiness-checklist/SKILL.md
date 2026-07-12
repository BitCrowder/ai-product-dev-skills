---
name: launch-readiness-checklist
description: Create launch readiness checklists and go/no-go plans for product releases, AI features, web apps, SaaS features, mobile app updates, experiments, beta launches, public launches, migrations, or major changes. Use when the user asks to prepare for launch, check whether a feature can ship, create a release checklist, plan rollout, assess launch risk, write release notes, define rollback, coordinate support, or run a launch readiness review.
---

# Launch Readiness Checklist

## Overview

Use this skill to turn a planned release into a cross-functional readiness review with clear owners, blockers, risks, rollback criteria, and go/no-go recommendation.

The output must help a team decide whether to ship, delay, limit rollout, or run a beta.

## Workflow

### 1. Define Launch Context

Collect:

- product or feature name
- launch type: alpha, beta, internal, staged, public, migration, experiment, or hotfix
- target users and rollout percentage
- platforms affected
- release date or window
- stakeholders and owners
- success metrics
- known risks
- dependencies
- support impact

If the user only asks "can we launch?", first build the context and assumptions.

### 2. Segment Readiness Areas

Assess readiness across:

- product scope and acceptance criteria
- engineering quality
- QA and regression
- data and analytics
- AI evals if an AI feature is involved
- security, privacy, and compliance
- performance and reliability
- customer support and operations
- marketing and communications
- documentation and onboarding
- rollout, monitoring, and rollback

Use `references/templates.md` for the readiness table.

### 3. Identify Blockers and Risks

Classify every issue:

- blocker: must resolve before launch
- launch risk: can launch with mitigation
- follow-up: should not block launch
- explicit non-goal: out of scope

For each risk, include owner, mitigation, trigger, and rollback or escalation path.

### 4. Define Monitoring and Rollback

Specify:

- launch dashboard or metrics
- health checks
- alert thresholds
- support escalation path
- rollback trigger
- rollback owner
- user communication if rollback happens

For AI launches, include eval regression thresholds, failure sampling, and human review path.

### 5. Produce Go/No-Go Recommendation

End with one of:

- Go
- Go with mitigations
- Limited rollout
- Delay
- No-go

The recommendation must include reasoning and exact conditions required to change status.

### 6. Quality Gate

Read `references/checklists.md` before finalizing.

The launch review is not ready if:

- no owner is assigned to blockers
- rollback criteria are missing
- analytics are missing
- support impact is ignored
- risks are listed without mitigation
- go/no-go decision is vague

## Output Rules

- Use a concise executive status at the top.
- Use tables for readiness, blockers, and risks.
- Mark missing information explicitly.
- Do not say "ready" without evidence.
- If the launch is risky, recommend limited rollout or delay.

## References

- Read `references/templates.md` for readiness review formats.
- Read `references/checklists.md` before finalizing.
- Read `references/examples.md` for compact examples.
