#!/usr/bin/env python3
"""Check local Markdown references in a skill directory.

The checker deliberately stays local and conservative: remote URLs, code examples,
and obvious documentation placeholders are ignored.  ``--orphans`` reports files
that are candidates for review when they cannot be reached from ``SKILL.md``.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, Optional
from urllib.parse import unquote, urlsplit


_FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
_LINK_START_RE = re.compile(r"(?:!?)\[[^\n\]]*\]\(")
_REFERENCE_RE = re.compile(
    r"^\s{0,3}\[[^\]\n]+\]:\s*(?:<([^>\n]*)>|(\S+))"
)
_REFERENCE_USE_RE = re.compile(r"(?<!!)\[([^\]\n]*)\]\[([^\]\n]*)\]")


@dataclass(frozen=True)
class Link:
    source: Path
    line: int
    raw_target: str


@dataclass(frozen=True)
class BrokenLink:
    link: Link
    resolved: Path


def _remove_inline_code(line: str) -> str:
    """Remove inline code spans, including an unterminated span to line end."""

    output: list[str] = []
    position = 0
    while position < len(line):
        start = line.find("`", position)
        if start < 0:
            output.append(line[position:])
            break
        output.append(line[position:start])
        run_end = start
        while run_end < len(line) and line[run_end] == "`":
            run_end += 1
        marker = line[start:run_end]
        close = line.find(marker, run_end)
        if close < 0:
            break
        position = close + len(marker)
    return "".join(output)


def _markdown_lines(text: str) -> Iterator[tuple[int, str]]:
    """Yield non-code Markdown lines with their original one-based line number."""

    fence: Optional[tuple[str, int]] = None
    for line_number, line in enumerate(text.splitlines(), 1):
        match = _FENCE_RE.match(line)
        if fence is not None:
            if match and match.group(1)[0] == fence[0] and len(match.group(1)) >= fence[1]:
                fence = None
            continue
        if match:
            fence = (match.group(1)[0], len(match.group(1)))
            continue
        yield line_number, _remove_inline_code(line)


def _parse_parenthesized_target(line: str, open_paren: int) -> Optional[str]:
    """Read a Markdown destination after the opening ``](`` at ``open_paren``."""

    position = open_paren + 1
    while position < len(line) and line[position].isspace():
        position += 1
    if position >= len(line):
        return None
    if line[position] == "<":
        end = position + 1
        while end < len(line):
            if line[end] == ">" and (end == 0 or line[end - 1] != "\\"):
                return line[position + 1 : end]
            end += 1
        return None

    start = position
    depth = 0
    while position < len(line):
        character = line[position]
        if character == "\\" and position + 1 < len(line):
            position += 2
            continue
        if character == "(" :
            depth += 1
        elif character == ")":
            if depth == 0:
                break
            depth -= 1
        elif character.isspace() and depth == 0:
            break
        position += 1
    return line[start:position] or None


def iter_links(source: Path, text: str) -> Iterator[Link]:
    """Extract inline and reference-definition links from Markdown text."""

    lines = list(_markdown_lines(text))
    definitions: dict[str, str] = {}
    for _, line in lines:
        reference = _REFERENCE_RE.match(line)
        if reference:
            definition = reference.group(1) or reference.group(2)
            label = line[line.index("[") + 1 : line.index("]")].strip().casefold()
            definitions[label] = definition

    for line_number, line in lines:
        for match in _LINK_START_RE.finditer(line):
            target = _parse_parenthesized_target(line, match.end() - 1)
            if target is not None:
                yield Link(source, line_number, target)
        reference = _REFERENCE_RE.match(line)
        if reference:
            yield Link(source, line_number, reference.group(1) or reference.group(2))
            continue
        for match in _REFERENCE_USE_RE.finditer(line):
            label = (match.group(2) or match.group(1)).strip().casefold()
            target = definitions.get(label)
            if target is not None:
                yield Link(source, line_number, target)


def _is_placeholder(target: str) -> bool:
    lowered = target.casefold()
    if target in {"...", "…", "TODO", "FIXME", "PLACEHOLDER"} or "path/to/" in lowered:
        return True
    if (target.startswith("{") and target.endswith("}")) or (
        target.startswith("$") and target.endswith("}")
    ):
        return True
    return False


def resolve_local_target(raw_target: str, source: Path) -> Optional[Path]:
    """Normalize a local Markdown destination, or return ``None`` when skipped."""

    target = html.unescape(raw_target.strip())
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    target = target.replace(r"\ ", " ")
    target = re.sub(r"\\([\\()<>{}\[\]])", r"\1", target)
    if not target or target.startswith("#") or _is_placeholder(target):
        return None
    parsed = urlsplit(target)
    # A scheme and protocol-relative URL both identify a remote/non-file target.
    if parsed.scheme or target.startswith("//"):
        return None
    path_text = target.split("#", 1)[0].split("?", 1)[0]
    if not path_text:
        return None
    path_text = unquote(path_text)
    path = Path(path_text).expanduser()
    if not path.is_absolute():
        path = source.parent / path
    return path.resolve(strict=False)


def _read_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def markdown_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.md") if path.is_file())


def find_broken_links(root: Path) -> list[BrokenLink]:
    broken: list[BrokenLink] = []
    for source in markdown_files(root):
        for link in iter_links(source, _read_markdown(source)):
            resolved = resolve_local_target(link.raw_target, source)
            if resolved is not None and not resolved.exists():
                broken.append(BrokenLink(link, resolved))
    return broken


def _in_root(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def find_orphan_candidates(root: Path) -> list[Path]:
    """Return in-root files unreachable from the ``SKILL.md`` link graph."""

    display_root = root
    canonical_root = root.resolve()
    entrypoint = (canonical_root / "SKILL.md").resolve(strict=False)
    if not entrypoint.is_file():
        return []
    reachable: set[Path] = {entrypoint}
    pending = [entrypoint]
    while pending:
        source = pending.pop()
        if source.suffix.casefold() != ".md":
            continue
        for link in iter_links(source, _read_markdown(source)):
            resolved = resolve_local_target(link.raw_target, source)
            if resolved is None or not resolved.is_file() or not _in_root(resolved, canonical_root):
                continue
            if resolved not in reachable:
                reachable.add(resolved)
                if resolved.suffix.casefold() == ".md":
                    pending.append(resolved)

    candidates = []
    for path in sorted(display_root.rglob("*")):
        if path.is_file() and path.resolve(strict=False) not in reachable:
            candidates.append(path)
    return candidates


def _display(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def build_parser() -> argparse.ArgumentParser:
    return argparse.ArgumentParser(
        prog="check_reference_health.py",
        description="Check exact local Markdown links in one skill directory.",
        epilog=(
            "Supports inline links ([text](path)), image links, and reference definitions; "
            "destinations may use angle brackets for spaces and may include URL encoding. "
            "Anchors and query strings are ignored for local existence checks. Remote URLs, "
            "fenced or inline code, and obvious placeholders are skipped. --orphans follows "
            "links from SKILL.md through Markdown references and prints review candidates; "
            "it is not proof that every unlinked file is defective. This is not a full CommonMark "
            "parser: multiline links, HTML links, and other extensions are not validated."
        ),
    )


def main(argv: Optional[Iterable[str]] = None) -> int:
    parser = build_parser()
    parser.add_argument("target", type=Path, help="skill directory to inspect")
    parser.add_argument(
        "--orphans",
        action="store_true",
        help="print in-target files unreachable from SKILL.md",
    )
    args = parser.parse_args(argv)
    root = args.target.expanduser()
    if not root.exists() or not root.is_dir():
        print(f"error: target directory does not exist: {root}", file=sys.stderr)
        return 2
    root = root.resolve()
    if not (root / "SKILL.md").is_file():
        print(f"error: target skill is missing SKILL.md: {root}", file=sys.stderr)
        return 2

    broken = find_broken_links(root)
    if broken:
        print(f"Broken local links in {root}:")
        for item in broken:
            print(
                f"  {_display(item.link.source, root)}:{item.link.line}: "
                f"{item.link.raw_target!r} -> {item.resolved}"
            )
    else:
        print(f"No broken local links in {root}.")

    if args.orphans:
        entrypoint = root / "SKILL.md"
        if not entrypoint.is_file():
            print("Orphan candidates unavailable: SKILL.md is missing.")
        else:
            candidates = find_orphan_candidates(root)
            if candidates:
                print("Orphan candidates (review in context):")
                for path in candidates:
                    print(f"  {_display(path, root)}")
            else:
                print("No orphan candidates from SKILL.md.")
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
