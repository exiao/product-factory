#!/usr/bin/env python3
"""Install Product Factory skills, or update managed files without losing local edits."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import tempfile

RECEIPT = '.product-factory-install.json'
LOCK = '.product-factory-install.lock'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(root):
    skills = sorted(p for p in root.iterdir()
                    if p.is_dir() and (p / 'SKILL.md').is_file())
    if not skills:
        raise ValueError('No skill directories containing SKILL.md found.')
    files = {}
    for skill in skills:
        for path in [skill, *skill.rglob('*')]:
            if path.is_symlink():
                raise ValueError(f'Source symlinks are not supported: {path}')
            if path.is_file():
                files[path.relative_to(root).as_posix()] = digest(path)
    return skills, files


def safe_path(root, relative):
    path = root
    for part in PurePosixPath(relative).parts:
        path = path / part
        if path.is_symlink():
            raise ValueError(f'Refusing destination symlink: {path}')
    return path


def read_receipt(destination):
    path = safe_path(destination, RECEIPT)
    if not path.is_file():
        raise ValueError('No installation receipt. Install into an empty --dest and '
                         'compare/back up older skills before reinstalling; see docs/setup.md.')
    receipt = json.loads(path.read_text())
    if (not isinstance(receipt, dict) or receipt.get('version') != 1
            or not isinstance(receipt.get('skills'), list)
            or not isinstance(receipt.get('files'), dict)):
        raise ValueError('Invalid or unsupported installation receipt.')
    names = receipt['skills']
    if not all(isinstance(name, str) and re.fullmatch(r'[a-z0-9][a-z0-9-]*', name)
               for name in names):
        raise ValueError('Invalid skill names in installation receipt.')
    for relative, checksum in receipt['files'].items():
        parts = relative.split('/')
        if (len(parts) < 2 or parts[0] not in names
                or any(part in ('', '.', '..') or '\\' in part or ':' in part for part in parts)
                or not isinstance(checksum, str) or not re.fullmatch(r'[0-9a-f]{64}', checksum)):
            raise ValueError(f'Invalid receipt file entry: {relative}')
        safe_path(destination, relative)
    return receipt


def atomic_write(path, content, mode):
    fd, temporary = tempfile.mkstemp(prefix='.product-factory-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(content)
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def save_receipt(destination, skills, files):
    content = json.dumps({'version': 1, 'skills': sorted(skills), 'files': files},
                         indent=2, sort_keys=True) + '\n'
    atomic_write(destination / RECEIPT, content.encode(), 0o600)


def parent_directories(files):
    return {parent.as_posix() for relative in files
            for parent in PurePosixPath(relative).parents if parent != PurePosixPath('.')}


def install(destination, skills, files):
    conflicts = [p.name for p in skills if os.path.lexists(destination / p.name)]
    if os.path.lexists(destination / RECEIPT):
        conflicts.append(RECEIPT)
    if conflicts:
        raise ValueError('No skills installed. Existing destinations: ' + ', '.join(conflicts)
                         + '\nUse --update for a managed installation or choose an empty --dest.')
    created = []
    try:
        for source in skills:
            target = destination / source.name
            target.mkdir()
            created.append(target)
            shutil.copytree(source, target, dirs_exist_ok=True)
        save_receipt(destination, [p.name for p in skills], files)
    except (OSError, KeyboardInterrupt):
        for target in reversed(created):
            shutil.rmtree(target)
        raise
    print(f'Installed {len(skills)} skills in {destination}. Start a new Codex task to use them.')
    return 0


def update(destination, source_root, skills, files):
    receipt = read_receipt(destination)
    old = receipt['files']
    owned = set(receipt['skills'])
    owned_dirs = parent_directories(old) | owned
    incoming = {p.name for p in skills}
    blocked = {name for name in incoming - owned if os.path.lexists(destination / name)}
    conflicts = [f'{name}: existing skill is not managed by this installation' for name in sorted(blocked)]
    next_files = dict(old)
    changes = []
    for relative in sorted(set(old) | set(files)):
        if relative.split('/')[0] in blocked:
            continue
        target = safe_path(destination, relative)
        unowned_parent = next((parent for parent in PurePosixPath(relative).parents
                               if parent != PurePosixPath('.') and parent.as_posix() not in owned_dirs
                               and (destination / parent).exists()), None)
        if unowned_parent is not None:
            conflicts.append(f'{relative}: existing directory {unowned_parent} is not managed')
            continue
        desired = files.get(relative)
        previous = old.get(relative)
        if target.exists() and not target.is_file():
            conflicts.append(f'{relative}: destination is not a regular file')
            continue
        actual = digest(target) if target.exists() else None
        if previous is None and actual is not None:
            conflicts.append(f'{relative}: local file is not managed')
        elif previous is not None and actual != previous and actual != desired:
            conflicts.append(f'{relative}: locally modified or deleted')
        else:
            if desired is None:
                next_files.pop(relative, None)
            else:
                next_files[relative] = desired
            if actual != desired:
                changes.append((target, source_root / relative if desired else None))

    # Keep the old receipt until all writes succeed; roll back ordinary I/O failures.
    undo = []
    created_dirs = []
    try:
        for target, source in changes:
            original = target.read_bytes() if target.exists() else None
            mode = stat.S_IMODE(target.stat().st_mode) if original is not None else None
            undo.append((target, original, mode))
            if source is None:
                target.unlink()
            else:
                missing = []
                parent = target.parent
                while not parent.exists():
                    missing.append(parent)
                    parent = parent.parent
                for parent in reversed(missing):
                    parent.mkdir()
                    created_dirs.append(parent)
                atomic_write(target, source.read_bytes(), mode if mode is not None
                             else stat.S_IMODE(source.stat().st_mode))
        save_receipt(destination, owned | (incoming - blocked), next_files)
    except (OSError, KeyboardInterrupt):
        for target, original, mode in reversed(undo):
            if original is None:
                if target.is_file():
                    target.unlink()
            else:
                atomic_write(target, original, mode)
        for parent in reversed(created_dirs):
            parent.rmdir()
        raise
    # Remove only obsolete empty managed folders, leaving local additions intact.
    for relative in sorted(owned_dirs - parent_directories(next_files), key=lambda p: p.count('/'), reverse=True):
        try:
            (destination / relative).rmdir()
        except OSError:
            pass  # Nonempty or inaccessible folders stay in place.
    print(f'Updated {len(changes)} files in {destination}. Local customizations preserved.')
    if conflicts:
        print('Conflicts (left unchanged):\n' + '\n'.join(conflicts))
        print('Back up and reconcile these files before retrying; see docs/setup.md.')
    return 1 if conflicts else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', type=Path,
                        default=Path(os.environ.get('CODEX_HOME', Path.home() / '.codex')) / 'skills')
    parser.add_argument('--update', action='store_true', help='Update files owned by an installation receipt.')
    args = parser.parse_args()
    try:
        source_root = Path(__file__).resolve().parent / 'skills'
        skills, files = inventory(source_root)
        if args.dest.expanduser().is_symlink():
            raise ValueError('The destination itself must not be a symlink.')
        destination = args.dest.expanduser().resolve()
        if destination == source_root or source_root in destination.parents:
            raise ValueError('Choose a destination outside the source skills directory.')
        destination.mkdir(parents=True, exist_ok=True)
        lock = destination / LOCK
        try:
            lock.mkdir()
        except FileExistsError:
            raise ValueError(f'Installation lock exists: {lock}. If no installer is running, '
                             'inspect an interrupted installation before removing this lock.')
        try:
            return update(destination, source_root, skills, files) if args.update else install(destination, skills, files)
        finally:
            lock.rmdir()
    except (OSError, ValueError, KeyboardInterrupt) as error:
        parser.exit(1, f'Installation failed: {error}\n')


if __name__ == '__main__':
    raise SystemExit(main())
