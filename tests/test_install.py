"""Exercise the public installer CLI against isolated source and destination trees."""
import importlib.util
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = '.product-factory-install.json'


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = self.root / 'source'
        self.source.mkdir()
        shutil.copy2(ROOT / 'install.py', self.source / 'install.py')
        self.dest = self.root / 'installed'
        self.write('alpha/SKILL.md', '---\nname: alpha\ndescription: example\n---\nVersion one\n')
        self.write('alpha/references/guide.md', 'Original guide\n')

    def write(self, relative, text):
        path = self.source / 'skills' / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def run_cli(self, *args, code=0):
        result = subprocess.run([sys.executable, str(self.source / 'install.py'),
                                 '--dest', str(self.dest), *args], capture_output=True, text=True)
        self.assertEqual(result.returncode, code, result.stdout + result.stderr)
        return result.stdout + result.stderr

    def receipt(self):
        return json.loads((self.dest / RECEIPT).read_text())

    def test_repository_bundle_installs_with_file_parity(self):
        result = subprocess.run([sys.executable, str(ROOT / 'install.py'), '--dest', str(self.dest)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        source_files = {p.relative_to(ROOT / 'skills').as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                        for skill in (ROOT / 'skills').iterdir() if (skill / 'SKILL.md').is_file()
                        for p in skill.rglob('*') if p.is_file()}
        self.assertEqual(source_files, self.receipt()['files'])
        for relative, checksum in source_files.items():
            self.assertEqual(hashlib.sha256((self.dest / relative).read_bytes()).hexdigest(), checksum)

    def test_destination_inside_source_is_refused(self):
        self.dest = self.source / 'skills/alpha/nested'
        self.assertIn('outside the source', self.run_cli(code=1))
        self.assertFalse(self.dest.exists())

    def test_fresh_install_and_conflict_refusal(self):
        self.write('.DS_Store', 'ignored root file')
        self.run_cli()
        for path in (self.source / 'skills/alpha').rglob('*'):
            if path.is_file():
                self.assertEqual(path.read_bytes(), (self.dest / path.relative_to(self.source / 'skills')).read_bytes())
        self.assertFalse((self.dest / '.DS_Store').exists())
        receipt = self.receipt()
        self.assertEqual(receipt['skills'], ['alpha'])
        self.write('beta/SKILL.md', 'new skill')
        self.run_cli(code=1)
        self.assertFalse((self.dest / 'beta').exists())
        self.assertEqual(receipt, self.receipt())

    def test_update_add_delete_and_repeat(self):
        self.run_cli()
        self.write('alpha/SKILL.md', 'Version two\n')
        (self.source / 'skills/alpha/references/guide.md').unlink()
        tool = self.write('alpha/scripts/tool.sh', '#!/bin/sh\nexit 0\n')
        tool.chmod(0o755)
        self.run_cli('--update')
        self.assertEqual((self.dest / 'alpha/SKILL.md').read_text(), 'Version two\n')
        self.assertFalse((self.dest / 'alpha/references/guide.md').exists())
        self.assertEqual((self.dest / 'alpha/scripts/tool.sh').stat().st_mode & 0o777, 0o755)
        self.assertNotIn('alpha/references/guide.md', self.receipt()['files'])
        self.assertIn('Updated 0 files', self.run_cli('--update'))

    def test_customizations_survive_and_conflicts_remain_until_reconciled(self):
        self.run_cli()
        old_hash = self.receipt()['files']['alpha/SKILL.md']
        (self.dest / 'alpha/SKILL.md').write_text('My customization\n')
        (self.dest / 'alpha/local.txt').write_text('My addition\n')
        self.write('alpha/SKILL.md', 'Upstream change\n')
        self.write('alpha/references/guide.md', 'New guide\n')
        self.write('alpha/local.txt', 'Upstream collision\n')
        self.run_cli('--update', code=1)
        self.assertEqual((self.dest / 'alpha/SKILL.md').read_text(), 'My customization\n')
        self.assertEqual((self.dest / 'alpha/local.txt').read_text(), 'My addition\n')
        self.assertEqual((self.dest / 'alpha/references/guide.md').read_text(), 'New guide\n')
        self.assertEqual(old_hash, self.receipt()['files']['alpha/SKILL.md'])
        self.assertNotIn('alpha/local.txt', self.receipt()['files'])
        self.run_cli('--update', code=1)
        shutil.copyfile(self.source / 'skills/alpha/SKILL.md', self.dest / 'alpha/SKILL.md')
        (self.dest / 'alpha/local.txt').unlink()  # User has backed up the unowned conflict.
        self.run_cli('--update')
        self.assertNotEqual(old_hash, self.receipt()['files']['alpha/SKILL.md'])

    def test_local_deletions_and_modified_upstream_deletions_are_preserved(self):
        self.run_cli()
        (self.dest / 'alpha/SKILL.md').unlink()
        (self.dest / 'alpha/references/guide.md').write_text('Custom guide')
        (self.source / 'skills/alpha/references/guide.md').unlink()
        self.run_cli('--update', code=1)
        self.assertFalse((self.dest / 'alpha/SKILL.md').exists())
        self.assertEqual((self.dest / 'alpha/references/guide.md').read_text(), 'Custom guide')

    def test_new_skill_does_not_merge_into_unowned_folder(self):
        self.run_cli()
        self.write('beta/SKILL.md', 'Upstream beta')
        (self.dest / 'beta').mkdir()
        (self.dest / 'beta/notes.txt').write_text('Unrelated beta')
        self.run_cli('--update', code=1)
        self.assertFalse((self.dest / 'beta/SKILL.md').exists())
        self.assertNotIn('beta', self.receipt()['skills'])
        self.assertEqual((self.dest / 'beta/notes.txt').read_text(), 'Unrelated beta')

    def test_update_preserves_nested_unowned_folders(self):
        self.run_cli()
        local = self.dest / 'alpha/local-folder'
        local.mkdir()
        (local / 'notes.txt').write_text('Local notes')
        self.write('alpha/local-folder/new.txt', 'Upstream addition')
        self.write('alpha/SKILL.md', 'Safe change')
        self.assertIn('directory alpha/local-folder is not managed', self.run_cli('--update', code=1))
        self.assertEqual(list(local.iterdir()), [local / 'notes.txt'])
        self.assertEqual((local / 'notes.txt').read_text(), 'Local notes')
        self.assertEqual((self.dest / 'alpha/SKILL.md').read_text(), 'Safe change')
        self.assertNotIn('alpha/local-folder/new.txt', self.receipt()['files'])

    def test_obsolete_empty_managed_folder_can_be_reintroduced(self):
        self.run_cli()
        (self.source / 'skills/alpha/references/guide.md').unlink()
        self.run_cli('--update')
        self.assertFalse((self.dest / 'alpha/references').exists())
        self.write('alpha/references/new.md', 'New guide')
        self.run_cli('--update')
        self.assertEqual((self.dest / 'alpha/references/new.md').read_text(), 'New guide')

    def test_legacy_invalid_receipt_and_symlink_refusal(self):
        self.dest.mkdir()
        self.assertIn('No installation receipt', self.run_cli('--update', code=1))
        self.run_cli()
        baseline = (self.dest / 'alpha/SKILL.md').read_bytes()
        receipt = self.receipt()
        for bad in ({'version': 99}, {**receipt, 'files': {'alpha/../../outside': 'a' * 64}}, []):
            with self.subTest(receipt=bad):
                (self.dest / RECEIPT).write_text(json.dumps(bad))
                self.run_cli('--update', code=1)
                self.assertEqual((self.dest / 'alpha/SKILL.md').read_bytes(), baseline)
        (self.dest / RECEIPT).write_text(json.dumps(receipt))
        outside = self.root / 'outside'
        outside.mkdir()
        (outside / 'guide.md').write_text('Do not touch')
        shutil.rmtree(self.dest / 'alpha/references')
        (self.dest / 'alpha/references').symlink_to(outside, target_is_directory=True)
        self.write('alpha/SKILL.md', 'New upstream')
        self.run_cli('--update', code=1)
        self.assertEqual((outside / 'guide.md').read_text(), 'Do not touch')
        self.assertEqual((self.dest / 'alpha/SKILL.md').read_bytes(), baseline)

    def test_active_or_interrupted_lock_is_respected(self):
        self.dest.mkdir()
        (self.dest / '.product-factory-install.lock').mkdir()
        self.assertIn('Installation lock exists', self.run_cli(code=1))
        self.assertFalse((self.dest / 'alpha').exists())

    def test_update_rolls_back_if_receipt_cannot_be_saved(self):
        self.run_cli()
        before = {p.relative_to(self.dest): p.read_bytes() for p in self.dest.rglob('*') if p.is_file()}
        self.write('alpha/SKILL.md', 'Changed')
        self.write('alpha/new/data.txt', 'Added')
        (self.source / 'skills/alpha/references/guide.md').unlink()
        spec = importlib.util.spec_from_file_location('installer', self.source / 'install.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        skills, files = module.inventory(self.source / 'skills')
        with patch.object(module, 'save_receipt', side_effect=OSError('disk error')):
            with self.assertRaises(OSError):
                module.update(self.dest, self.source / 'skills', skills, files)
        after = {p.relative_to(self.dest): p.read_bytes() for p in self.dest.rglob('*') if p.is_file()}
        self.assertEqual(before, after)
        self.assertFalse((self.dest / 'alpha/new').exists())


if __name__ == '__main__':
    unittest.main()
