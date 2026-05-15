# Universal Project Assembler Agent

Status: `MODULAR_V3_READY_FOR_SERVER_TRANSFER_AFTER_SELF_AUDIT`

Purpose: scan an existing project read-only, classify files, map capabilities, score reusable donors, prepare a clean build plan, draft validation gates, and produce human-auditable reports.

Bridge note: this copy is stored in `ECOM_GOVERNED_RUNTIME` only as a server-transfer bridge. Canonical project memory remains `ECOM_OS_V3`.

## First profile

`ECOM_OS_V3`

## Architecture

```text
project_assembler_agent.py   # orchestrator
run_project_assembler.py     # CLI runner
profiles/ecom_os_v3_profile.json
modules/
  inventory.py
  capability_graph.py
  dependency_graph.py
  donor_scoring.py
  clean_plan.py
  validation.py
  reporter.py
  safety.py
  finish_signal.py
  self_audit.py
```

## Safety

Default mode is read-only.

Blocked by default:

- marketplace write actions
- cleanup/delete/move/quarantine moves
- bot restart
- secret value printing
- old product mixing
- active runtime patching

## Server layout

```text
SOURCE_RUNTIME_READONLY=/home/ionlipca7/runtime_eco_v1
ASSEMBLER_WORKSPACE=/home/ionlipca7/ecom_project_assembler
CLEAN_BUILD_TARGET=/home/ionlipca7/ecom_clean_build_current
```

## Run on server later

Self-audit first:

```bash
cd /home/ionlipca7/runtime_eco_v1
python3 storage/agents/project_assembler/run_project_assembler.py --profile storage/agents/project_assembler/profiles/ecom_os_v3_profile.json --mode self_audit
```

Full read-only workflow:

```bash
cd /home/ionlipca7/runtime_eco_v1
python3 storage/agents/project_assembler/run_project_assembler.py --profile storage/agents/project_assembler/profiles/ecom_os_v3_profile.json --mode full_readonly
```

## Main outputs

```text
inventory_files.jsonl
inventory_index.json
secret_references_no_values.json
capability_map_current.json
capability_graph_current.json
capability_gaps_current.json
donor_scoreboard_current.json
selected_donors_current.json
quarantine_boundary_current.json
forbidden_paths_current.json
failed_attempts_current.json
clean_assembly_plan_current.json
clean_build_file_manifest_current.json
clean_build_dependency_map_current.json
clean_build_secret_reference_map_no_values.json
validation_plan_current.json
validation_gates_current.json
dry_run_sequence_current.json
dry_validation_report_current.json
project_assembler_report_short_current.md
project_assembler_report_full_current.json
next_actions_current.json
FINISH_ASSEMBLER_READY_FOR_HUMAN_AUDIT.json
```

## Finish rule

If `FINISH_ASSEMBLER_READY_FOR_HUMAN_AUDIT.json` exists, the agent stopped safely and waits for Ion human audit before any physical clean build or runtime action.
