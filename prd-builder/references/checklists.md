# PRD Quality Checklist

## Completeness

- The target user or segment is named.
- The user problem is stated without solution bias.
- The business or product goal is explicit.
- The primary success metric is measurable.
- Non-goals are listed.
- Requirements are prioritized.
- Requirements are testable.
- Acceptance criteria cover happy, empty, error, and edge states where relevant.
- Dependencies and owners are identified.
- Risks and mitigations are included.
- Open questions are separated from requirements.

## Red Flags

- Requirements use vague words such as better, seamless, powerful, robust, or intuitive without test criteria.
- The PRD includes every requested idea in v1.
- The PRD hides assumptions as facts.
- The PRD has metrics without instrumentation.
- The PRD lacks rollback, migration, or support considerations for a launchable feature.

## Final Review Questions

1. Could an engineer estimate this without another meeting?
2. Could QA write tests from the acceptance criteria?
3. Could data verify whether the feature worked?
4. Could design identify the required screens and states?
5. Could leadership see why this is worth doing now?
