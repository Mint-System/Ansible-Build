---
commit_ref:
title: "Remove users on test project cleanup"
author: "Janik von Rotz <login@janikvonrotz.ch>"
action: implement
state: draft
date_completed: YYYY-MM-DD
harness:
provider:
model:
input_tokens:
output_tokens:
---

# Remove users on test project cleanup

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read the `AGENTS.md` and `README.md` to get an understanding of the project
- Read entire task section and prepare a list of todos
- Update the todo list while working on task

## Task

When running `test-project cleanup` it removes the containers, but not the users of the `iam` role.

The users can only be removed explicitly by setting `state: absent`.

The relevant inventory is `test_inventory/host_vars/localhost.yml`.

Add ansible cleanup command for iam and set this attribute temporary.

@Clanker When task is completed set frontmatter state to review. Prompt the author to verify the results.

## Worklog

@Clanker Add a summary here once the task has been completed.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness, provider and model. If you have access to session info also add token count.
