def build_validation_plan(forbidden_actions):
    return {
        'status': 'PASS_VALIDATION_PLAN_DRAFTED',
        'sequence': [
            'python compile checks for selected .py donors',
            'import checks in clean build after physical build gate',
            'Telegram dry/operator check',
            'URL intake dry test',
            'field source dry test',
            'photo/source dry test',
            'German HTML dry test',
            'category/aspects dry test',
            'external marketplace read-only check only after separate gate',
            'final critic dry-run',
            'human audit'
        ],
        'blocked_until_separate_gate': forbidden_actions
    }


def build_validation_gates(forbidden_actions):
    return {
        'status': 'PASS_VALIDATION_GATES_DEFINED',
        'gates': forbidden_actions
    }


def build_dry_validation_placeholder():
    return {
        'status': 'NOT_RUN_YET_PLAN_ONLY',
        'next': 'run validations after clean build gate'
    }
