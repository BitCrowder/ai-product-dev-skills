# Launch Readiness Examples

## Invocation

```text
Use $launch-readiness-checklist to assess whether our AI support chatbot can launch to 10% of customers next week.
```

## Output Skeleton

```markdown
# Launch Readiness Review: AI Support Chatbot 10% Rollout

## Executive Status
- Recommendation: Limited rollout
- Highest risk: Incorrect policy answers during missing-context cases
- Required condition: Eval groundedness >= 95% and support escalation macro ready

## Blockers
| Blocker | Impact | Owner | Required resolution |
|---|---|---|---|
| No support escalation macro | Support cannot handle bad answer reports consistently | Support lead | Publish macro before rollout |

## Monitoring Plan
| Signal | Threshold | Action |
|---|---|---|
| Unsupported answer reports | > 3 in 24h | Pause rollout and review traces |
```
