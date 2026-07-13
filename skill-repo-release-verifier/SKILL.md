---
name: skill-repo-release-verifier
description: Verify, commit, sync, and confirm publication of Codex skill repositories, especially multi-skill GitHub repositories. Use when the user asks to validate skills, avoid redoing manual checks, confirm all SKILL.md files pass quick_validate.py, check Chinese descriptions and catalog coverage, scan for template residue, commit changes, sync to GitHub with git push or GitHub Contents API fallback, and verify remote visibility, default branch, file count, and required files.
---

# Skill Repo Release Verifier

## 中文简介

**Skill 仓库发布验证器**：把 Skill 仓库发布前后的验证流程标准化，自动检查所有 Skill 是否有效、中文简介是否齐全、模板残留是否清理、GitHub 是否同步成功、远端文件树是否完整，避免每次都从头想验证步骤。

## Overview

Use this skill as the final release gate for a Codex skill repository. It turns the repeated manual verification flow into a checklist with exact commands and evidence to report.

This skill does not replace domain-specific skill creation. It verifies that a skill repository is structurally valid, discoverable, committed, synced, and visible on GitHub.

## Workflow

### 1. Identify Repository Context

Collect:

- local repository path
- GitHub repo owner/name
- expected default branch
- changed files or target skill folders
- whether Chinese descriptions and catalog are required
- whether normal `git push` is reliable

If the repo path is not provided, infer it from the current working directory.

### 2. Run Local Skill Validation

For every skill folder containing `SKILL.md`, run `quick_validate.py`.

Use the command pattern in `references/commands.md`. If `PyYAML` is missing, use the existing `/tmp/codex-skill-validate-deps` path or install `PyYAML` into a temporary target directory; do not add it to the repository.

### 3. Scan Repository Hygiene

Check:

- generated TODO/template residue
- every skill has `agents/openai.yaml`
- every skill has reference files when expected
- every skill has `中文简介` when the repo requires Chinese discoverability
- `docs/skill-catalog.zh.md` exists and covers all skills when Chinese discoverability is required
- `git status --short --branch` is understood before committing

### 4. Commit Intentionally

Commit only the intended release changes. Do not stage unrelated user work.

Use a clear commit message, such as:

- `Add Chinese skill descriptions`
- `Add expanded product and developer skills`
- `Add skill release verifier`

### 5. Sync to GitHub

Try normal `git push` when appropriate. If it hangs or fails due to network/TLS/HTTP transport issues, use GitHub Contents API fallback.

The fallback must:

- enumerate changed files from the commit
- compare local blob SHA with remote SHA
- skip files already synced
- include remote `sha` when updating existing files
- create missing files without `sha`
- report each uploaded path

Read `references/commands.md` for the exact API-safe loop.

### 6. Verify Remote State

Confirm:

- repo visibility
- default branch
- remote file tree count
- required files exist
- new or updated skill folders are present
- catalog exists if required

Use `references/checklists.md` before reporting completion.

## Output Contract

Always report:

- local validation command and result
- hygiene checks and counts
- commit SHA or commit message
- sync method used: git push or GitHub API fallback
- remote repo visibility and default branch
- remote file count and key paths verified
- any remaining risk or failed check

Do not claim completion until the remote verification command has succeeded.

## References

- Read `references/commands.md` for exact local validation and GitHub API fallback commands.
- Read `references/checklists.md` before finalizing.
- Read `references/examples.md` for the expected final report format.
