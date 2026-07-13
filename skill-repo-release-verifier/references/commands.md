# Verification Commands

Use these commands from the repository root. Replace `OWNER/REPO` and paths as needed.

## Validate Every Skill

```bash
set -e
for d in */SKILL.md; do
  s=${d%/SKILL.md}
  echo "== $s =="
  PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$PWD/$s"
done
```

If `PyYAML` is missing:

```bash
python3 -m pip install --quiet --target /tmp/codex-skill-validate-deps PyYAML
```

## Scan Template Residue

```bash
rg -n "\\[TODO|Complete and informative|Structuring This Skill|Replace with the first main section" . \
  -g '!skill-repo-release-verifier/references/commands.md' || true
```

## Check Chinese Description Coverage

```bash
local_count=$(rg -n "^## 中文简介$" */SKILL.md | wc -l | tr -d ' ')
skill_count=$(find . -maxdepth 2 -name SKILL.md | wc -l | tr -d ' ')
echo "中文简介: $local_count / Skill: $skill_count"
test "$local_count" = "$skill_count"
test -f docs/skill-catalog.zh.md
```

## Commit

```bash
git status --short
git add <intended files>
git commit -m "<message>"
```

## GitHub API Fallback Sync

Use this when `git push` hangs or fails. It uploads files changed in the latest commit, skipping files already identical on `main`.

```bash
set -e
repo='OWNER/REPO'
base="$PWD"
git show --name-only --format='' HEAD | while IFS= read -r file; do
  [ -z "$file" ] && continue
  local_sha=$(git hash-object "$file")
  existing_sha=$(gh api "repos/$repo/contents/$file?ref=main" --jq '.sha' 2>/dev/null || true)
  if [ "$existing_sha" = "$local_sha" ]; then
    echo "skip $file"
    continue
  fi
  content=$(base64 -i "$base/$file" | tr -d '\n')
  if [ -n "$existing_sha" ] && [ "$existing_sha" != "null" ]; then
    jq -n --arg message "Update $file" --arg content "$content" --arg sha "$existing_sha" \
      '{message:$message, content:$content, sha:$sha}' > /tmp/gh-content-update.json
  else
    jq -n --arg message "Add $file" --arg content "$content" \
      '{message:$message, content:$content}' > /tmp/gh-content-update.json
  fi
  gh api "repos/$repo/contents/$file" --method PUT --input /tmp/gh-content-update.json --jq '.content.path'
done
```

## Verify Remote

```bash
gh repo view OWNER/REPO --json nameWithOwner,visibility,url,defaultBranchRef \
  --jq '.nameWithOwner + " " + .visibility + " " + .defaultBranchRef.name + " " + .url'

gh api 'repos/OWNER/REPO/git/trees/main?recursive=1' \
  --jq '[.tree[] | select(.type=="blob") | .path] | {count:length, hasCatalog: any(. == "docs/skill-catalog.zh.md")}'
```
