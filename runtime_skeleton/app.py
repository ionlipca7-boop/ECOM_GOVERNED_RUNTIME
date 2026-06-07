from __future__ import annotations

import json
from pathlib import Path
from string import Template
from typing import Any

from contract_loader import load_dashboard_payload
from report_writer import write_json_report
from validator import validate_contracts


APP_ROOT = Path(__file__).resolve().parent
TEMPLATE_PATH = APP_ROOT / "templates" / "index.html"
OUTPUT_ROOT = APP_ROOT / "_output"
DASHBOARD_PATH = OUTPUT_ROOT / "index.html"
PAYLOAD_PATH = OUTPUT_ROOT / "dashboard_payload.json"


def build_dashboard() -> dict[str, Any]:
    validation = validate_contracts()
    payload = load_dashboard_payload()
    payload["validation"] = validation

    write_json_report(PAYLOAD_PATH, payload)
    _write_dashboard_html(payload)

    return {
        "status": validation.get("status", "UNKNOWN"),
        "dashboard": DASHBOARD_PATH.as_posix(),
        "payload": PAYLOAD_PATH.as_posix(),
        "validation_report": (OUTPUT_ROOT / "validation_report.json").as_posix(),
        "route_count": validation.get("route_count"),
    }


def _write_dashboard_html(payload: dict[str, Any]) -> None:
    template = Template(TEMPLATE_PATH.read_text(encoding="utf-8"))
    embedded_payload = json.dumps(payload, ensure_ascii=False)
    html = template.safe_substitute(embedded_payload=embedded_payload)
    DASHBOARD_PATH.write_text(html, encoding="utf-8")


def main() -> None:
    result = build_dashboard()
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
