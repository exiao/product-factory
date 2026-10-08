"""Exercise sibling isolation and request boundaries; never dispatch a task."""
import json
import shutil
import subprocess
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

source = Path(__file__).resolve().parents[1] / 'assets/template'
with tempfile.TemporaryDirectory() as directory:
    processes = []
    try:
        for index in range(2):
            site = Path(directory) / f'review-{index}'
            shutil.copytree(source, site)
            port = 18980 + index
            processes.append(subprocess.Popen(['python3', str(site / 'server.py'), '--port', str(port)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL))
        def request(port, path='/api/review', payload=None, headers=None):
            req = urllib.request.Request(f'http://127.0.0.1:{port}{path}',
                data=json.dumps(payload).encode() if payload is not None else None,
                headers={'Content-Type': 'application/json', **(headers or {})})
            with urllib.request.urlopen(req, timeout=3) as response:
                return json.load(response)
        for port in (18980, 18981):
            for attempt in range(30):
                try:
                    request(port)
                    break
                except urllib.error.URLError:
                    time.sleep(.1)
            else:
                raise AssertionError('Server did not start')
        request(18980, payload={'project': 'one', 'drafts': {'a': 'note'}})
        assert request(18980)['project'] == 'one'
        assert request(18981) == {}, 'Sibling review leaked saved state'
        assert request(18981, headers={'Referer': 'https://github.com/'}) == {}
        try:
            request(18980, payload={}, headers={'Origin': 'https://attacker.invalid'})
            raise AssertionError('Cross-origin write accepted')
        except urllib.error.HTTPError as error:
            assert error.code == 403
        for path, headers in [('/.feedback/current.json', {}), ('/api/review', {'Host': 'attacker.invalid'})]:
            try:
                request(18980, path, headers=headers)
                raise AssertionError('Private data was accessible')
            except urllib.error.HTTPError as error:
                assert error.code in (403, 404)
        request(18980, '/api/snapshot', {'drafts': {'a': 'note'}, 'selected': 'a'})
        request(18980, '/api/snapshot', {'drafts': {'a': 'note'}, 'selected': 'b'})
        assert len(list((Path(directory)/'review-0/.feedback').glob('review-*.json'))) == 1
        print('PASS: sibling isolation, private-file/Host rejection, shared snapshot deduplication')
    finally:
        for process in processes:
            process.terminate()
            process.wait(timeout=5)
