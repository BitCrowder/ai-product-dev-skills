# Release Verification Checklist

## Local Validation

- Every folder with `SKILL.md` passes `quick_validate.py`.
- `SKILL.md` frontmatter contains only `name` and `description`.
- No generated TODO/template residue remains.
- Expected `agents/openai.yaml` files exist.
- Expected reference files exist.
- Chinese discoverability requirements are satisfied when required.

## Git Hygiene

- `git status --short --branch` is inspected.
- Only intended files are staged.
- Commit message describes the change.
- Unrelated user changes are not reverted.

## GitHub Sync

- Normal push succeeded, or API fallback uploaded the changed files.
- API fallback used `sha` for existing files and no `sha` for new files.
- Files already identical on remote were skipped where possible.

## Remote Verification

- Repository is the expected `OWNER/REPO`.
- Visibility is correct.
- Default branch is correct.
- Remote file tree includes new or updated skill files.
- Remote file count is plausible.
- Required catalog or docs files exist.

## Final Report

- Include validation evidence.
- Include sync method.
- Include remote verification evidence.
- Include unresolved risks, if any.
