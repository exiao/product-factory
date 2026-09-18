"""Checks the real bridge with a stubbed CLI, never sending a task message."""
import importlib.util
import json
import subprocess
import tempfile
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('handoff', Path(__file__).resolve().parents[1] / 'assets/template/handoff.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
thread = '01a0b54f-8346-7463-9b0a-44086ed76994'
with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    data = {'drafts': {'x:v2': {'notes': 'Keep both'}}, 'responses': {}, 'selected': 'x'}
    with patch.object(m.subprocess, 'run', return_value=SimpleNamespace(returncode=0, stdout=f'Queued message test-message for thread {thread}')) as run:
        code, receipt = m.save_and_dispatch(data, root, thread)
        assert code == 200 and receipt['status'] == 'queued'
        assert run.call_args.args[0][:4] == ['codex', 'queue', '--thread', thread]
        m.save_and_dispatch({**data, 'selected': 'y', 'selectedAt': 'later'}, root, thread)
        assert run.call_count == 1
    with patch.object(m.subprocess, 'run', side_effect=subprocess.TimeoutExpired('codex',45)) as run:
        other = {**data, 'drafts': {'x:v2': {'notes': 'Revise this'}}}
        code, receipt = m.save_and_dispatch(other, root, thread)
        assert code == 409 and receipt['status'] == 'uncertain'
        m.save_and_dispatch(other, root, thread)
        assert run.call_count == 1
    snapshot = json.loads(next(root.glob('review-*.json')).read_text())
    assert not snapshot['responses']
print('PASS: acknowledged argv dispatch, dedup despite navigation, uncertainty retained/no retry, drafts not approval. CLI mocked.')
