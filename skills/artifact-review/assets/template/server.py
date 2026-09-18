"""Isolated local review server for the bitcoin-move review desk."""
# Stdlib only. Serves this review dir on 127.0.0.1; persists UI state
# to ../feedback/current.json and immutable snapshots beside it.
# Dispatch uses fixed server-side argv and task binding; no browser-controlled commands.
from __future__ import annotations

import argparse
import hashlib
import json
import os
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, unquote
import uuid
from handoff import save_and_dispatch

# Cap accepted JSON bodies at 128 KiB to bound memory/disk use.
MAX_BODY = 128 * 1024
# Review dir is the only static root; feedback lives one level up.
REVIEW_DIR = Path(__file__).resolve().parent
FEEDBACK_DIR = REVIEW_DIR.parent / "feedback"
CURRENT_FILE = FEEDBACK_DIR / "current.json"
# Serializes read-modify-write cycles across handler threads.
IO_LOCK = threading.Lock()
DISPATCH_THREAD = None


def _json_bytes(obj: object) -> bytes:
    # Canonical encoding keeps snapshot hashes stable.
    return json.dumps(obj, ensure_ascii=False, sort_keys=True).encode("utf-8")


def _send_json(handler: SimpleHTTPRequestHandler, status: int, obj: object) -> None:
    body = _json_bytes(obj)
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Content-Length", str(len(body)))
    handler.send_header("Cache-Control", "no-store")
    handler.end_headers()
    handler.wfile.write(body)


def _same_origin_ok(handler: SimpleHTTPRequestHandler) -> bool:
    # Non-browser clients send no Origin/Referer and are allowed.
    # Browser fetch() always sends Origin; forms/backs may send Referer.
    host = handler.headers.get("Host", "")
    if host not in {f"127.0.0.1:{handler.server.server_port}", f"localhost:{handler.server.server_port}"}:
        return False
    for name in ("Origin", "Referer"):
        val = handler.headers.get(name)
        if not val:
            continue
        try:
            netloc = urlparse(val).netloc
        except Exception:
            return False
        # Exact host:port match blocks cross-site POSTs (CSRF).
        if netloc != host:
            return False
    return True


def _read_json_body(handler: SimpleHTTPRequestHandler):
    # Returns (obj, error_response). Enforces size + JSON-only.
    ctype = (handler.headers.get("Content-Type") or "").split(";")[0].strip().lower()
    if ctype != "application/json":
        return None, (415, {"error": "Content-Type must be application/json"})
    try:
        length = int(handler.headers.get("Content-Length", ""))
    except (TypeError, ValueError):
        return None, (411, {"error": "Content-Length header required"})
    if length < 0 or length > MAX_BODY:
        return None, (413, {"error": f"body over {MAX_BODY} byte limit"})
    try:
        raw = handler.rfile.read(length)
    except Exception:
        return None, (400, {"error": "failed to read request body"})
    if len(raw) != length:
        return None, (400, {"error": "truncated request body"})
    try:
        obj = json.loads(raw.decode("utf-8"))
    except Exception:
        return None, (400, {"error": "invalid JSON body"})
    if not isinstance(obj, dict):
        return None, (400, {"error": "JSON body must be an object"})
    return obj, None


def _atomic_write(path: Path, data: bytes) -> None:
    # Tmp-file + os.replace keeps readers from seeing partial writes.
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


