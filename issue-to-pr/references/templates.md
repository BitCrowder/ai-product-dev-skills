# Issue-To-PR Templates

## Issue Triage

```markdown
## Issue Understanding
- Source:
- Type:
- Expected behavior:
- Actual behavior:
- Affected scope:
- Acceptance criteria:
- Unknowns:

## Reproduction or Confirmation
| Step | Result | Evidence |
|---|---|---|

## Implementation Plan
| Area/File | Change | Reason | Risk |
|---|---|---|---|

## Test Plan
| Test | Purpose | Command |
|---|---|---|
```

## PR Description

```markdown
## Summary
- [What changed]
- [Why it changed]

## Linked Issue
Closes #[issue-number]

## Changes
| Area | Change |
|---|---|

## Verification
| Command or Check | Result |
|---|---|

## Risk and Rollout
- Risk:
- Rollback:
- Follow-up:
```

Use `Fixes #123`, `Closes #123`, or `Resolves #123` only when the PR should automatically close the GitHub issue after merge. Use `Refs #123` when the PR is related but should not close it.

## Commit Message Pattern

```text
fix: handle empty search results
feat: add team invite acceptance flow
test: cover transcript parser edge cases
docs: clarify setup for local evals
```
