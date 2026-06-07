# ECOM OS V7.3C Local Runtime Skeleton

Local file-based dashboard for reviewing the eight independent ECOM OS V7.3C route-blocks.

## Generate

```powershell
python runtime_skeleton/app.py
```

This writes:

- `runtime_skeleton/_output/index.html`
- `runtime_skeleton/_output/dashboard_payload.json`
- `runtime_skeleton/_output/validation_report.json`

The dashboard is a static local HTML file. It does not start a server, patch Telegram, call eBay, restart services, delete files, commit, or push.

## What It Shows

- 8 route cards/buttons
- route status
- route purpose
- safe next action
- global Back / Home / Stop rules
- inputs, outputs, agents, blocks, handoffs, and contract rules
- validation status and source paths

## Validate Only

```powershell
python runtime_skeleton/validator.py
```

The validator reads `storage/contracts/v7_3c/` and writes `runtime_skeleton/_output/validation_report.json`.
