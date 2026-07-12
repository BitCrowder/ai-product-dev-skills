# Issue-To-PR Checklist

## Before Editing

- Repository and target branch are known.
- Issue intent is understood.
- Acceptance criteria are explicit or assumptions are labeled.
- Reproduction steps exist for bugs when feasible.
- Likely files and risks are identified.
- Unrelated changes are avoided.

## Before PR

- Relevant tests were added or updated.
- Verification commands were run.
- Original issue is addressed.
- Edge cases are covered.
- PR body explains what changed and why.
- PR references or closes the issue correctly.
- Risk and rollback notes are included.

## Red Flags

- Code changes start before understanding the issue.
- No regression test for a bug fix.
- Broad refactors mixed with feature work.
- PR description says "minor changes" without evidence.
- Verification is described as "should work" instead of command output.
