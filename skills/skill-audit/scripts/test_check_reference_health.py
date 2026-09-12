#!/usr/bin/env python3
"""Focused tests for check_reference_health.py."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("check_reference_health.py")
SPEC = importlib.util.spec_from_file_location("check_reference_health", SCRIPT)
assert SPEC and SPEC.loader
checker = importlib.util.module_from_spec(SPEC)
sys.modules["check_reference_health"] = checker
SPEC.loader.exec_module(checker)


class ReferenceHealthTests(unittest.TestCase):
    def make_skill(self, skill: str, **files: str) -> Path:
        directory = Path(self.tempdir.name) / skill
        directory.mkdir(parents=True)
        for relative, content in files.items():
            path = directory / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        return directory

    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def test_broken_exact_path_is_not_rescued_by_existing_sibling(self) -> None:
        root = self.make_skill(
            "exact",
            **{
                "SKILL.md": "[missing](references/guide.md)\n",
                "references/other/guide.md": "# sibling\n",
            },
        )
        broken = checker.find_broken_links(root)
        self.assertEqual([item.link.raw_target for item in broken], ["references/guide.md"])

    def test_missing_example_is_not_placeholder(self) -> None:
        root = self.make_skill("missing-example", **{"SKILL.md": "[example](example.md)\n"})
        self.assertEqual(len(checker.find_broken_links(root)), 1)

    def test_valid_sibling_link_resolves(self) -> None:
        root = self.make_skill(
            "sibling",
            **{
                "SKILL.md": "[sibling skill](../other/SKILL.md)\n",
            },
        )
        (root.parent / "other").mkdir()
        (root.parent / "other/SKILL.md").write_text("# other\n", encoding="utf-8")
        self.assertEqual(checker.find_broken_links(root), [])

    def test_example_filename_is_checked_as_a_real_path(self) -> None:
        root = self.make_skill(
            "example-name",
            **{
                "SKILL.md": "[example](example.md)\n",
                "references/example.md": "# different path\n",
            },
        )
        broken = checker.find_broken_links(root)
        self.assertEqual([item.link.raw_target for item in broken], ["example.md"])

    def test_nested_references_are_traversed(self) -> None:
        root = self.make_skill(
            "nested",
            **{
                "SKILL.md": "[guide](references/guide.md)\n",
                "references/guide.md": "[details](nested/details.md)\n",
                "references/nested/details.md": "# details\n",
            },
        )
        self.assertEqual(checker.find_broken_links(root), [])

    def test_code_remote_anchor_query_encoded_and_tilde_targets_are_handled(self) -> None:
        root = self.make_skill(
            "forms",
            **{
                "SKILL.md": (
                    "`[bad](nope.md)`\n"
                    "```md\n[bad](nope-too.md)\n```\n"
                    "[remote](https://example.com/nope.md)\n"
                    "[anchor](#section) [query](docs/guide.md?x=1#top)\n"
                    "[encoded](<docs/space%20name.md>)\n"
                    "[example](example.md)\n"
                ),
                "docs/guide.md": "# guide\n",
                "docs/space name.md": "# spaces\n",
                "example.md": "# example\n",
            },
        )
        self.assertEqual(checker.find_broken_links(root), [])

    def test_orphans_follow_transitive_references_and_report_candidates(self) -> None:
        root = self.make_skill(
            "orphans",
            **{
                "SKILL.md": "[guide][guide]\n\n[guide]: references/guide.md\n",
                "references/guide.md": "[details](nested/details.md)\n",
                "references/nested/details.md": "# details\n",
                "references/unlinked.md": "# candidate\n",
            },
        )
        candidates = checker.find_orphan_candidates(root)
        self.assertEqual([path.relative_to(root).as_posix() for path in candidates], ["references/unlinked.md"])


if __name__ == "__main__":
    unittest.main()
