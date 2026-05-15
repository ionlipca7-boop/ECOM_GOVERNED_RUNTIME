def build_clean_plan():
    return {
        'status': 'CLEAN_PLAN_READY',
        'rules': [
            'no_delete_without_gate',
            'archive_before_cleanup',
            'quarantine_before_remove',
            'readonly_verify_before_live',
            'no_parallel_branches',
            'single_route_execution'
        ],
        'cleanup_mode': 'audit_first'
    }
