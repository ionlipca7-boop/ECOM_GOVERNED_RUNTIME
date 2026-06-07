from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONTRACT_ROOT = PROJECT_ROOT / "storage" / "contracts" / "v7_3c"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_routes(contract_root: Path = CONTRACT_ROOT) -> list[dict[str, Any]]:
    registry_path = contract_root / "runtime_registry" / "route_registry_v7_3c.json"
    registry = read_json(registry_path)
    routes: list[dict[str, Any]] = []

    for item in registry.get("routes", []):
        route_path = contract_root / item["contract_file"]
        route = read_json(route_path)
        route["_contract_file"] = item["contract_file"]
        routes.append(route)

    return routes


def load_dashboard_payload(contract_root: Path = CONTRACT_ROOT) -> dict[str, Any]:
    registry = read_json(contract_root / "runtime_registry" / "route_registry_v7_3c.json")
    button_map = read_json(contract_root / "telegram" / "telegram_button_map_v7_3c.json")

    return {
        "version": registry.get("version", "V7.3C"),
        "status": registry.get("status"),
        "server_transfer": registry.get("server_transfer"),
        "global_rules": registry.get("global_rules", []),
        "button_map": button_map.get("main_menu", []),
        "routes": load_routes(contract_root),
    }
