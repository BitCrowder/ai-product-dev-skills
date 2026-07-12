# AI Eval Checklist

## Eval Design

- The eval objective maps to a product or release decision.
- Quality dimensions are decomposed and observable.
- Dataset schema is defined.
- Dataset slices cover happy path, edge cases, adversarial cases, and production failures.
- Each case has expected behavior or rubric.
- Graders have thresholds.
- Automated checks and human review are separated.
- Failure taxonomy maps to remediation.
- Regression workflow names baseline and candidate.

## RAG-Specific Checks

- Retrieval relevance is measured separately from answer quality.
- Citation accuracy is checked.
- Unsupported claims are counted.
- Missing-context behavior is tested.

## Agent-Specific Checks

- Tool selection is evaluated.
- Tool arguments are evaluated.
- Step count, loops, latency, and cost are tracked.
- Unsafe or unauthorized tool use is tested.

## Red Flags

- The plan only asks humans "is this good?"
- The dataset has only happy paths.
- The rubric is subjective without examples.
- The eval has no release threshold.
- Failures cannot be traced to likely fixes.
