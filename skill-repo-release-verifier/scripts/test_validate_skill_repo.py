#!/usr/bin/env python3
"""Fixture tests for the deterministic Skill repository validator."""

from __future__ import annotations

import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("validate_skill_repo.py")
SKILLS = (
    "alpha-discovery",
    "beta-decision",
    "gamma-design",
    "delta-engineering",
    "epsilon-evaluation",
    "zeta-release",
)
CATEGORIES = (
    "产品发现与研究",
    "产品定义与决策",
    "设计、原型与体验",
    "工程实现与代码质量",
    "AI 应用评测与质量",
    "发布、沟通与仓库治理",
)
HEADINGS = (
    "中文简介",
    "使用背景",
    "核心原则",
    "适用场景",
    "不适用场景",
    "输入要求",
    "信息不足时的处理",
    "工作流",
    "专业判断规则",
    "输出契约",
    "质量门槛",
    "常见失败与修正",
    "参考资料",
)


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_skill_repo", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load validate_skill_repo.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write_skill(root: Path, name: str) -> None:
    skill = root / name
    (skill / "agents").mkdir(parents=True)
    (skill / "references").mkdir()
    sections = "\n\n".join(f"## {heading}\n{name} {heading} 内容。" for heading in HEADINGS)
    (skill / "SKILL.md").write_text(
        "---\n"
        f"name: {name}\n"
        "description: Use when validating a fixture Skill repository.\n"
        "---\n\n"
        f"# {name}\n\n{sections}\n",
        encoding="utf-8",
    )
    (skill / "agents" / "openai.yaml").write_text(
        "interface:\n"
        f'  display_name: "{name} 测试"\n'
        '  short_description: "测试 Skill"\n'
        '  default_prompt: "验证测试仓库。"\n',
        encoding="utf-8",
    )
    for reference in ("usage-guide.zh.md", "templates.md", "checklists.md", "examples.md"):
        (skill / "references" / reference).write_text(
            f"# {name} {reference}\n\n有效的 fixture 内容。\n", encoding="utf-8"
        )


def write_catalog(root: Path, skills: tuple[str, ...] = SKILLS) -> None:
    catalog = root / "docs" / "skill-catalog.zh.md"
    catalog.parent.mkdir(parents=True, exist_ok=True)
    catalog.write_text(
        "# 中文目录\n\n" + "\n".join(f"- `{name}`" for name in skills) + "\n",
        encoding="utf-8",
    )


def write_readme(root: Path, skills: tuple[str, ...] = SKILLS) -> None:
    sections = []
    for category, name in zip(CATEGORIES, skills):
        sections.append(f"### {category}\n\n- `{name}`")
    (root / "README.md").write_text(
        "# Fixture Skill Repository\n\n"
        "[中文目录](docs/skill-catalog.zh.md)\n\n"
        + "\n\n".join(sections)
        + "\n",
        encoding="utf-8",
    )


def make_repository(root: Path) -> None:
    for name in SKILLS:
        write_skill(root, name)
    write_catalog(root)
    write_readme(root)


class ValidateSkillRepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.mkdtemp(prefix="skill-repo-validator-")
        self.root = Path(self.tempdir) / "repo"
        self.root.mkdir()
        make_repository(self.root)
        self.validator = load_validator()

    def tearDown(self) -> None:
        shutil.rmtree(self.tempdir)

    def codes(self):
        return {issue.code for issue in self.validator.validate_repository(self.root).issues}

    def append_readme(self, markdown: str) -> None:
        readme = self.root / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + f"\n{markdown}\n", encoding="utf-8")

    def run_cli(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT_PATH), str(self.root), *arguments],
            capture_output=True,
            text=True,
            check=False,
        )

    def json_output(self, completed: subprocess.CompletedProcess[str]) -> dict:
        if not completed.stdout.lstrip().startswith("{"):
            return {}
        return json.loads(completed.stdout)

    def commands_text(self) -> str:
        commands = SCRIPT_PATH.parent.parent / "references" / "commands.md"
        return commands.read_text(encoding="utf-8")

    def commands_block(self, heading: str) -> str:
        pattern = rf"^## {re.escape(heading)}\n.*?^```bash\n(.*?)^```"
        match = re.search(pattern, self.commands_text(), flags=re.MULTILINE | re.DOTALL)
        self.assertIsNotNone(match, f"Missing bash block for {heading}")
        return match.group(1)

    def test_missing_usage_guide_is_reported(self) -> None:
        (self.root / SKILLS[0] / "references" / "usage-guide.zh.md").unlink()
        self.assertIn("missing_required_file", self.codes())

    def test_readme_omission_is_reported(self) -> None:
        write_readme(self.root, SKILLS[:-1])
        self.assertIn("readme_skill_missing", self.codes())

    def test_duplicate_category_entry_is_reported(self) -> None:
        self.append_readme(f"- `{SKILLS[0]}`")
        self.assertIn("readme_skill_duplicate", self.codes())

    def test_missing_v2_heading_is_reported(self) -> None:
        skill = self.root / SKILLS[0] / "SKILL.md"
        skill.write_text(skill.read_text(encoding="utf-8").replace("## 输出契约\n", ""), encoding="utf-8")
        self.assertIn("missing_v2_heading", self.codes())

    def test_v2_heading_inside_fenced_code_is_still_missing(self) -> None:
        skill = self.root / SKILLS[0] / "SKILL.md"
        skill.write_text(
            skill.read_text(encoding="utf-8").replace(
                "## 输出契约\n",
                "```markdown\n## 输出契约\n```\n",
            ),
            encoding="utf-8",
        )
        self.assertIn("missing_v2_heading", self.codes())

    def test_broken_relative_markdown_link_is_reported(self) -> None:
        self.append_readme("[不存在](missing.md)")
        self.assertIn("broken_relative_link", self.codes())

    def test_expected_count_reports_too_few_skills(self) -> None:
        completed = self.run_cli("--expected-count", str(len(SKILLS) + 1), "--json")
        payload = self.json_output(completed)
        self.assertEqual(1, completed.returncode)
        self.assertIn("skill_count_mismatch", {issue.get("code") for issue in payload.get("issues", [])})

    def test_expected_count_reports_too_many_skills(self) -> None:
        completed = self.run_cli("--expected-count", str(len(SKILLS) - 1), "--json")
        payload = self.json_output(completed)
        self.assertEqual(1, completed.returncode)
        self.assertIn("skill_count_mismatch", {issue.get("code") for issue in payload.get("issues", [])})

    def test_cli_defaults_to_twenty_skills(self) -> None:
        completed = self.run_cli("--json")
        payload = self.json_output(completed)
        self.assertEqual(1, completed.returncode)
        self.assertEqual(20, payload.get("expected_skill_count"))
        self.assertIn("skill_count_mismatch", {issue.get("code") for issue in payload.get("issues", [])})

    def test_cli_expected_count_override_keeps_fixtures_generic(self) -> None:
        completed = self.run_cli("--expected-count", str(len(SKILLS)), "--json")
        payload = self.json_output(completed)
        self.assertEqual(0, completed.returncode)
        self.assertTrue(payload.get("passed"))
        self.assertEqual(len(SKILLS), payload.get("expected_skill_count"))

    def test_broken_anchor_is_reported(self) -> None:
        target = self.root / "docs" / "anchor-target.md"
        target.write_text("# Existing Heading\n", encoding="utf-8")
        self.append_readme("[坏锚点](docs/anchor-target.md#missing-heading)")
        self.assertIn("broken_anchor", self.codes())

    def test_broken_same_document_anchor_is_reported(self) -> None:
        self.append_readme("[坏锚点](#missing-heading)")
        self.assertIn("broken_anchor", self.codes())

    def test_reference_style_link_is_validated(self) -> None:
        self.append_readme("[指南][usage]\n\n[usage]: docs/missing-guide.md")
        self.assertIn("broken_relative_link", self.codes())

    def test_reference_style_image_is_validated(self) -> None:
        self.append_readme("![架构图][diagram]\n\n[diagram]: docs/missing-diagram.png")
        self.assertIn("broken_relative_link", self.codes())

    def test_missing_reference_definition_is_reported(self) -> None:
        self.append_readme("[指南][undefined-reference]")
        self.assertIn("missing_link_definition", self.codes())

    def test_reference_syntax_inside_inline_code_is_ignored(self) -> None:
        self.append_readme("证据标签示例：`[事实][S2][高]`。")
        result = self.validator.validate_repository(self.root)
        self.assertTrue(result.passed, result.issues)

    def test_links_and_references_inside_code_are_ignored(self) -> None:
        self.append_readme(
            "```markdown\n"
            "[坏链接](missing.md)\n"
            "[指南][manual]\n"
            "[manual]: missing-manual.md\n"
            "```\n"
            "`[内联](missing-inline.md)` `[手册][missing-reference]`"
        )
        result = self.validator.validate_repository(self.root)
        self.assertTrue(result.passed, result.issues)

    def test_reference_definition_inside_fence_is_not_visible(self) -> None:
        self.append_readme(
            "```markdown\n"
            "[manual]: docs/manual.md\n"
            "```\n"
            "[手册][manual]"
        )
        self.assertIn("missing_link_definition", self.codes())

    def test_shortcut_reference_is_validated_when_definition_exists(self) -> None:
        self.append_readme("[manual]\n\n[manual]: docs/missing-manual.md")
        self.assertIn("broken_relative_link", self.codes())

    def test_collapsed_reference_is_validated(self) -> None:
        self.append_readme("[manual][]\n\n[manual]: docs/missing-manual.md")
        self.assertIn("broken_relative_link", self.codes())

    def test_shortcut_parser_excludes_images_definitions_and_inline_links(self) -> None:
        self.append_readme(
            "![manual]\n"
            "[manual]: https://example.com/manual.png\n"
            "[内联](https://example.com/manual)"
        )
        result = self.validator.validate_repository(self.root)
        self.assertTrue(result.passed, result.issues)

    def test_percent_encoded_path_and_anchor_are_valid(self) -> None:
        target = self.root / "docs" / "usage guide.md"
        target.write_text("# Release Notes\n", encoding="utf-8")
        self.append_readme("[指南](docs/usage%20guide.md#release-notes)")
        result = self.validator.validate_repository(self.root)
        self.assertTrue(result.passed, result.issues)

    def test_existing_path_outside_repository_is_rejected(self) -> None:
        outside = Path(self.tempdir) / "outside.md"
        outside.write_text("# Outside\n", encoding="utf-8")
        self.append_readme("[越界](../outside.md)")
        self.assertIn("link_outside_repository", self.codes())

    def test_required_file_symlink_outside_repository_is_rejected(self) -> None:
        outside = Path(self.tempdir) / "outside-usage.md"
        outside.write_text("# Outside usage\n", encoding="utf-8")
        required = self.root / SKILLS[0] / "references" / "usage-guide.zh.md"
        required.unlink()
        required.symlink_to(outside)
        self.assertIn("path_outside_repository", self.codes())

    def test_broken_required_file_symlink_is_reported(self) -> None:
        required = self.root / SKILLS[0] / "references" / "usage-guide.zh.md"
        required.unlink()
        required.symlink_to("missing-usage.md")
        self.assertIn("broken_symlink", self.codes())

    def test_markdown_target_symlink_outside_repository_is_rejected(self) -> None:
        outside = Path(self.tempdir) / "outside-target.md"
        outside.write_text("# Outside target\n", encoding="utf-8")
        target = self.root / "docs" / "linked-outside.md"
        target.symlink_to(outside)
        self.append_readme("[越界目标](docs/linked-outside.md)")
        self.assertIn("path_outside_repository", self.codes())

    def test_broken_markdown_target_symlink_is_reported(self) -> None:
        target = self.root / "docs" / "broken-target.md"
        target.symlink_to("missing-target.md")
        self.append_readme("[坏软链接](docs/broken-target.md)")
        self.assertIn("broken_symlink", self.codes())

    def test_external_links_are_ignored(self) -> None:
        self.append_readme(
            "[网站](https://example.com/path#anchor)\n"
            "[邮件](mailto:owner@example.com)\n"
            "![远端图片](http://example.com/image.png)"
        )
        result = self.validator.validate_repository(self.root)
        self.assertTrue(result.passed, result.issues)

    def test_malformed_utf8_returns_json_issue_and_continues(self) -> None:
        malformed = self.root / SKILLS[0] / "references" / "examples.md"
        malformed.write_bytes(b"\xff\xfeinvalid")
        (self.root / SKILLS[1] / "references" / "usage-guide.zh.md").unlink()
        completed = self.run_cli("--expected-count", str(len(SKILLS)), "--json")
        payload = self.json_output(completed)
        issues = payload.get("issues", [])
        self.assertEqual(1, completed.returncode)
        self.assertNotIn("Traceback", completed.stderr)
        self.assertEqual(
            1,
            sum(
                issue.get("code") == "read_error" and issue.get("path") == f"{SKILLS[0]}/references/examples.md"
                for issue in issues
            ),
        )
        self.assertIn("missing_required_file", {issue.get("code") for issue in issues})

    def test_malformed_url_returns_stable_json_issue_and_continues(self) -> None:
        self.append_readme("[坏 URL](https://[invalid)")
        (self.root / SKILLS[1] / "references" / "usage-guide.zh.md").unlink()
        completed = self.run_cli("--expected-count", str(len(SKILLS)), "--json")
        payload = self.json_output(completed)
        issues = payload.get("issues", [])
        self.assertEqual(1, completed.returncode)
        self.assertNotIn("Traceback", completed.stderr)
        self.assertIn("invalid_link_target", {issue.get("code") for issue in issues})
        self.assertIn("missing_required_file", {issue.get("code") for issue in issues})

    def test_frontmatter_plain_name_allows_inline_comment(self) -> None:
        skill = self.root / SKILLS[0] / "SKILL.md"
        skill.write_text(
            skill.read_text(encoding="utf-8").replace(
                f"name: {SKILLS[0]}",
                f"name: {SKILLS[0]} # canonical directory name",
            ),
            encoding="utf-8",
        )
        result = self.validator.validate_repository(self.root)
        self.assertNotIn(
            "invalid_frontmatter",
            {issue.code for issue in result.issues},
        )
        self.assertNotIn(
            "frontmatter_name_mismatch",
            {issue.code for issue in result.issues},
        )

    def test_frontmatter_hash_inside_quotes_is_not_a_comment(self) -> None:
        skill = self.root / SKILLS[0] / "SKILL.md"
        skill.write_text(
            skill.read_text(encoding="utf-8").replace(
                f"name: {SKILLS[0]}",
                f'name: "{SKILLS[0]} # not a comment"',
            ),
            encoding="utf-8",
        )
        self.assertIn("frontmatter_name_mismatch", self.codes())

    def test_base64_command_is_gnu_and_bsd_portable(self) -> None:
        text = self.commands_text()
        self.assertIn('base64 < "$file" | tr -d \'\\n\'', text)
        self.assertNotIn('base64 -i "$file"', text)

    def test_inline_link_supports_balanced_parentheses_and_title(self) -> None:
        target = self.root / "docs" / "guide(v2).md"
        target.write_text("# Guide\n", encoding="utf-8")
        self.append_readme('[指南](docs/guide(v2).md "Guide title")')
        result = self.validator.validate_repository(self.root)
        self.assertTrue(result.passed, result.issues)

    def test_inline_link_supports_angle_target_and_title(self) -> None:
        target = self.root / "docs" / "guide v2.md"
        target.write_text("# Guide\n", encoding="utf-8")
        self.append_readme('[指南](<docs/guide v2.md> "Guide title")')
        result = self.validator.validate_repository(self.root)
        self.assertTrue(result.passed, result.issues)

    def test_contents_api_only_creates_on_404(self) -> None:
        text = self.commands_text()
        self.assertNotIn("2>/dev/null || true", text)
        self.assertIn('*"HTTP 404"*)', text)
        self.assertIn('*"HTTP 401"*|*"HTTP 403"*)', text)
        self.assertIn('cat "$contents_error" >&2', text)
        self.assertIn('exit "$contents_exit"', text)

    def test_recursive_tree_rejects_truncated_response_before_path_checks(self) -> None:
        text = self.commands_text()
        truncated_check = text.find("jq -e '.truncated == false'")
        path_extraction = text.find('[.tree[] | select(.type == "blob") | .path]')
        self.assertGreaterEqual(truncated_check, 0)
        self.assertGreater(path_extraction, truncated_check)

    def test_readme_category_scan_ignores_fenced_entries(self) -> None:
        write_readme(self.root, SKILLS[1:])
        self.append_readme(
            f"```markdown\n"
            f"### {CATEGORIES[0]}\n\n"
            f"- `{SKILLS[0]}`\n"
            f"```"
        )
        codes = self.codes()
        self.assertIn("readme_skill_missing", codes)
        self.assertIn("category_skill_missing", codes)

    def test_readme_coverage_ignores_inline_code_mentions(self) -> None:
        write_readme(self.root, SKILLS[1:])
        self.append_readme(f"示例命令可能输出 `{SKILLS[0]}`，但这不是目录条目。")
        codes = self.codes()
        self.assertIn("readme_skill_missing", codes)
        self.assertIn("category_skill_missing", codes)

    def test_contents_fallback_reads_only_candidate_commit_blobs(self) -> None:
        block = self.commands_block("GitHub Contents API 回退")
        self.assertIn('git diff --name-status -z --no-renames "$base_commit" "$candidate_commit"', block)
        self.assertIn('git show "$candidate_commit:$file"', block)
        self.assertIn('git rev-parse "$candidate_commit:$file"', block)
        self.assertNotIn('git hash-object "$file"', block)
        self.assertNotIn('base64 < "$file"', block)
        for status in ("A", "M", "D"):
            self.assertRegex(block, rf'["\']?{status}["\']?\)')

    def test_contents_fallback_does_not_swallow_invalid_base(self) -> None:
        block = self.commands_block("GitHub Contents API 回退")
        block = block.replace("base_commit=<approved-base-sha>", "base_commit=invalid-base")
        fake_bin = Path(self.tempdir) / "fake-bin"
        fake_bin.mkdir()
        fake_gh = fake_bin / "gh"
        fake_gh.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
        fake_gh.chmod(0o755)
        subprocess.run(
            ["git", "init", "-q"],
            cwd=self.root,
            check=True,
        )
        subprocess.run(
            ["git", "config", "user.email", "fixture@example.com"],
            cwd=self.root,
            check=True,
        )
        subprocess.run(
            ["git", "config", "user.name", "Fixture"],
            cwd=self.root,
            check=True,
        )
        subprocess.run(
            ["git", "add", "."],
            cwd=self.root,
            check=True,
        )
        subprocess.run(
            ["git", "commit", "-qm", "fixture"],
            cwd=self.root,
            check=True,
        )
        env = os.environ.copy()
        env["PATH"] = f"{fake_bin}{os.pathsep}{env['PATH']}"
        completed = subprocess.run(
            ["bash"],
            cwd=self.root,
            input=block,
            capture_output=True,
            text=True,
            env=env,
            check=False,
        )
        self.assertNotEqual(0, completed.returncode, completed.stdout + completed.stderr)
        self.assertIn("invalid-base", completed.stderr)

    def test_contents_fallback_verifies_complete_change_set(self) -> None:
        block = self.commands_block("GitHub Contents API 回退")
        self.assertIn("set -euo pipefail", block)
        diff = 'git diff --name-status -z --no-renames "$base_commit" "$candidate_commit"'
        self.assertIn(f'{diff} >"$change_list"', block)
        self.assertNotIn(f"{diff} |", block)
        truncated = block.find("jq -e '.truncated == false'")
        verification_loop = block.find('while IFS= read -r -d \'\' status && IFS= read -r -d \'\' file; do', truncated)
        self.assertGreaterEqual(truncated, 0)
        self.assertGreater(verification_loop, truncated)
        self.assertIn('candidate_blob=$(git rev-parse "$candidate_commit:$file")', block[verification_loop:])
        self.assertIn('remote_blob=$(jq -r --arg path "$file"', block[verification_loop:])
        self.assertIn('test "$remote_blob" = "$candidate_blob"', block[verification_loop:])
        self.assertIn('test "$remote_blob" = \'\'', block[verification_loop:])

    def test_contents_fallback_rejects_unsupported_git_modes(self) -> None:
        block = self.commands_block("GitHub Contents API 回退")
        self.assertIn('git ls-tree "$candidate_commit" -- "$file"', block)
        self.assertIn('candidate_mode', block)
        self.assertIn('candidate_type', block)
        self.assertIn('"100644"', block)
        self.assertIn('"blob"', block)
        self.assertIn('Use ordinary git push', block)
        self.assertIn('remote_mode=$(jq -r --arg path "$file"', block)
        self.assertIn('remote_type=$(jq -r --arg path "$file"', block)
        self.assertIn('test "$remote_mode" = "100644"', block)
        self.assertIn('test "$remote_type" = "blob"', block)

    def test_contents_fallback_stops_before_uploading_symlink(self) -> None:
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(
            ["git", "config", "user.email", "fixture@example.com"],
            cwd=self.root,
            check=True,
        )
        subprocess.run(
            ["git", "config", "user.name", "Fixture"],
            cwd=self.root,
            check=True,
        )
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "base"], cwd=self.root, check=True)
        base_commit = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        link = self.root / "release-link"
        link.symlink_to("README.md")
        subprocess.run(["git", "add", "release-link"], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "add symlink"], cwd=self.root, check=True)
        tree_entry = subprocess.run(
            ["git", "ls-tree", "HEAD", "--", "release-link"],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        self.assertTrue(tree_entry.startswith("120000 blob "), tree_entry)
        candidate_blob = tree_entry.split()[2]

        fake_bin = Path(self.tempdir) / "mode-fake-bin"
        fake_bin.mkdir()
        gh_log = Path(self.tempdir) / "gh.log"
        fake_gh = fake_bin / "gh"
        fake_gh.write_text(
            "#!/bin/sh\n"
            "case \"$*\" in\n"
            "  \"auth status\") exit 0 ;;\n"
            "  *\"git/trees/\"*)\n"
            "    printf '{\"truncated\":false,\"tree\":[{\"path\":\"release-link\",\"mode\":\"120000\",\"type\":\"blob\",\"sha\":\"%s\"}]}' \"$REMOTE_BLOB\"\n"
            "    ;;\n"
            "  *\"?ref=main\"*) printf 'gh: HTTP 404\\n' >&2; exit 1 ;;\n"
            "  *\"--method PUT\"*) printf 'PUT\\n' >>\"$GH_LOG\"; printf 'uploaded\\n' ;;\n"
            "  *) printf 'unexpected gh call: %s\\n' \"$*\" >&2; exit 2 ;;\n"
            "esac\n",
            encoding="utf-8",
        )
        fake_gh.chmod(0o755)
        fake_jq = fake_bin / "jq"
        fake_jq.write_text(
            "#!/bin/sh\n"
            "case \"$1:$2\" in\n"
            "  -n:*) printf '{}\\n' ;;\n"
            "  -e:*) exit 0 ;;\n"
            "  -r:.sha) printf 'null\\n' ;;\n"
            "  -r:--arg) printf '%s\\n' \"$REMOTE_BLOB\" ;;\n"
            "  *) printf '{}\\n' ;;\n"
            "esac\n",
            encoding="utf-8",
        )
        fake_jq.chmod(0o755)

        block = self.commands_block("GitHub Contents API 回退")
        block = block.replace("base_commit=<approved-base-sha>", f"base_commit={base_commit}")
        env = os.environ.copy()
        env["PATH"] = f"{fake_bin}{os.pathsep}{env['PATH']}"
        env["GH_LOG"] = str(gh_log)
        env["REMOTE_BLOB"] = candidate_blob
        completed = subprocess.run(
            ["bash"],
            cwd=self.root,
            input=block,
            capture_output=True,
            text=True,
            env=env,
            check=False,
        )
        self.assertNotEqual(0, completed.returncode, completed.stdout + completed.stderr)
        self.assertIn("120000", completed.stderr)
        self.assertIn("Use ordinary git push", completed.stderr)
        self.assertFalse(gh_log.exists(), gh_log.read_text(encoding="utf-8") if gh_log.exists() else "")

    def test_template_residue_is_reported(self) -> None:
        template = self.root / SKILLS[0] / "references" / "templates.md"
        template.write_text("# 模板\n\nTODO: Replace with the first main section.\n", encoding="utf-8")
        self.assertIn("template_residue", self.codes())

    def test_frontmatter_name_mismatch_is_reported(self) -> None:
        skill = self.root / SKILLS[0] / "SKILL.md"
        skill.write_text(skill.read_text(encoding="utf-8").replace(f"name: {SKILLS[0]}", "name: wrong-name"), encoding="utf-8")
        self.assertIn("frontmatter_name_mismatch", self.codes())

    def test_valid_repository_passes_without_issues(self) -> None:
        result = self.validator.validate_repository(self.root)
        self.assertTrue(result.passed)
        self.assertEqual([], result.issues)


if __name__ == "__main__":
    unittest.main()
