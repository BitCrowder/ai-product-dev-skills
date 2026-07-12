# PRD Templates

## Full PRD

```markdown
# PRD: [Product or Feature Name]

## Executive Summary
- Problem:
- Target user:
- Proposed solution:
- Business goal:
- Success metric:
- Recommended v1 scope:

## Context and Evidence
| Item | Evidence | Source | Confidence |
|---|---|---|---|
| | | | High/Medium/Low |

## Goals
| Goal | Why it matters | Metric |
|---|---|---|

## Non-Goals
| Non-goal | Why excluded |
|---|---|

## Users and Jobs
| User segment | Job-to-be-done | Current workaround | Pain |
|---|---|---|---|

## Problem Statement
[Who] needs [capability/outcome] because [pain/context]. Today they [workaround], which causes [cost/risk].

## Requirements
| ID | Requirement | Priority | Rationale | Acceptance Criteria |
|---|---|---|---|---|
| FR-1 | The user can... | Must | | Given/When/Then |

## Non-Functional Requirements
| Category | Requirement | Acceptance Criteria |
|---|---|---|
| Performance | | |
| Security/Privacy | | |
| Accessibility | | |
| Reliability | | |

## UX and Content Requirements
| Surface | Required states | Content notes |
|---|---|---|
| | Default, empty, loading, error, success | |

## Analytics
| Event or Metric | Definition | Trigger | Owner |
|---|---|---|---|

## Dependencies
| Dependency | Owner | Risk | Needed by |
|---|---|---|---|

## Risks and Mitigations
| Risk | Likelihood | Impact | Mitigation | Decision owner |
|---|---|---|---|---|

## Rollout Plan
- Internal test:
- Beta or limited release:
- General release:
- Rollback trigger:

## Open Questions
| Question | Why it matters | Owner | Needed by |
|---|---|---|---|
```

## Requirement Row Pattern

```markdown
| FR-[n] | The system must [observable behavior] when [condition]. | Must/Should/Could | [User/business reason] | Given [state], when [action], then [result]. |
```

## Success Metric Pattern

```markdown
| Metric | Baseline | Target | Measurement window | Instrumentation needed |
|---|---:|---:|---|---|
| Activation rate | Unknown | +10% relative | 14 days after launch | `feature_activated` event |
```
