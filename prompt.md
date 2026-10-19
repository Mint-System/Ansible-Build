---
title: "Delete views from thirdparty modules in Odoo upgrade"
author: "Janik von Rotz <login@janikvonrotz.ch>"
action: implement
state: draft
date_completed: YYYY-MM-DD
harness:
model:
input_tokens:
output_tokens:
---

# Delete views from thirdparty modules in Odoo upgrade

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

In `bin/upgrade-odoo` I would like to add a new task to delete `ir.ui.view` rows in the upgraded Odoo database for a list of thirdparty modules.

Introduce a new env var `ODOO_ADDONS_RESET`. The content is show with `info` command before `Init Addons:` as `Reset Addons`.

Create a new step `reset-views`. This commands pipes a Python script into the Odoo shell connected to target Odoo instance.

### docker-odoo-delete-views

Create a bash script in `roles/odoo/files`. 

The script looks up the `ir.ui.view` entries in `ir.module.data` based on the `module` name.

See `docker-odoo-clear-views` for reference.

It support `-m` for a list of modules.

Then it deletes the view records and shows how many records have been deleted.

### other

Delete the `docker-odoo-clear-views`, `docker-odoo-clear-rules`, `docker-odoo-localhost-restore` abnd `docker-odoo-patch` scripts.

Rename `docker-odoo-clear-assets` to `docker-odoo-delete-assets`

@Clanker When task is completed set frontmatter state to review. Prompt the author to verify the results.

## Worklog

@Clanker Add a summary here once the task has been completed.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness and model. If you have access to session info also add token count.
