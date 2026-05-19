# ION LOCAL ASSISTANT ARCHITECTURE

## Goal

Build a local Windows-first assistant that saves operator time and keeps every important action under operator control.

## Main Flow

```text
OBSERVE
CLASSIFY
RISK SCORE
DRAFT ACTION
WAIT FOR OPERATOR APPROVAL
EXECUTE ONLY IF ALLOWED
```

## Current Layer

```text
SCAN AND REPORT ONLY
```

## Planned Structure

```text
1_foundation
2_scanners
3_analyzers
4_action_drafts
5_operator_gate
6_optional_local_ai_layer
```

## Local AI Direction

Optional future layer:

- Ollama for local models
- Open Interpreter local mode for controlled local assistance
- no paid cloud API required by default

## Windows Helper Direction

Recommended companion tools:

- Everything for fast file search
- Microsoft PowerToys for Windows productivity
- Czkawka for duplicate finding
- later local dashboard

## Risk Levels

```text
LOW     read report draft
MEDIUM  copy quarantine plan
HIGH    move rename
BLOCKED delete live send publish secrets server
```

## Operator Experience Target

The assistant should reduce manual work:

- read logs
- summarize output
- prepare next CMD block
- organize files
- prepare reports
- generate safe drafts
- wait for approval
