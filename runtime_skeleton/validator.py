from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from report_writer import write_json_report


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONTRACT_ROOT = PROJECT_ROOT / "storage" / "contracts" / "v7_3c"
OUTPUT_PATH = Path(__file__).resolve().parent / "_output" / "validation_report.json"
ARCHIVE_PATH = (
    PROJECT_ROOT
    / "storage"
    / "memory_v2"
    / "archive"
    / "V7_3C_FULL_8_BUTTON_ROUTE_ARCHIVE_20260606T163359Z.md"
)

REQUIRED_ROUTE_FIELDS = [
    "route_id",
    "button",
    "callback",
    "role",
    "purpose_ru",
    "inputs",
    "outputs",
    "agents",
    "blocks",
    "handoffs",
    "rules",
]

REQUIRED_FILES = [
    "runtime_registry/route_registry_v7_3c.json",
    "telegram/telegram_button_map_v7_3c.json",
    "telegram/callback_contract_v7_3c.json",
    "final_gates/final_gate_contract_v7_3c.json",
]

SECRET_MARKERS = ("token", "secret", "password", "api_key")


def _relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def validate_contracts(
    contract_root: Path = CONTRACT_ROOT,
    output_path: Path = OUTPUT_PATH,
) -> dict[str, Any]:
    missing: list[str] = []
    warnings: list[str] = []
    parse_errors: list[str] = []

    if not contract_root.exists():
        missing.append(str(contract_root))
        report = _build_report("BLOCK", 0, 0, 0, missing, warnings)
        return _write(report, output_path)

    all_files = sorted(path for path in contract_root.rglob("*") if path.is_file())
    json_files = sorted(path for path in all_files if path.suffix.lower() == ".json")
    route_files = sorted((contract_root / "routes").glob("route_*.json"))

    if len(route_files) != 8:
        warnings.append(f"Expected 8 route JSON files, found {len(route_files)}")

    if not ARCHIVE_PATH.exists():
        missing.append(
            "Route archive is missing: "
            "storage/memory_v2/archive/V7_3C_FULL_8_BUTTON_ROUTE_ARCHIVE_20260606T163359Z.md"
        )

    for required in REQUIRED_FILES:
        if not (contract_root / required).exists():
            missing.append(required)

    parsed: dict[Path, Any] = {}
    for path in json_files:
        try:
            parsed[path] = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            parse_errors.append(f"{_relative(path, contract_root)}: {exc}")

    for route_file in route_files:
        route = parsed.get(route_file)
        if not isinstance(route, dict):
            continue

        for field in REQUIRED_ROUTE_FIELDS:
            if field not in route:
                missing.append(f"{_relative(route_file, contract_root)}::{field}")

        callback = str(route.get("callback", ""))
        if len(callback) > 32:
            warnings.append(
                f"{_relative(route_file, contract_root)} callback is longer than 32 chars"
            )

        route_id = str(route.get("route_id", ""))
        if route_id and route_file.stem != route_id:
            warnings.append(
                f"{_relative(route_file, contract_root)} route_id does not match file stem"
            )

        for key_path in _find_secret_like_keys(route):
            warnings.append(
                f"{_relative(route_file, contract_root)} contains secret-like key '{key_path}'"
            )

    warnings.extend(parse_errors)
    status = "PASS" if not missing and not parse_errors and len(route_files) == 8 else "BLOCK"
    report = _build_report(
        status,
        file_count=len(all_files),
        json_count=len(json_files),
        route_count=len(route_files),
        missing=missing,
        warnings=warnings,
    )
    return _write(report, output_path)


def _build_report(
    status: str,
    file_count: int,
    json_count: int,
    route_count: int,
    missing: list[str],
    warnings: list[str],
) -> dict[str, Any]:
    return {
        "status": status,
        "file_count": file_count,
        "json_count": json_count,
        "route_count": route_count,
        "missing": missing,
        "warnings": warnings,
        "checked_utc": datetime.now(timezone.utc).isoformat(),
    }


def _find_secret_like_keys(value: Any, prefix: str = "") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, nested in value.items():
            key_text = str(key)
            path = f"{prefix}.{key_text}" if prefix else key_text
            lower_key = key_text.lower()
            if any(marker in lower_key for marker in SECRET_MARKERS):
                found.append(path)
            found.extend(_find_secret_like_keys(nested, path))
    elif isinstance(value, list):
        for index, nested in enumerate(value):
            found.extend(_find_secret_like_keys(nested, f"{prefix}[{index}]"))
    return found


def _write(report: dict[str, Any], output_path: Path) -> dict[str, Any]:
    write_json_report(output_path, report)
    return report


if __name__ == "__main__":
    result = validate_contracts()
    print(json.dumps(result, ensure_ascii=False, indent=2))
