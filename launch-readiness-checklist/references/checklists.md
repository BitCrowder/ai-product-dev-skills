# Launch Readiness Checklist

## Product

- Scope matches approved requirements.
- Acceptance criteria are met.
- Known limitations are documented.
- User-facing copy is final.
- Onboarding or education is ready if needed.

## Engineering and QA

- Build passes.
- Relevant tests pass.
- Regression areas were checked.
- Feature flags or rollout controls are configured.
- Migration or compatibility concerns are addressed.
- Performance and reliability risks are understood.

## Data and AI

- Success metrics are defined.
- Analytics events are implemented or explicitly deferred.
- Dashboards or queries are ready.
- For AI features, eval thresholds are met.
- Monitoring covers failure categories that matter.

## Security, Privacy, Compliance

- Data handling is reviewed.
- Permissions and access control are checked.
- Legal or compliance review is complete when required.
- Sensitive logging is avoided.

## Support and Operations

- Support team knows what is changing.
- FAQ or macros are ready when needed.
- Escalation path is named.
- Incident owner is assigned.

## Communications

- Release notes are ready.
- Internal announcement is ready.
- Customer communication is ready if applicable.
- Status page or changelog plan exists when relevant.

## Go/No-Go Red Flags

- No rollback plan.
- No owner for a blocker.
- No success metric.
- No support path for affected users.
- Known severe bug without mitigation.
- Monitoring cannot detect the most important failure.
