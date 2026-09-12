#!/usr/bin/env python3
"""Copy the skill bundle without overwriting existing skills."""
import argparse
import os
from pathlib import Path
import shutil


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', type=Path, default=Path(os.environ.get('CODEX_HOME', Path.home() / '.codex')) / 'skills')
    args = parser.parse_args()
    sources = sorted((Path(__file__).resolve().parent / 'skills').iterdir())
    destination = args.dest.expanduser().resolve()
    conflicts = [p.name for p in sources if os.path.lexists(destination / p.name)]
    if conflicts:
        parser.exit(1, 'No skills installed. Existing destinations: ' + ', '.join(conflicts) + '\nChoose an empty --dest or move conflicting folders to a backup first.\n')
    destination.mkdir(parents=True, exist_ok=True)
    created = []
    try:
        for source in sources:
            target = destination / source.name
            target.mkdir()  # Reserve only a previously absent directory.
            created.append(target)
            shutil.copytree(source, target, dirs_exist_ok=True)
    except (OSError, KeyboardInterrupt) as error:
        for target in reversed(created):
            shutil.rmtree(target)
        parser.exit(1, f'Installation failed; newly created skill folders removed: {error}\n')
    print(f'Installed {len(sources)} skills in {destination}. Start a new Codex task to use them.')


if __name__ == '__main__':
    main()
