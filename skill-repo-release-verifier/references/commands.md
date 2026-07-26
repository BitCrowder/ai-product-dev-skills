# 发布验证命令

从仓库根目录执行。所有 `<...>` 都是运行前确认的值，不要在不知道远端或分支时替换猜测值。

## 本地预检与确定性验证

```bash
set -e
repo_root=$(git rev-parse --show-toplevel)
git -C "$repo_root" status --short --branch
git -C "$repo_root" remote -v
python3 skill-repo-release-verifier/scripts/validate_skill_repo.py "$repo_root" --expected-count 20
python3 skill-repo-release-verifier/scripts/validate_skill_repo.py "$repo_root" --expected-count 20 --json
git -C "$repo_root" diff --check
```

脚本失败时先修复其 `path`、`code`、`message`，不要继续发布。JSON 适合保存到 CI 或发布记录；默认输出适合人工阅读。

## 逐 Skill 结构校验

```bash
set -e
for skill_file in */SKILL.md; do
  skill_directory=${skill_file%/SKILL.md}
  PYTHONPATH=/tmp/codex-skill-validate-deps \
    python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
    "$skill_directory"
done
```

若环境缺少 PyYAML，只在临时目录安装：

```bash
python3 -m pip install --quiet --target /tmp/codex-skill-validate-deps PyYAML
```

## 审计提交范围并提交

```bash
set -e
base_commit=<approved-base-sha>
git diff --check "$base_commit" HEAD
git diff --name-only "$base_commit" HEAD
git status --short
git add <approved-path-1> <approved-path-2>
git diff --cached --check
git diff --cached --name-only
git commit -m "<approved-message>"
candidate_commit=$(git rev-parse HEAD)
git show --stat --oneline "$candidate_commit"
```

看到无关改动时不执行 `git add .`，也不要还原该改动；把路径列为阻断项并请求 owner 决定。

## 普通 Push 与分支 SHA 核验

```bash
set -e
repo='OWNER/REPO'
branch='main'
candidate_commit=$(git rev-parse HEAD)
git push origin "HEAD:$branch"
remote_sha=$(gh api "repos/$repo/git/ref/heads/$branch" --jq '.object.sha')
test "$remote_sha" = "$candidate_commit" || {
  printf 'remote branch SHA differs: local=%s remote=%s\n' "$candidate_commit" "$remote_sha" >&2
  exit 1
}
```

若命令失败，保留退出码和原始错误。`git push` 成功后仍须完成下方默认分支和文件树核验。

## GitHub Contents API 回退

只在普通 push 已失败、`gh auth status` 成功且目标默认分支已确认时使用。它按文件更新，可能产生多个远端提交，所以最终以远端树为准。

