# ION LOCAL ASSISTANT SPEC V0

## Purpose

ION Local Assistant is a local Windows-first order dispatcher.

It helps the operator understand and organize local files, photos, reports and project folders.

## Current Scope

```text
V0 = DRY_RUN_ONLY
```

V0 does not modify user files.

## Main Jobs

1. Scan a selected folder.
2. Build file inventory.
3. Detect exact duplicates by SHA256.
4. Group files by extension/type.
5. Detect large files.
6. Detect empty folders.
7. Export machine-readable JSON report.
8. Export human-readable TXT report.

## Inputs

- local Windows folder path;
- optional scan depth;
- optional ignored folders.

## Outputs

```text
storage/reports/<timestamp>_folder_scan.json
storage/reports/<timestamp>_folder_scan.txt
```

## V0 Commands

```text
python scripts/scan_folder_report_v0.py --path "C:\\path\\to\\folder"
```

## V0 Guarantees

- no delete;
- no move;
- no rename;
- no network action;
- no server access;
- no eBay access;
- no secret reading by design.

## Future Modes

```text
V1 = Quarantine plan only
V2 = Approved quarantine move
V3 = Local UI
V4 = Optional local LLM
```

## Operator Control

All dangerous actions require explicit operator approval.

The assistant must always show:

- what it found;
- what it proposes;
- what it will not touch;
- what requires approval.
