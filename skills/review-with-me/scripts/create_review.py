"""Copy the runnable starter without overwriting an existing review."""
import argparse
import shutil
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('destination', type=Path)
args = parser.parse_args()
source = Path(__file__).resolve().parents[1] / 'assets'
if args.destination.exists() and any(args.destination.iterdir()):
    parser.error('Destination is not empty. Adapt the existing review; do not overwrite it.')
shutil.copytree(source / 'template', args.destination, dirs_exist_ok=True)
(args.destination / 'assets').mkdir(exist_ok=True)
for name in ['review-desk.js', 'review-desk.css', 'review-actions.js', 'review-actions.css']:
    shutil.copy2(source / name, args.destination / 'assets' / name)
print(f'Review created: {args.destination.resolve()}')
print('Fill artifacts.json, then run python3 server.py --port PORT --thread TASK_UUID from that directory.')
