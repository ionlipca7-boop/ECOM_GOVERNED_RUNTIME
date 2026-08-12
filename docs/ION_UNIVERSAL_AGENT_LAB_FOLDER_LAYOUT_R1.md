# ION UNIVERSAL AGENT LAB — FOLDER LAYOUT R1

Recommended Windows root (isolated beside production):

D:\ION_UNIVERSAL_AGENT_LAB

Do not place lab runtime inside D:\ECOM_OS_PRO_LOCAL_OPERATOR_BUILD.

## Proposed layout

00_CONTROL\
  current_status.json
  approvals\
  task_queue\
  leases\
  audit\

01_PROJECT_MIRRORS\
  ecom_os_readonly\
  future_projects\

02_MEMORY\
  knowledge_lab_adapter\
  iwe_adapter\
  context_packets\
  decisions\
  debts\
  learnings\
  session_checkpoints\

03_SKILLS\
  registry\
  ecom-context-load\
  ecom-ui-canon\
  ecom-workflow-map\
  ecom-screen-contract\
  ecom-design-consultation\
  ecom-design-review\
  ecom-responsive-qa\
  ecom-browser-qa\
  ecom-investigate\
  ecom-cross-model-review\
  ecom-context-save\
  ecom-context-restore\
  ecom-learn\
  ecom-health\
  ecom-security-review\

04_AGENTS\
  coordinator\
  ui_architect\
  logic_guardian\
  browser_qa\
  responsive_qa\
  investigator\
  critic\
  memory_curator\
  future_specialists\

05_ORCHESTRATOR\
  mailbox\
  scheduler\
  router\
  state\
  checkpoints\
  provider_adapters\

06_SAFE_AI_GATE\
  policies\
  allowlists\
  redaction\
  provider_profiles\
  audit\

07_BROWSER_LAB\
  profiles\
  sessions\
  screenshots\
  visual_checkpoints\
  dom_maps\
  responsive_results\
  candidates\

08_UI_FACTORY\
  canon\
  workflow_maps\
  screen_contracts\
  design_system\
  concept_A\
  concept_B\
  concept_C\
  scorecards\
  accepted_candidate\

09_TESTS\
  fixtures\
  static\
  regression\
  adversarial\
  e2e_nonlive\
  recovery\

10_INTEGRATION_PACKAGES\
  pending\
  approved\
  applied_receipts\
  rollback\

11_TOOLS\
  launchers\
  diagnostics\
  local_dependencies\

12_REPORTS\
  current\
  history\

## Existing Knowledge Lab relationship

Existing D:\ECOM_KNOWLEDGE_LAB remains its own knowledge subsystem. The new lab should initially consume it through its existing mirror/READONLY guard instead of moving or rewriting it.

Knowledge roles remain:
Browser Dashboard = quick project state
Obsidian = human visual knowledge/map
IWE = machine retrieval/graph
READONLY Guard = safe agent-facing access

The Universal Agent Lab adds orchestration, skills, design/browser factory, safe AI routing, durable multi-agent state and controlled integration packages around that existing memory subsystem.

## Migration rule

Nothing is physically moved from production or Knowledge Lab during phases 0-10. Use references, read-only adapters, mirrors and exported context packets. Copy only lab-owned fixtures/candidates/evidence.
