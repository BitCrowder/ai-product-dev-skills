#!/usr/bin/env python3
"""Deterministically validate a V2 Codex Skill repository using only stdlib."""

from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlsplit


V2_HEADINGS = (
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
README_CATEGORIES = (
    "产品发现与研究",
    "产品定义与决策",
    "设计、原型与体验",
    "工程实现与代码质量",
    "AI 应用评测与质量",
    "发布、沟通与仓库治理",
)
COMMON_REQUIRED_FILES = (
    "agents/openai.yaml",
    "references/usage-guide.zh.md",
    "references/checklists.md",
    "references/examples.md",
)
RESIDUE_PATTERNS = (
    re.compile(r"^\s*(?:TODO|TBD|FIXME)\s*:\s*(?:replace|fill|complete|add)\b", re.IGNORECASE),
    re.compile(r"\bReplace with the first main section\b", re.IGNORECASE),
    re.compile(r"^\s*\[(?:TODO|TBD|INSERT|YOUR [^\]]+)\]\s*$", re.IGNORECASE),
    re.compile(r"待办占位|未决占位|补充相关内容|在此填写|示例内容"),
)
INLINE_LINK_START = re.compile(r"!?\[[^\]\n]*\]\(")
REFERENCE_DEFINITION = re.compile(r"^\s{0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)")
REFERENCE_USE = re.compile(r"!?\[([^\]]+)\]\[([^\]]*)\]")
SHORTCUT_REFERENCE = re.compile(r"(?<!!)\[([^\]\n]+)\]")
MARKDOWN_HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")
INLINE_CODE = re.compile(r"(`+).*?\1")


@dataclass(frozen=True)
class Issue:
    path: str
    code: str
    message: str


@dataclass(frozen=True)
class ValidationResult:
    root: str
    skill_count: int
    expected_skill_count: int | None
    issues: list[Issue]

    @property
    def passed(self) -> bool:
        return not self.issues

    def as_dict(self) -> dict[str, object]:
        return {
            "passed": self.passed,
            "root": self.root,
            "skill_count": self.skill_count,
            "expected_skill_count": self.expected_skill_count,
            "issues": [asdict(issue) for issue in self.issues],
        }


class Validator:
    def __init__(self, root: Path, expected_count: int | None) -> None:
        self.root = root.resolve()
        self.expected_count = expected_count
        self.issues: list[Issue] = []
        self._text_cache: dict[Path, str | None] = {}
        self._issue_keys: set[tuple[str, str, str]] = set()

    def display_path(self, path: Path) -> str:
        path = lexical_absolute(path)
        try:
            return path.relative_to(self.root).as_posix()
        except ValueError:
            return path.as_posix()

    def add_issue(self, path: Path, code: str, message: str) -> None:
        issue = Issue(self.display_path(path), code, message)
        key = (issue.path, issue.code, issue.message)
        if key not in self._issue_keys:
            self._issue_keys.add(key)
            self.issues.append(issue)

    def repository_path_problem(self, path: Path) -> tuple[str, str] | None:
        path = lexical_absolute(path)
        try:
            relative = path.relative_to(self.root)
        except ValueError:
            return "path_outside_repository", "Path is outside the repository root."
        cursor = self.root
        for part in relative.parts:
            cursor = cursor / part
            if not cursor.is_symlink():
                continue
            try:
                target = cursor.resolve(strict=True)
            except (OSError, RuntimeError):
                return "broken_symlink", "Path contains a broken symlink."
            try:
                target.relative_to(self.root)
            except ValueError:
                return (
                    "path_outside_repository",
                    "Path contains a symlink that resolves outside the repository root.",
                )
        return None

    def read_text(self, path: Path) -> str | None:
        path = lexical_absolute(path)
        if path in self._text_cache:
            return self._text_cache[path]
        problem = self.repository_path_problem(path)
        if problem is not None:
            self.add_issue(path, *problem)
            self._text_cache[path] = None
            return None
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeError:
            self.add_issue(path, "read_error", "File is not valid UTF-8.")
            text = None
        except OSError:
            self.add_issue(path, "read_error", "Unable to read file.")
            text = None
        self._text_cache[path] = text
        return text

    def skill_directories(self) -> list[Path]:
        try:
            children = list(self.root.iterdir())
        except OSError:
            self.add_issue(self.root, "read_error", "Unable to list repository root.")
            return []
        return sorted(
            (path for path in children if path.is_dir() and (path / "SKILL.md").is_file()),
            key=lambda path: path.name,
        )

    def markdown_files(self) -> list[Path]:
        try:
            return sorted(
                path
                for path in self.root.rglob("*.md")
                if ".git" not in path.parts and ".superpowers" not in path.parts
            )
        except OSError:
            self.add_issue(self.root, "read_error", "Unable to enumerate Markdown files.")
            return []

    def validate_skill(self, skill: Path) -> None:
        skill_file = skill / "SKILL.md"
        text = self.read_text(skill_file)
        if text is not None:
            name = frontmatter_name(text)
            if name is None:
                self.add_issue(
                    skill_file,
                    "invalid_frontmatter",
                    "SKILL.md must include frontmatter with a readable name field.",
                )
            elif name != skill.name:
                self.add_issue(
                    skill_file,
                    "frontmatter_name_mismatch",
                    f"Frontmatter name '{name}' does not match directory '{skill.name}'.",
                )

            headings = h2_headings(text)
            missing = [heading for heading in V2_HEADINGS if heading not in headings]
            for heading in missing:
                self.add_issue(
                    skill_file,
                    "missing_v2_heading",
                    f"Required V2 heading '{heading}' is missing.",
                )
            present_in_order = [heading for heading in headings if heading in V2_HEADINGS]
            if not missing and present_in_order != list(V2_HEADINGS):
                self.add_issue(
                    skill_file,
                    "v2_heading_order",
                    "The 13 required V2 headings must appear once and in the required order.",
                )

        for required in required_files_for(skill):
            required_path = skill / required
            problem = self.repository_path_problem(required_path)
            if problem is not None:
                self.add_issue(required_path, *problem)
                continue
            if not required_path.is_file():
                self.add_issue(required_path, "missing_required_file", "Required V2 file is missing.")

        try:
            markdown_files = sorted(skill.rglob("*.md"))
        except OSError:
            self.add_issue(skill, "read_error", "Unable to enumerate Skill Markdown files.")
            return
        for markdown in markdown_files:
            markdown_text = self.read_text(markdown)
            if markdown_text is None:
                continue
            for line_number, line in non_fenced_lines(markdown_text):
                if any(pattern.search(line) for pattern in RESIDUE_PATTERNS):
                    self.add_issue(
                        markdown,
                        "template_residue",
                        f"Possible unfilled template residue at line {line_number}.",
                    )

    def validate_navigation(self, skills: list[Path]) -> None:
        expected = {skill.name for skill in skills}
        readme_path = self.root / "README.md"
        catalog_path = self.root / "docs" / "skill-catalog.zh.md"
        if not readme_path.is_file():
            self.add_issue(readme_path, "missing_readme", "README.md is required.")
            return
        readme = self.read_text(readme_path)
        if readme is None:
            return
        categories = extract_category_entries(readme)
        for category, entries in categories.items():
            if not entries:
                self.add_issue(
                    readme_path,
                    "empty_readme_category",
                    f"Category '{category}' has no Skill entries.",
                )
        all_entries = [entry for category in README_CATEGORIES for entry in categories[category]]
        for skill in sorted(expected):
            count = all_entries.count(skill)
            if count == 0:
                self.add_issue(
                    readme_path,
                    "readme_skill_missing",
                    f"README does not cover '{skill}'.",
                )
                self.add_issue(
                    readme_path,
                    "category_skill_missing",
                    f"'{skill}' is missing from the six README categories.",
                )
            elif count > 1:
                self.add_issue(
                    readme_path,
                    "readme_skill_duplicate",
                    f"'{skill}' appears {count} times across the six README categories.",
                )
        for entry in sorted(set(all_entries) - expected):
            self.add_issue(
                readme_path,
                "category_unknown_skill",
                f"Category entry '{entry}' has no Skill directory.",
            )

        if not catalog_path.is_file():
            self.add_issue(catalog_path, "missing_catalog", "docs/skill-catalog.zh.md is required.")
            return
        catalog = self.read_text(catalog_path)
        if catalog is None:
            return
        for skill in sorted(expected):
            if f"`{skill}`" not in catalog:
                self.add_issue(
                    catalog_path,
                    "catalog_skill_missing",
                    f"Chinese catalog does not cover '{skill}'.",
                )

    def validate_link_target(
        self,
        source: Path,
        raw_target: str,
        line_number: int,
    ) -> None:
        try:
            target = parse_link_target(raw_target)
        except ValueError:
            self.add_issue(
                source,
                "invalid_link_target",
                f"Link target '{raw_target}' is malformed (line {line_number}).",
            )
            return
        if target is None:
            return
        decoded_path, fragment = target
        lexical_target = lexical_absolute(source if not decoded_path else source.parent / decoded_path)
        try:
            lexical_target.relative_to(self.root)
        except ValueError:
            self.add_issue(
                source,
                "link_outside_repository",
                f"Relative link '{raw_target}' escapes the repository root (line {line_number}).",
            )
            return
        problem = self.repository_path_problem(lexical_target)
        if problem is not None:
            code, _ = problem
            message = (
                f"Relative link '{raw_target}' contains a broken symlink (line {line_number})."
                if code == "broken_symlink"
                else f"Relative link '{raw_target}' resolves outside the repository root via symlink "
                f"(line {line_number})."
            )
            self.add_issue(source, code, message)
            return
        resolved = lexical_target.resolve()
        if not resolved.exists():
            self.add_issue(
                source,
                "broken_relative_link",
                f"Relative link '{decoded_path}' does not exist (line {line_number}).",
            )
            return
        if fragment:
            target_text = self.read_text(resolved)
            if target_text is None:
                return
            anchors = heading_anchors(target_text)
            if fragment not in anchors:
                self.add_issue(
                    source,
                    "broken_anchor",
                    f"Anchor '#{fragment}' does not exist in '{self.display_path(resolved)}' (line {line_number}).",
                )

    def validate_links(self) -> None:
        for markdown in self.markdown_files():
            text = self.read_text(markdown)
            if text is None:
                continue
            lines = list(non_fenced_lines(text))
            definitions: dict[str, tuple[str, int]] = {}
            for line_number, line in lines:
                definition = REFERENCE_DEFINITION.match(strip_inline_code(line))
                if definition:
                    definitions[normalize_reference_label(definition.group(1))] = (
                        definition.group(2),
                        line_number,
                    )

            for line_number, line in lines:
                parsed_line = strip_inline_code(line)
                if REFERENCE_DEFINITION.match(parsed_line):
                    continue
                inline_links = parse_inline_links(parsed_line)
                for target, _, _ in inline_links:
                    self.validate_link_target(markdown, target, line_number)
                masked_line = mask_spans(
                    parsed_line,
                    [(start, end) for _, start, end in inline_links],
                )
                references = list(REFERENCE_USE.finditer(masked_line))
                for reference in references:
                    label = reference.group(2) or reference.group(1)
                    normalized = normalize_reference_label(label)
                    definition = definitions.get(normalized)
                    if definition is None:
                        self.add_issue(
                            markdown,
                            "missing_link_definition",
                            f"Reference link definition '[{label}]' is missing (line {line_number}).",
                        )
                        continue
                    self.validate_link_target(markdown, definition[0], line_number)
                shortcut_line = mask_spans(
                    masked_line,
                    [(reference.start(), reference.end()) for reference in references],
                )
                for shortcut in SHORTCUT_REFERENCE.finditer(shortcut_line):
                    normalized = normalize_reference_label(shortcut.group(1))
                    definition = definitions.get(normalized)
                    if definition is not None:
                        self.validate_link_target(markdown, definition[0], line_number)

    def run(self) -> ValidationResult:
        if not self.root.is_dir():
            return ValidationResult(
                str(self.root),
                0,
                self.expected_count,
                [Issue(".", "invalid_root", "Repository root does not exist.")],
            )
        skills = self.skill_directories()
        if not skills:
            self.issues.append(Issue(".", "no_skills_found", "No top-level Skill directories were found."))
        if self.expected_count is not None and len(skills) != self.expected_count:
            self.issues.append(
                Issue(
                    ".",
                    "skill_count_mismatch",
                    f"Expected {self.expected_count} Skill directories, found {len(skills)}.",
                )
            )
        for skill in skills:
            self.validate_skill(skill)
        self.validate_navigation(skills)
        self.validate_links()
        return ValidationResult(
            str(self.root),
            len(skills),
            self.expected_count,
            sorted(self.issues, key=lambda issue: (issue.path, issue.code, issue.message)),
        )


def parse_quoted_scalar(value: str, quote: str) -> str | None:
    index = 1
    while index < len(value):
        character = value[index]
        if quote == "'" and character == "'" and index + 1 < len(value) and value[index + 1] == "'":
            index += 2
            continue
        if quote == '"' and character == "\\":
            index += 2
            continue
        if character == quote:
            scalar = value[: index + 1]
            remainder = value[index + 1 :].strip()
            if remainder and not remainder.startswith("#"):
                return None
            if quote == "'":
                return scalar[1:-1].replace("''", "'")
            try:
                parsed = json.loads(scalar)
            except json.JSONDecodeError:
                return None
            return parsed if isinstance(parsed, str) else None
        index += 1
    return None


def parse_name_scalar(value: str) -> str | None:
    value = value.strip()
    if not value:
        return None
    if value[0] in ("'", '"'):
        return parse_quoted_scalar(value, value[0])
    value = re.split(r"\s+#", value, maxsplit=1)[0].strip()
    return value or None


def frontmatter_name(text: str) -> str | None:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", text, re.DOTALL)
    if not match:
        return None
    name = re.search(r"^name:\s*(.*?)\s*$", match.group(1), re.MULTILINE)
    return parse_name_scalar(name.group(1)) if name else None


def h2_headings(text: str) -> list[str]:
    headings: list[str] = []
    for _, line in non_fenced_lines(text):
        match = re.match(r"^##\s+(.+?)\s*$", strip_inline_code(line))
        if match:
            headings.append(match.group(1))
    return headings


def required_files_for(skill: Path) -> tuple[str, ...]:
    final_reference = (
        "references/commands.md"
        if skill.name == "skill-repo-release-verifier"
        else "references/templates.md"
    )
    return COMMON_REQUIRED_FILES + (final_reference,)


def non_fenced_lines(text: str) -> Iterable[tuple[int, str]]:
    in_fence = False
    fence_marker: str | None = None
    for number, line in enumerate(text.splitlines(), start=1):
        marker = re.match(r"^\s*(```|~~~)", line)
        if marker:
            if not in_fence:
                in_fence = True
                fence_marker = marker.group(1)
            elif marker.group(1) == fence_marker:
                in_fence = False
                fence_marker = None
            continue
        if not in_fence:
            yield number, line


def extract_category_entries(readme: str) -> dict[str, list[str]]:
    entries = {category: [] for category in README_CATEGORIES}
    current: str | None = None
    item = re.compile(r"^\s*(?:[-*+]\s+|\|\s*)`([a-z0-9][a-z0-9-]*)`")
    for _, line in non_fenced_lines(readme):
        heading = re.match(r"^###\s+(.+?)\s*$", line)
        if heading:
            current = heading.group(1) if heading.group(1) in entries else None
            continue
        if current:
            match = item.match(line)
            if match:
                entries[current].append(match.group(1))
    return entries


def normalize_reference_label(label: str) -> str:
    return " ".join(label.casefold().split())


def lexical_absolute(path: Path) -> Path:
    return Path(os.path.abspath(os.fspath(path)))


def strip_inline_code(line: str) -> str:
    return INLINE_CODE.sub("", line)


def find_inline_link_end(line: str, opening: int) -> int | None:
    depth = 1
    quote: str | None = None
    in_angle = False
    index = opening + 1
    while index < len(line):
        character = line[index]
        if character == "\\":
            index += 2
            continue
        if quote is not None:
            if character == quote:
                quote = None
        elif in_angle:
            if character == ">":
                in_angle = False
        elif character == "<":
            in_angle = True
        elif character in ("'", '"'):
            quote = character
        elif character == "(":
            depth += 1
        elif character == ")":
            depth -= 1
            if depth == 0:
                return index
        index += 1
    return None


def inline_destination(contents: str) -> str | None:
    contents = contents.strip()
    if not contents:
        return None
    if contents.startswith("<"):
        closing = contents.find(">")
        return contents[: closing + 1] if closing >= 0 else None
    depth = 0
    index = 0
    while index < len(contents):
        character = contents[index]
        if character == "\\":
            index += 2
            continue
        if character == "(":
            depth += 1
        elif character == ")" and depth:
            depth -= 1
        elif character.isspace() and depth == 0:
            break
        index += 1
    return contents[:index] or None


def parse_inline_links(line: str) -> list[tuple[str, int, int]]:
    links: list[tuple[str, int, int]] = []
    offset = 0
    while offset < len(line):
        match = INLINE_LINK_START.search(line, offset)
        if match is None:
            break
        opening = match.end() - 1
        closing = find_inline_link_end(line, opening)
        if closing is None:
            offset = match.end()
            continue
        target = inline_destination(line[opening + 1 : closing])
        if target is not None:
            links.append((target, match.start(), closing + 1))
        offset = closing + 1
    return links


def mask_spans(line: str, spans: list[tuple[int, int]]) -> str:
    if not spans:
        return line
    characters = list(line)
    for start, end in spans:
        characters[start:end] = " " * (end - start)
    return "".join(characters)


def parse_link_target(raw_target: str) -> tuple[str, str] | None:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None
    return unquote(parsed.path), unquote(parsed.fragment)


def github_heading_slug(heading: str) -> str:
    heading = re.sub(r"<[^>]+>", "", heading).strip().lower()
    heading = re.sub(r"[^\w\- ]", "", heading, flags=re.UNICODE)
    return re.sub(r"\s+", "-", heading)


def heading_anchors(text: str) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for _, line in non_fenced_lines(text):
        heading = MARKDOWN_HEADING.match(line)
        if not heading:
            continue
        base = github_heading_slug(heading.group(1))
        duplicate = counts.get(base, 0)
        anchor = base if duplicate == 0 else f"{base}-{duplicate}"
        counts[base] = duplicate + 1
        anchors.add(anchor)
    return anchors


def validate_repository(root: Path, expected_count: int | None = None) -> ValidationResult:
    return Validator(root, expected_count).run()


def positive_integer(value: str) -> int:
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("expected count must be at least 1")
    return number


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "repository",
        nargs="?",
        default=".",
        help="Skill repository root (default: current directory)",
    )
    parser.add_argument(
        "--expected-count",
        type=positive_integer,
        default=20,
        help="Expected number of top-level Skill directories (default: 20).",
    )
    parser.add_argument("--json", action="store_true", help="Emit the machine-readable result as JSON.")
    args = parser.parse_args()
    result = validate_repository(Path(args.repository), expected_count=args.expected_count)
    if args.json:
        print(json.dumps(result.as_dict(), ensure_ascii=False, indent=2, sort_keys=True))
    else:
        state = "PASS" if result.passed else "FAIL"
        expected = (
            f" expected {result.expected_skill_count};"
            if result.expected_skill_count is not None
            else ""
        )
        print(
            f"{state}: {result.skill_count} Skill directories checked;"
            f"{expected} {len(result.issues)} issue(s)."
        )
        for issue in result.issues:
            print(f"{issue.path}: [{issue.code}] {issue.message}")
    return 0 if result.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
