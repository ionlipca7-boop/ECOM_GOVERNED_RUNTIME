from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONTRACT_ROOT = PROJECT_ROOT / "storage" / "contracts" / "v7_3c"
ARCHIVE_PATH = (
    PROJECT_ROOT
    / "storage"
    / "memory_v2"
    / "archive"
    / "V7_3C_FULL_8_BUTTON_ROUTE_ARCHIVE_20260606T163359Z.md"
)

DISPLAY_ROUTE_TEXT = {
    "route_01_new_product": {
        "button": "01 New Product",
        "purpose": "Create a clean one-product listing package without variants.",
        "safe_next_action": "Collect product evidence, photos, cost, stock, and send the draft to Route 07 before any live action.",
    },
    "route_02_variant_product": {
        "button": "02 Variant Product",
        "purpose": "Build a master product with variant SKUs, quantities, prices, and photos.",
        "safe_next_action": "Confirm the variant matrix and stock per SKU, then hand approval to Route 07.",
    },
    "route_03_listing_studio": {
        "button": "03 Listing Studio",
        "purpose": "Improve listing angles through A/B/C drafts without creating duplicate buyer-intent clones.",
        "safe_next_action": "Compare draft options, keep the evidence read-only, and request Route 07 approval for the selected path.",
    },
    "route_04_marketplace_lifecycle": {
        "button": "04 Marketplace Lifecycle",
        "purpose": "Watch listing health and surface only useful attention signals.",
        "safe_next_action": "Label the listing state, prepare a non-live recommendation, and route decisions through Route 07.",
    },
    "route_05_finance_inventory": {
        "button": "05 Finance / Inventory",
        "purpose": "Maintain the single source of truth for stock, cost, money, and SKU state.",
        "safe_next_action": "Verify receipts, costs, stock counts, and conflicts before allowing any other route to depend on the data.",
    },
    "route_06_product_radar": {
        "button": "06 Product Radar",
        "purpose": "Evaluate product ideas before purchase or listing.",
        "safe_next_action": "Build a read-only research card with evidence, risk, margin, and an Ion decision request.",
    },
    "route_07_decision_center": {
        "button": "07 Decision Center",
        "purpose": "Hold approvals, reports, blocked cases, waiting decisions, and exact action gates.",
        "safe_next_action": "Show the shortest safe decision card and record the exact approval or block marker.",
    },
    "route_08_memory_teacher": {
        "button": "08 Memory / Teacher",
        "purpose": "Maintain autonomous project memory: lessons, rules, archive pointers, evidence, and safety.",
        "safe_next_action": "Store only evidence-backed lessons and route conflicts back to Route 07 for Ion decisions.",
    },
}

GLOBAL_RUNTIME_RULES = [
    {
        "name": "Back",
        "rule": "Return to the previous route card or last safe decision point; do not mutate route state.",
    },
    {
        "name": "Home",
        "rule": "Return to the eight-route dashboard and keep all route blocks independent.",
    },
    {
        "name": "Stop",
        "rule": "Stop the local runtime flow immediately; no live action, restart, delete, Telegram patch, eBay action, commit, or push.",
    },
]


def read_json(path: Path, root: Path = PROJECT_ROOT) -> Any:
    safe_path = _resolve_inside(path, root)
    return json.loads(safe_path.read_text(encoding="utf-8"))


def load_routes(contract_root: Path = CONTRACT_ROOT) -> list[dict[str, Any]]:
    contract_root = _resolve_inside(contract_root, PROJECT_ROOT)
    registry_path = contract_root / "runtime_registry" / "route_registry_v7_3c.json"
    registry = read_json(registry_path, contract_root)
    routes: list[dict[str, Any]] = []

    for item in registry.get("routes", []):
        contract_file = str(item.get("contract_file", ""))
        route_path = _resolve_inside(contract_root / contract_file, contract_root)
        route = read_json(route_path, contract_root)
        route["_contract_file"] = contract_file
        routes.append(_normalize_route(route, item))

    return sorted(routes, key=lambda route: route["route_id"])


def load_dashboard_payload(contract_root: Path = CONTRACT_ROOT) -> dict[str, Any]:
    contract_root = _resolve_inside(contract_root, PROJECT_ROOT)
    registry = read_json(
        contract_root / "runtime_registry" / "route_registry_v7_3c.json",
        contract_root,
    )
    button_map = read_json(
        contract_root / "telegram" / "telegram_button_map_v7_3c.json",
        contract_root,
    )

    archive = load_archive_summary()
    routes = load_routes(contract_root)

    return {
        "version": registry.get("version", "V7.3C"),
        "status": registry.get("status", "unknown"),
        "server_transfer": registry.get("server_transfer", "unknown"),
        "source_paths": {
            "contracts": _relative(contract_root),
            "archive": _relative(ARCHIVE_PATH),
        },
        "archive": archive,
        "global_rules": GLOBAL_RUNTIME_RULES,
        "contract_rules": registry.get("global_rules", []),
        "button_map": button_map.get("main_menu", []),
        "routes": routes,
    }


def load_archive_summary(archive_path: Path = ARCHIVE_PATH) -> dict[str, Any]:
    if not archive_path.exists():
        return {
            "status": "missing",
            "path": _relative(archive_path),
            "summary": "Route archive was requested but is not present in this checkout.",
        }

    archive_path = _resolve_inside(archive_path, PROJECT_ROOT)
    text = archive_path.read_text(encoding="utf-8", errors="replace")
    headings = [
        line.strip("# ").strip()
        for line in text.splitlines()
        if line.startswith("#") and line.strip("# ").strip()
    ]
    return {
        "status": "loaded",
        "path": _relative(archive_path),
        "line_count": len(text.splitlines()),
        "headings": headings[:12],
    }


def _normalize_route(route: dict[str, Any], registry_item: dict[str, Any]) -> dict[str, Any]:
    route_id = str(route.get("route_id") or registry_item.get("route_id"))
    display = DISPLAY_ROUTE_TEXT.get(route_id, {})
    blocks = route.get("blocks") if isinstance(route.get("blocks"), list) else []

    status = "ready_for_local_review"
    if any("missing_route07_approval" == str(block) for block in blocks):
        status = "blocked_until_route_07_approval"
    elif blocks:
        status = "guarded_by_contract_blocks"

    normalized = dict(route)
    normalized.update(
        {
            "route_id": route_id,
            "button": display.get("button", route.get("button", route_id)),
            "raw_button": route.get("button"),
            "purpose": display.get("purpose", route.get("purpose_ru", "")),
            "raw_purpose_ru": route.get("purpose_ru", ""),
            "safe_next_action": display.get(
                "safe_next_action",
                "Review contract inputs and route any live decision through Route 07.",
            ),
            "status": status,
            "contract_file": route.get("_contract_file") or registry_item.get("contract_file"),
        }
    )
    return normalized


def _resolve_inside(path: Path, root: Path) -> Path:
    resolved_root = root.resolve()
    resolved_path = path.resolve()
    if resolved_path != resolved_root and resolved_root not in resolved_path.parents:
        raise ValueError(f"Refusing to read outside workspace root: {resolved_path}")
    return resolved_path


def _relative(path: Path) -> str:
    try:
        return path.resolve().relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return str(path)
