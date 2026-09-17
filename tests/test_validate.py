import tempfile
import unittest
from pathlib import Path

from scripts.validate import validate


class ValidateTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        (self.root / "skills" / "demo").mkdir(parents=True)
        (self.root / "skills" / "demo" / "SKILL.md").write_text(
            "---\nname: demo\ndescription: A useful demo skill.\n---\n\n# Demo\n",
            encoding="utf-8",
        )

    def tearDown(self):
        self.tempdir.cleanup()

    def write_docs(self, readme="This repository supplies 1 skills.\n", bundle_count=1):
        (self.root / "README.md").write_text(readme, encoding="utf-8")
        (self.root / "BUNDLE.md").write_text(
            f"# Bundle\n\n{bundle_count} skills selected.\n\n"
            "- [demo](skills/demo/SKILL.md)\n",
            encoding="utf-8",
        )

    def test_validates_local_links_and_ignores_examples_remote_and_anchors(self):
        self.write_docs()
        (self.root / "docs").mkdir()
        (self.root / "docs" / "guide.md").write_text(
            "[skill](../skills/demo/SKILL.md#usage)\n"
            "[remote](https://example.com/missing.md)\n"
            "[anchor](#section)\n\n"
            "```markdown\n[example](missing.md)\n```\n",
            encoding="utf-8",
        )
        (self.root / "preview-skills").mkdir()
        (self.root / "preview-skills" / "ignored.md").write_text(
            "[ignored](missing.md)\n", encoding="utf-8"
        )
        self.assertEqual(validate(self.root), [])

    def test_reports_missing_links_and_metadata_or_inventory_drift(self):
        self.write_docs(readme="This repository supplies 2 skills.\n", bundle_count=2)
        (self.root / "docs.md").write_text(
            "[missing](missing.md) [second missing](second.md) "
            "![missing image](missing.svg)\n",
            encoding="utf-8",
        )
        (self.root / "skills" / "demo" / "SKILL.md").write_text(
            "---\nname: wrong\ndescription: \n---\n", encoding="utf-8"
        )
        errors = "\n".join(validate(self.root))
        self.assertIn("missing link target", errors)
        self.assertIn("second.md", errors)
        self.assertIn("missing.svg", errors)
        self.assertIn("name must be 'demo'", errors)
        self.assertIn("description must be nonempty", errors)
        self.assertIn("README.md: advertises 2 skills; found 1", errors)
        self.assertIn("BUNDLE.md: advertises 2 skills; found 1", errors)

    def test_rejects_unsupported_frontmatter_scalars(self):
        self.write_docs()
        for scalar in ("true", "null", "|", "123"):
            with self.subTest(scalar=scalar):
                (self.root / "skills" / "demo" / "SKILL.md").write_text(
                    f"---\nname: demo\ndescription: {scalar}\n---\n", encoding="utf-8"
                )
                self.assertIn("unsupported description scalar", "\n".join(validate(self.root)))


if __name__ == "__main__":
    unittest.main()
