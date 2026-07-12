# Issue-To-PR Examples

## Invocation

```text
Use $issue-to-pr to fix issue #42 where the dashboard crashes when the project has no activity.
```

## Output Skeleton

```markdown
## Issue Understanding
Dashboard assumes at least one activity item. Empty projects trigger an undefined access.

## Implementation Plan
| Area | Change | Risk |
|---|---|---|
| Activity query | Return empty array safely | Low |
| Dashboard component | Render empty state | Medium |
| Tests | Add empty-project regression | Low |

## Verification
| Command | Result |
|---|---|
| `npm test -- dashboard-empty-state` | Pass |

## PR Summary
Fixes #42 by rendering a stable empty state when a project has no activity.
```
