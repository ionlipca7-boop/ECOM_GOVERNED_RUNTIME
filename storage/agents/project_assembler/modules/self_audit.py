from pathlib import Path

REQUIRED_FILES = [
    'README.md',
    'project_assembler_agent.py',
    'run_project_assembler.py',
    'profiles/ecom_os_v3_profile.json',
    'modules/__init__.py',
    'modules/safety.py',
    'modules/reporter.py',
    'modules/inventory.py',
    'modules/capability_graph.py',
    'modules/dependency_graph.py',
    'modules/donor_scoring.py',
    'modules/clean_plan.py',
    'modules/validation.py',
    'modules/finish_signal.py',
    'modules/self_audit.py'
]


def run_self_audit(agent_root: Path):
    missing = []
    present = []
    for rel in REQUIRED_FILES:
        path = agent_root / rel
        if path.exists():
            present.append(rel)
        else:
            missing.append(rel)

    return {
        'status': 'PASS_SELF_AUDIT' if not missing else 'BLOCK_SELF_AUDIT_MISSING_FILES',
        'agent_root': str(agent_root),
        'present_count': len(present),
        'missing_count': len(missing),
        'present': present,
        'missing': missing,
        'ready_for_server_transfer': not missing
    }