class Handler(SimpleHTTPRequestHandler):
    # Pin static serving to the review dir regardless of cwd.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(REVIEW_DIR), **kwargs)

    def log_message(self, *args):  # Quieter stdout; errors still raise.
        pass

    def list_directory(self, path):  # No directory listings.
        self.send_error(404, "Not found")

    def _block_special(self, rel: str) -> bool:
        # Hide server source, dotfiles, and anything escaping the root.
        parts = [p for p in unquote(rel).split("/") if p not in ("", ".")]
        if ".." in parts:
            return True
        if any(p.endswith((".py", ".pyc")) for p in parts):
            return True
        if any(p.startswith(".") or p == "__pycache__" for p in parts):
            return True
        target = (REVIEW_DIR.joinpath(*parts) if parts else REVIEW_DIR).resolve()
        return target != REVIEW_DIR and REVIEW_DIR not in target.parents

    def do_GET(self):
        path = urlparse(self.path).path.rstrip("/") or "/"
        if path == "/api/capabilities":
            _send_json(self, 200, {"dispatch": bool(DISPATCH_THREAD)})
            return
        if path == "/api/review":
            # Return last saved POST body, or {} when nothing saved yet.
            with IO_LOCK:
                try:
                    obj = json.loads(CURRENT_FILE.read_text(encoding="utf-8"))
                except FileNotFoundError:
                    obj = {}
                except Exception:
                    _send_json(self, 500, {"error": "saved review state unreadable"})
                    return
            if not isinstance(obj, dict):
                obj = {}
            _send_json(self, 200, obj)
            return
        if path.startswith("/api/"):  # No other API surface exists.
            _send_json(self, 404, {"error": "unknown api route"})
            return
        if self._block_special(urlparse(self.path).path):
            self.send_error(404, "Not found")
            return
        return super().do_GET()

    def do_HEAD(self):
        if self._block_special(urlparse(self.path).path):
            self.send_error(404, "Not found")
            return
        return super().do_HEAD()

    def do_POST(self):
        route = urlparse(self.path).path.rstrip("/") or "/"
        if route not in ("/api/review", "/api/snapshot", "/api/submit"):
            _send_json(self, 404, {"error": "unknown api route"})
            return
        if not _same_origin_ok(self):  # Reject cross-site browser POSTs.
            _send_json(self, 403, {"error": "cross-origin POST rejected"})
            return
        obj, err = _read_json_body(self)
        if err:
            _send_json(self, err[0], err[1])
            return
        if route == "/api/submit":
            if not DISPATCH_THREAD:
                _send_json(self, 503, {"error": "Codex is not connected. Export feedback or restart with --thread."})
                return
            code, receipt = save_and_dispatch(obj, FEEDBACK_DIR, DISPATCH_THREAD)
            _send_json(self, code, {k: receipt[k] for k in ("status", "messageId", "error") if k in receipt})
            return
        data = _json_bytes(obj)
        if len(data) > MAX_BODY:
            _send_json(self, 413, {"error": f"body over {MAX_BODY} byte limit"})
            return
        with IO_LOCK:
            try:
                FEEDBACK_DIR.mkdir(parents=True, exist_ok=True)
                if route == "/api/review":
                    _atomic_write(CURRENT_FILE, data)
                    _send_json(self, 200, {"saved": True})
                    return
                # Navigation does not change the content identity.
                data = _json_bytes({k: v for k, v in obj.items() if k not in ("selected", "selectedAt", "exportedAt")})
                # Identical content reuses the same immutable snapshot.
                digest = hashlib.sha256(data).hexdigest()
                dest = FEEDBACK_DIR / f"snapshot-{digest}.json"
                if not dest.exists():
                    _atomic_write(dest, data)
                _send_json(self, 200, {"saved": True, "path": str(dest.resolve())})
            except OSError:
                _send_json(self, 500, {"error": "failed to write feedback file"})


def main() -> None:
    global DISPATCH_THREAD
    ap = argparse.ArgumentParser(description="bitcoin-move local review server")
    ap.add_argument("--port", type=int, default=8769, help="localhost port")
    ap.add_argument("--thread", help="Fixed originating Codex task UUID")
    args = ap.parse_args()
    if args.thread:
        DISPATCH_THREAD = str(uuid.UUID(args.thread))
        FEEDBACK_DIR.mkdir(parents=True, exist_ok=True)
        binding = FEEDBACK_DIR / "task.json"
        if binding.exists() and json.loads(binding.read_text()).get("thread") != DISPATCH_THREAD:
            raise SystemExit("Review is already bound to another task")
        _atomic_write(binding, _json_bytes({"thread": DISPATCH_THREAD}))
    if not (1 <= args.port <= 65535):
        raise SystemExit("--port must be 1-65535")
    # Localhost-only bind; no TLS/auth needed for an isolated review loop.
    ThreadingHTTPServer(("127.0.0.1", args.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