```bash
set -euo pipefail
repo='OWNER/REPO'
branch='main'
base_commit=<approved-base-sha>
candidate_commit=$(git rev-parse HEAD)
temp_root=$(mktemp -d "${TMPDIR:-/tmp}/skill-repo-fallback.XXXXXX")
change_list="$temp_root/changes.nul"
contents_json="$temp_root/contents.json"
contents_error="$temp_root/contents-error.txt"
payload="$temp_root/payload.json"
tree_response="$temp_root/tree-response.json"
cleanup() {
  rm -rf "$temp_root"
}
trap cleanup EXIT INT TERM

git cat-file -e "${base_commit}^{commit}"
git cat-file -e "${candidate_commit}^{commit}"
gh auth status

# Write the complete candidate change set before entering a loop. A bad base
# therefore stops here instead of being hidden by a pipeline or subshell.
git diff --name-status -z --no-renames "$base_commit" "$candidate_commit" >"$change_list"

read_remote_contents() {
  file=$1
  if gh api "repos/$repo/contents/$file?ref=$branch" >"$contents_json" 2>"$contents_error"; then
    remote_sha=$(jq -r '.sha' "$contents_json")
  else
    contents_exit=$?
    contents_message=$(cat "$contents_error")
    case "$contents_message" in
      *"HTTP 404"*)
        remote_sha=''
        ;;
      *"HTTP 401"*|*"HTTP 403"*)
        printf 'Contents API authentication/authorization failure for %s:\n' "$file" >&2
        cat "$contents_error" >&2
        exit "$contents_exit"
        ;;
      *)
        printf 'Contents API transport or unexpected failure for %s:\n' "$file" >&2
        cat "$contents_error" >&2
        exit "$contents_exit"
        ;;
    esac
  fi
}

while IFS= read -r -d '' status && IFS= read -r -d '' file; do
  case "$status" in
    A)
      operation='Add'
      ;;
    M)
      operation='Update'
      ;;
    D)
      read_remote_contents "$file"
      if [ -z "$remote_sha" ] || [ "$remote_sha" = 'null' ]; then
        printf 'skip absent %s\n' "$file"
        continue
      fi
      jq -n --arg message "Delete $file" --arg sha "$remote_sha" --arg branch "$branch" \
        '{message:$message, sha:$sha, branch:$branch}' >"$payload"
      delete_commit=$(gh api "repos/$repo/contents/$file" --method DELETE --input "$payload" \
        --jq '.commit.sha')
      printf '%s %s\n' "$file" "$delete_commit"
      continue
      ;;
    *)
      printf 'Unsupported candidate change status %s for %s; stopping.\n' "$status" "$file" >&2
      exit 1
      ;;
  esac

  candidate_entry=$(git ls-tree "$candidate_commit" -- "$file")
  candidate_mode=${candidate_entry%% *}
  candidate_remainder=${candidate_entry#* }
  candidate_type=${candidate_remainder%% *}
  if [ -z "$candidate_entry" ] || [ "$candidate_mode" != "100644" ] || [ "$candidate_type" != "blob" ]; then
    printf 'Unsupported Git mode/type for Contents API fallback: path=%s mode=%s type=%s. Use ordinary git push to preserve Git metadata.\n' \
      "$file" "${candidate_mode:-missing}" "${candidate_type:-missing}" >&2
    exit 1
  fi
  candidate_blob=$(git rev-parse "$candidate_commit:$file")
  read_remote_contents "$file"
  if [ "$candidate_blob" = "$remote_sha" ]; then
    printf 'skip identical %s\n' "$file"
    continue
  fi
  content=$(git show "$candidate_commit:$file" | base64 | tr -d '\n')
  if [ -n "$remote_sha" ] && [ "$remote_sha" != 'null' ]; then
    jq -n --arg message "Update $file" --arg content "$content" \
      --arg sha "$remote_sha" --arg branch "$branch" \
      '{message:$message, content:$content, sha:$sha, branch:$branch}' >"$payload"
  else
    jq -n --arg message "$operation $file" --arg content "$content" --arg branch "$branch" \
      '{message:$message, content:$content, branch:$branch}' >"$payload"
  fi
  gh api "repos/$repo/contents/$file" --method PUT --input "$payload" \
    --jq '.content.path + " " + .commit.sha'
done <"$change_list"

gh api "repos/$repo/git/trees/$branch?recursive=1" >"$tree_response"
if ! jq -e '.truncated == false' "$tree_response" >/dev/null; then
  printf 'Remote recursive tree is truncated; candidate completeness cannot be verified.\n' >&2
  jq '{truncated, sha}' "$tree_response" >&2
  exit 1
fi

while IFS= read -r -d '' status && IFS= read -r -d '' file; do
  remote_path=$(jq -r --arg path "$file" \
    '[.tree[] | select(.path == $path)][0].path // ""' \
    "$tree_response")
  remote_mode=$(jq -r --arg path "$file" \
    '[.tree[] | select(.path == $path)][0].mode // ""' \
    "$tree_response")
  remote_type=$(jq -r --arg path "$file" \
    '[.tree[] | select(.path == $path)][0].type // ""' \
    "$tree_response")
  remote_blob=$(jq -r --arg path "$file" \
    '[.tree[] | select(.path == $path)][0].sha // ""' \
    "$tree_response")
  case "$status" in
    A|M)
      candidate_blob=$(git rev-parse "$candidate_commit:$file")
      test "$remote_mode" = "100644" &&
        test "$remote_type" = "blob" &&
        test "$remote_blob" = "$candidate_blob" || {
        printf 'remote file mismatch: path=%s mode=%s type=%s candidate=%s remote=%s\n' \
          "$file" "$remote_mode" "$remote_type" "$candidate_blob" "$remote_blob" >&2
        exit 1
      }
      ;;
    D)
      test "$remote_path" = '' &&
        test "$remote_blob" = '' || {
        printf 'deleted path still exists remotely: path=%s mode=%s type=%s remote=%s\n' \
          "$file" "$remote_mode" "$remote_type" "$remote_blob" >&2
        exit 1
      }
      ;;
    *)
      printf 'Unsupported candidate change status %s for %s; stopping.\n' "$status" "$file" >&2
      exit 1
      ;;
  esac
done <"$change_list"
```

`--no-renames` 把 rename 表示为删除加新增，因此 A/M/D 都绑定到固定 `candidate_commit`：内容来自 `git show "$candidate_commit:$file"`，候选 blob SHA 来自 `git rev-parse "$candidate_commit:$file"`，不会读取工作区当前文件。Contents API 不能可靠保留 Git mode，所以 A/M 只允许 `100644 blob`；`120000` symlink、`100755` executable、`160000 commit` submodule 和其他 mode/type 必须停止并建议普通 `git push`。远端树也必须逐项返回 `100644 blob` 和相同 SHA，D 则不能留下任何同 path 条目。可移植的单文件 base64 形式仍是 `base64 < "$file" | tr -d '\n'`，但回退流程不得使用它读取工作区。分支保护或并发更新会安全停止；不要把 Contents API 回退误报为完整 Git 历史同步。

## 默认分支、SHA 与文件树核验

```bash
set -e
repo='OWNER/REPO'
expected_branch='main'
gh repo view "$repo" --json nameWithOwner,visibility,url,defaultBranchRef
actual_branch=$(gh api "repos/$repo" --jq '.default_branch')
test "$actual_branch" = "$expected_branch"
remote_sha=$(gh api "repos/$repo/git/ref/heads/$actual_branch" --jq '.object.sha')
printf 'remote branch=%s sha=%s\n' "$actual_branch" "$remote_sha"
gh api "repos/$repo/git/trees/$actual_branch?recursive=1" >/tmp/skill-repo-tree-response.json
if ! jq -e '.truncated == false' /tmp/skill-repo-tree-response.json >/dev/null; then
  printf 'Remote recursive tree is truncated; completeness cannot be verified.\n' >&2
  jq '{truncated, sha}' /tmp/skill-repo-tree-response.json >&2
  exit 1
fi
jq '[.tree[] | select(.type == "blob") | .path] | {count:length, paths:.}' \
  /tmp/skill-repo-tree-response.json >/tmp/skill-repo-tree.json
jq -e '.paths | index("README.md") and index("docs/skill-catalog.zh.md") and index("docs/validation/skill-v2-validation-report.md") and index("skill-repo-release-verifier/SKILL.md")' /tmp/skill-repo-tree.json
```

只有 Contents API 明确返回 `HTTP 404` 才把文件视为不存在并进入 create；`401`、`403`、超时、DNS/TLS 或其他错误都必须保留原始 stderr 并停止。递归树只有在 `.truncated == false` 后才能用于完整性结论；否则报告“树被截断，未验证完整”，不得声明远端文件树完整。
