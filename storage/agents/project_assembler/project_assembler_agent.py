import json
from pathlib import Path
from datetime import datetime, timezone

from modules.inventory import scan_inventory
from modules.capability_graph import build_capability_graph
from modules.dependency_graph import build_dependency_graph
from modules.donor_scoring import score_donors
from modules.clean_plan import (
    build_clean_assembly_plan,
    build_clean_manifest,
    build_secret_reference_map_note,
)
from modules.validation import (
    build_validation_plan,
    build_validation_gates,
    build_dry_validation_placeholder,
)
from modules.finish_signal import build_finish_signal
from modules.reporter import write_json, write_text
from modules.safety import readonly_guard


class ProjectAssemblerAgent:
    """Modular read-only Project Assembler Agent."""

    def __init__(self, profile_path: str):
        self.profile_path = Path(profile_path)
        self.profile = json.loads(self.profile_path.read_text(encoding='utf-8'))
        self.workspace = Path(self.profile['assembler_workspace'])
        self.source_runtime = Path(self.profile['source_runtime_readonly'])
        self.clean_build_target = Path(self.profile['clean_build_target'])
        self.workspace.mkdir(parents=True, exist_ok=True)
        self.now = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
        self.inventory = []
        self.capability_result = {}
        self.donor_result = {}

    def _write_json(self, name: str, data):
        return write_json(self.workspace, name, data)

    def _write_text(self, name: str, text: str):
        return write_text(self.workspace, name, text)

    def inventory_scan(self):
        self.inventory, result = scan_inventory(self.source_runtime, self.workspace)
        self._write_json('inventory_index.json', {
            'status': 'PASS_READONLY_INVENTORY_INDEX',
            'updated_utc': self.now,
            'source_runtime': str(self.source_runtime),
            'count': result['inventory_count'],
            'classification_counts': result['classification_counts'],
            'sample_paths': [x['relative_path'] for x in self.inventory[:200]],
        })
        self._write_json('secret_references_no_values.json', {
            'status': 'SECRET_REFERENCES_PATH_ONLY_NO_VALUES',
            'count': len(result['secret_references']),
            'items': result['secret_references'][:300],
        })
        return result

    def build_capability_outputs(self):
        self.capability_result = build_capability_graph(
            self.inventory,
            self.profile.get('expected_capabilities', []),
        )
        self._write_json('capability_map_current.json', {
            'status': 'PASS_CAPABILITY_MAP_BUILT',
            'capabilities': self.capability_result['capability_map'],
        })
        self._write_json('capability_graph_current.json', {
            'status': 'PASS_CAPABILITY_GRAPH_BUILT',
            **self.capability_result['capability_graph'],
        })
        self._write_json('capability_gaps_current.json', {
            'status': 'PASS_CAPABILITY_GAPS_BUILT',
            'gaps': self.capability_result['gaps'],
        })
        self._write_json('clean_build_dependency_map_current.json', build_dependency_graph())
        return self.capability_result

    def build_donor_outputs(self):
        self.donor_result = score_donors(self.inventory)
        self._write_json('donor_scoreboard_current.json', {
            'status': 'PASS_DONOR_SCOREBOARD_BUILT',
            'items': self.donor_result['scoreboard'][:1000],
        })
        self._write_json('selected_donors_current.json', {
            'status': 'PASS_SELECTED_DONORS_CANDIDATE_LIST_BUILT_REVIEW_REQUIRED',
            'items': self.donor_result['selected_donors'],
        })
        self._write_json('quarantine_boundary_current.json', {
            'status': 'PASS_QUARANTINE_BOUNDARY_LOGICAL_ONLY',
            'items': self.donor_result['quarantine'],
        })
        self._write_json('forbidden_paths_current.json', {
            'status': 'PASS_FORBIDDEN_PATHS_LOGICAL_ONLY',
            'items': self.donor_result['forbidden'],
        })
        self._write_json('failed_attempts_current.json', {
            'status': 'PASS_FAILED_ATTEMPTS_LOGICAL_ONLY',
            'items': self.donor_result['failed'],
        })
        return self.donor_result

    def build_clean_outputs(self):
        selected = self.donor_result.get('selected_donors', [])
        self._write_json('clean_assembly_plan_current.json', build_clean_assembly_plan(selected, self.source_runtime, self.clean_build_target))
        self._write_json('clean_build_file_manifest_current.json', build_clean_manifest(selected))
        self._write_json('clean_build_secret_reference_map_no_values.json', build_secret_reference_map_note())

    def build_validation_outputs(self):
        forbidden = self.profile.get('forbidden', [])
        plan = build_validation_plan(forbidden)
        self._write_json('validation_plan_current.json', plan)
        self._write_json('validation_gates_current.json', build_validation_gates(forbidden))
        self._write_json('dry_run_sequence_current.json', plan)
        self._write_json('dry_validation_report_current.json', build_dry_validation_placeholder())

    def build_final_reports(self, inventory_result):
        capabilities_found = list(self.capability_result.get('capability_map', {}).keys())
        selected_count = len(self.donor_result.get('selected_donors', []))
        summary = {
            'status': 'ASSEMBLER_FULL_READONLY_WORKFLOW_COMPLETE',
            'updated_utc': self.now,
            'profile': self.profile.get('project_name'),
            'safety': readonly_guard(),
            'inventory_count': inventory_result['inventory_count'],
            'classification_counts': inventory_result.get('classification_counts', {}),
            'capabilities_found': capabilities_found,
            'selected_donor_candidates': selected_count,
            'outputs_dir': str(self.workspace),
            'next': 'Ion human audit, then decide whether to open physical clean build gate',
        }
        self._write_json('project_assembler_report_full_current.json', summary)
        self._write_json('next_actions_current.json', {
            'status': 'NEXT_ACTIONS_READY',
            'actions': [
                'Review inventory_index.json',
                'Review capability_map_current.json',
                'Review selected_donors_current.json',
                'Review clean_assembly_plan_current.json',
                'Approve or reject physical clean build gate',
            ],
        })
        self._write_text(
            'project_assembler_report_short_current.md',
            '# Project Assembler Short Report\n\n'
            f"Status: {summary['status']}\n\n"
            f"Inventory count: {summary['inventory_count']}\n\n"
            f"Capabilities found: {', '.join(capabilities_found)}\n\n"
            f"Selected donor candidates: {selected_count}\n\n"
            'Next: human audit before any physical clean build or runtime action.\n',
        )
        self._write_json('FINISH_ASSEMBLER_READY_FOR_HUMAN_AUDIT.json', build_finish_signal())
        return summary

    def run_full_readonly_workflow(self):
        inventory_result = self.inventory_scan()
        self.build_capability_outputs()
        self.build_donor_outputs()
        self.build_clean_outputs()
        self.build_validation_outputs()
        return self.build_final_reports(inventory_result)

    def build_initial_report(self, inventory_result):
        return self._write_json('project_assembler_report_full_current.json', {
            'status': 'ASSEMBLER_READONLY_SCAN_COMPLETE',
            'profile': self.profile.get('project_name'),
            'inventory_count': inventory_result['inventory_count'],
            'next': ['capability_graph', 'donor_scoring', 'clean_build_plan'],
        })
