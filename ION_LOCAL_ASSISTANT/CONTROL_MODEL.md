# ION LOCAL ASSISTANT CONTROL MODEL

## How operator controls it

V1 control is simple and safe.

Operator opens a Windows CMD launcher and selects an action by number.

## Control levels

### Level 1: CMD menu

```text
ION_CONTROL_MENU.cmd
```

Actions:

```text
1 Scan folder
2 Extended scan
3 Project detector
4 Open reports folder
5 Exit
```

### Level 2: Desktop shortcut

A Windows shortcut can be created later.

Double click:

```text
ION_CONTROL_MENU.cmd
```

### Level 3: ChatGPT-guided mode

Operator can paste report output into ChatGPT.

ChatGPT can explain next safe action and prepare CMD blocks.

### Level 4: Future local UI

Optional future:

- local dashboard
- buttons
- file picker
- approval screen

## Current rule

No background service.
No hidden automation.
No silent actions.

Operator starts it manually.
