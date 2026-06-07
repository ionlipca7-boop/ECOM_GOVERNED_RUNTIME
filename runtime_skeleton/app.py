from __future__ import annotations

import json
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

from contract_loader import load_dashboard_payload
from validator import validate_contracts


HOST = "127.0.0.1"
PORT = 8000
APP_ROOT = Path(__file__).resolve().parent
TEMPLATE_PATH = APP_ROOT / "templates" / "index.html"
STATIC_ROOT = APP_ROOT / "static"
LOCAL_URL = f"http://localhost:{PORT}"


class RuntimeSkeletonHandler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        path = urlparse(self.path).path

        if path in ("/", "/index.html"):
            self._send_html(TEMPLATE_PATH.read_text(encoding="utf-8"))
            return

        if path == "/api/contracts":
            self._send_json(load_dashboard_payload())
            return

        if path == "/api/validation":
            self._send_json(validate_contracts())
            return

        if path.startswith("/static/"):
            self.directory = str(APP_ROOT)
            super().do_GET()
            return

        self.send_error(404, "Not found")

    def log_message(self, format: str, *args: object) -> None:
        print(f"[local] {self.address_string()} - {format % args}")

    def _send_html(self, body: str) -> None:
        encoded = body.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def _send_json(self, payload: object) -> None:
        encoded = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)


def main() -> None:
    validate_contracts()
    server = ThreadingHTTPServer((HOST, PORT), RuntimeSkeletonHandler)
    print("ECOM OS V7.3C Local Control Panel")
    print(f"Local URL: {LOCAL_URL}")
    print("Press Ctrl+C to stop.")
    server.serve_forever()


if __name__ == "__main__":
    main()
