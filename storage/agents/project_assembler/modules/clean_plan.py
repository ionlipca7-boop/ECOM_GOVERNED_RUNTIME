from collections import defaultdict


def build_clean_assembly_plan(selected_donors, source_runtime, clean_build_target):
    selected_by_capability = defaultdict(list)
    for donor in selected_donors:
        for tag in donor.get('capability_tags', []):
            selected_by_capability[tag].append(donor['relative_path'])

    return {
        'status': 'PASS_CLEAN_ASSEMBLY_PLAN_DRAFTED_NO_FILES_COPIED',
        'clean_build_target': str(clean_build_target),
        'source_runtime_readonly': str(source_runtime),
        'selected_by_capability': {k: v[:20] for k, v in selected_by_capability.items()},
        'rules': [
            'Do not copy secrets; reference paths only.',
            'Do not write into source runtime during assembly planning.',
            'Promote one donor per capability only after human approval.',
            'Keep quarantine/archive/noise out of clean build.',
            'Physical file copy requires a separate clean build gate.'
        ],
        'next': 'human_review_then_physical_clean_build_gate'
    }


def build_clean_manifest(selected_donors):
    return {
        'status': 'DRAFT_SELECTED_DONORS_ONLY_REVIEW_REQUIRED',
        'items': selected_donors
    }


def build_secret_reference_map_note():
    return {
        'status': 'PATH_REFERENCES_ONLY_NO_VALUES',
        'note': 'Use secret_references_no_values.json; secret values are not read or copied.'
    }
