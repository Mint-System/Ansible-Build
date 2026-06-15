---
title: "Show function for list-hosts"
state: completed
---

# Run 15

Note: @Clanker refers to the "ai agent" (you) who is working on this task.

@Clanker when working on this task, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on the task

## Context

Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

The command `list-hosts` does not have a row `function`. Add it.

Add a second param `[grep]`. I want run `task list-host inventories Busco` and get table with grep filtered rows.

## Worklog

Updated the `list-hosts` command in the `task` file:

1. **Added `Function` column**: Extracted the `function` field from inventory host entries and added it as a new column in the output table. The column is displayed in both the "with customer" and "without customer" inventory branches.
2. **Added optional `[grep]` parameter**: The command now accepts a second argument to filter rows case-insensitively (e.g., `task list-hosts inventories/setup Busco`).
3. **Fixed `set -e` bug**: Added `|| true` to the customer detection grep to prevent the script from silently exiting when processing inventories without customer fields.

The help table entry was also updated to reflect the new signature: `list-hosts [path] [grep]`.
