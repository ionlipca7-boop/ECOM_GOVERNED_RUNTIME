FORBIDDEN_ACTIONS = [
    'marketplace_write',
    'cleanup',
    'delete',
    'move',
    'quarantine_move',
    'secret_print',
    'runtime_restart',
    'old_product_mixing'
]


def readonly_guard():
    return {
        'status': 'READ_ONLY_FIRST',
        'forbidden_actions': FORBIDDEN_ACTIONS,
        'note': 'Assembler runs in read-only mode until a separate explicit gate is approved.'
    }
