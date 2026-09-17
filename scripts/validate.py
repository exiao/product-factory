#!/usr/bin/env python3
"""Validate the repository's Markdown links, skill metadata, and inventory.

This intentionally supports the repository's current Markdown and frontmatter
shapes. It is not a general Markdown or YAML parser.
"""
import ast
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


INLINE_LINK = re.compile(r"!?\[[^\]]*\]\(\s*(?:<([^>\n]+)>|([^\s)]+))")
REFERENCE_LINK = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(?:<([^>\n]+)>|(\S+))")
COUNT = re.compile(r"\b(\d+)\s+skills\b", re.IGNORECASE)
NON_STRING_SCALAR = re.compile(
    r"^(?:true|false|null|~|[-+]?(?:\d+|\d*\.\d+)(?:[eE][-+]?\d+)?|\d{4}-\d{1,2}-\d{1,2})$",
    re.IGNORECASE,
)


def markdown_links(path):
    """Yield (line number, destination) for links outside fenced code."""
    fence = None
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.lstrip()
        marker = stripped[:3] if stripped.startswith(("```", "~~~")) else None
        if fence:
            if marker == fence:
                fence = None
            continue
        if marker:
            fence = marker
            continue
        matches = list(INLINE_LINK.finditer(line))
        if matches:
            for match in matches:
                yield line_number, next(value for value in match.groups() if value is not None)
        else:
            match = REFERENCE_LINK.match(line)
            if match:
                yield line_number, next(value for value in match.groups() if value is not None)


def _local_destination(destination):
    destination = destination.strip()
    parsed = urlparse(destination)
    if not destination or destination.startswith("#") or destination.startswith("//") or parsed.scheme:
        return None
    return unquote(destination.split("#", 1)[0])


def validate_links(root):
    errors = []
    for markdown in sorted(root.rglob("*.md")):
        if any(part in (".git", "preview-skills") for part in markdown.relative_to(root).parts):
            continue
        for line_number, destination in markdown_links(markdown):
            destination = _local_destination(destination)
            if destination is None:
                continue
            target = (markdown.parent / destination).resolve()
            try:
                target.relative_to(root)
            except ValueError:
                errors.append(f"{markdown.relative_to(root)}:{line_number}: link escapes repository: {destination}")
            else:
                if not target.exists():
                    errors.append(f"{markdown.relative_to(root)}:{line_number}: missing link target: {destination}")
    return errors


def _frontmatter(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, ["missing opening frontmatter delimiter"]
    try:
        end = next(index for index, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration:
        return {}, ["missing closing frontmatter delimiter"]

    fields, errors = {}, []
    for line in lines[1:end]:
        match = re.match(r"^(name|description):[ \t]*(.*)$", line)
        if not match:
            continue
        key, raw = match.groups()
        if key in fields:
            errors.append(f"duplicate frontmatter field: {key}")
            continue
        if raw[:1] in ("'", '"'):
            try:
                value = ast.literal_eval(raw)
            except (SyntaxError, ValueError):
                errors.append(f"unsupported {key} scalar: {raw}")
                continue
            if not isinstance(value, str):
                errors.append(f"{key} must be a string")
                continue
        else:
            value = raw.strip()
            if (not value or value[:1] in "|>[{" or NON_STRING_SCALAR.fullmatch(value)):
                errors.append(f"unsupported {key} scalar: {raw}")
                continue
        fields[key] = value
    return fields, errors


def validate_metadata(root, skill_dirs):
    errors = []
    for skill_dir in skill_dirs:
        path = skill_dir / "SKILL.md"
        if not path.exists():
            errors.append(f"{skill_dir.relative_to(root)}: missing SKILL.md")
            continue
        fields, field_errors = _frontmatter(path)
        for error in field_errors:
            errors.append(f"{path.relative_to(root)}: {error}")
        if fields.get("name") != skill_dir.name:
            errors.append(f"{path.relative_to(root)}: name must be {skill_dir.name!r}")
        if not fields.get("description", "").strip():
            errors.append(f"{path.relative_to(root)}: description must be nonempty")
    return errors


def validate_inventory(root, skill_dirs):
    errors, actual = [], {skill_dir.name for skill_dir in skill_dirs}
    bundle = root / "BUNDLE.md"
    readme = root / "README.md"
    if not bundle.exists():
        return ["BUNDLE.md: file is missing"]
    bundle_skills = []
    for _, destination in markdown_links(bundle):
        destination = _local_destination(destination)
        if destination:
            match = re.fullmatch(r"skills/([^/]+)/SKILL\.md", destination)
            if match:
                bundle_skills.append(match.group(1))
    if len(bundle_skills) != len(actual):
        errors.append(f"BUNDLE.md: lists {len(bundle_skills)} skills; found {len(actual)} skill directories")
    duplicates = sorted(name for name in set(bundle_skills) if bundle_skills.count(name) > 1)
    if duplicates:
        errors.append("BUNDLE.md: duplicate skills: " + ", ".join(duplicates))
    missing = sorted(actual - set(bundle_skills))
    extra = sorted(set(bundle_skills) - actual)
    if missing:
        errors.append("BUNDLE.md: missing skills: " + ", ".join(missing))
    if extra:
        errors.append("BUNDLE.md: unknown skills: " + ", ".join(extra))
    for document in (bundle, readme):
        if not document.exists():
            if document == readme:
                errors.append("README.md: file is missing")
            continue
        advertised = [int(value) for value in COUNT.findall(document.read_text(encoding="utf-8"))]
        if not advertised:
            errors.append(f"{document.name}: no advertised skill count found")
        for count in advertised:
            if count != len(actual):
                errors.append(f"{document.name}: advertises {count} skills; found {len(actual)} skill directories")
    return errors


def validate(root):
    root = root.resolve()
    skills_root = root / "skills"
    skill_dirs = sorted((path for path in skills_root.iterdir() if path.is_dir()), key=lambda path: path.name) if skills_root.exists() else []
    errors = validate_links(root)
    errors.extend(validate_metadata(root, skill_dirs))
    errors.extend(validate_inventory(root, skill_dirs))
    return errors


def main():
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print("Validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    skill_count = sum(1 for path in (root / "skills").iterdir() if path.is_dir())
    print(f"Validation passed: {skill_count} skills and local Markdown links are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
