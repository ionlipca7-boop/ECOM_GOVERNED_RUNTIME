import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

SECRET_HINTS = ['token', 'secret', 'client_secret', 'refresh', '.env', 'credential', 'password']
ARCHIVE_HINTS = ['archive', 'backup', '.bak', 'old_', '_old', 'tmp', 'temp', 'log']
FAIL_HINTS = ['failed', 'rollback', 'error', 'broken']
FORBIDDEN_HINTS = ['forbidden', 'do_not_use', 'bad_pattern']
PASS_HINTS = ['pass', 'ready', 'verified', 'validated', 'current']

CAPABILITY_RULES = {
    'telegram': ['telegram', 'bot.py', 'cockpit', 'keyboard', 'callback', 'tmux'],
    'url_intake': ['url', 'intake', 'clean_product_slot', 'source_url', 'aliexpress'],
    'field_sources': ['field_source', 'ecom_sources', 'trace_current_product'],
    'photo_pipeline': ['photo', 'image', 'gallery', 'eps', 'picture'],
    'description_html': ['description', 'html', 'beschreibung'],
    'category_aspects': ['category', 'aspect', 'specifics', 'item_specifics'],
    'ebay_readonly': ['getmyebayselling', 'readonly', 'inventory_fetcher', 'sell_inventory_fetcher'],
    'ebay_write_route': ['publish', 'revise', 'offer', 'bulk_update', 'createorreplace'],
    'listing_registry': ['registry', 'listing', 'session'],
    'final_critic': ['critic', 'final_check', 'quality_gate'],
    'memory_system': ['current_pointer', 'working_step_pointer', 'ledger', 'archive', 'adr', 'route_map'],
    'cleanup_tools': ['cleanup', 'quarantine', 'delete', 'move'],
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def capability_tags(relative_path: str):
    low = relative_path.lower()
    tags = []
    for capability, hints in CAPABILITY_RULES.items():
        if any(h in low for h in hints):
            tags.append(capability)
    return sorted(set(tags)) or ['unknown']


def risk_flags(relative_path: str):
    low = relative_path.lower()
    flags = []
    if any(h in low for h in SECRET_HINTS):
        flags.append('SECRET_REFERENCE_RISK_PATH_ONLY')
    if any(h in low for h in ['publish', 'revise', 'delete', 'cleanup', 'move', 'restart']):
        flags.append('ACTION_RISK_REQUIRES_GATE')
    if '1005005210545584' in low:
        flags.append('OLD_PRODUCT_DONOR_BOUNDARY')
    return flags


def classify(relative_path: str, tags, flags):
    low = relative_path.lower()
    if any(h in low for h in FORBIDDEN_HINTS):
        return 'FORBIDDEN_PATH'
    if any(h in low for h in FAIL_HINTS):
        return 'FAILED_ATTEMPT_NO_ACTIVE_WRITE'
    if any(h in low for h in ARCHIVE_HINTS):
        return 'ARCHIVE_NOISE'
    if 'ACTION_RISK_REQUIRES_GATE' in flags:
        return 'QUARANTINE_CANDIDATE'
    if any(h in low for h in PASS_HINTS) or 'memory_system' in tags:
        return 'WORKING_DONOR'
    return 'UNKNOWN'


def scan_inventory(source_runtime: Path, workspace: Path):
    if not source_runtime.exists():
        raise FileNotFoundError(f'Source runtime not found: {source_runtime}')
    inventory = []
    secret_refs = []
    inventory_path = workspace / 'inventory_files.jsonl'
    with inventory_path.open('w', encoding='utf-8') as out:
        for path in sorted(source_runtime.rglob('*')):
            if not path.is_file():
                continue
            rel = str(path.relative_to(source_runtime))
            tags = capability_tags(rel)
            flags = risk_flags(rel)
            item = {
                'path': str(path),
                'relative_path': rel,
                'sha256': sha256_file(path),
                'size': path.stat().st_size,
                'suffix': path.suffix,
                'modified_utc': datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(),
                'capability_tags': tags,
                'classification': classify(rel, tags, flags),
                'risk_flags': flags,
                'status': 'NOT_TESTED_READONLY_INVENTORY_ONLY'
            }
            out.write(json.dumps(item, ensure_ascii=False) + '\n')
            inventory.append(item)
            if 'SECRET_REFERENCE_RISK_PATH_ONLY' in flags:
                secret_refs.append({'path': item['path'], 'reason': 'path/name suggests secret reference; value not read or printed'})
    counts = defaultdict(int)
    for item in inventory:
        counts[item['classification']] += 1
    return inventory, {'inventory_file': str(inventory_path), 'inventory_count': len(inventory), 'classification_counts': dict(counts), 'secret_references': secret_refs}
