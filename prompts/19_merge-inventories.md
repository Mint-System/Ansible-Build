---
title: "Merge inventories"
state: draft
model: 
input_tokens: 
---

# Run 19

Note: @Clanker refers to the "ai agent" (you) who is working on this task.

@Clanker when working on this task, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on the task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

This task requires you to build a script that merges the inventories `odoo` and `nextcloud` into `setup`.

See the `inventories` folder for details.

First prepare the inventories like this:

- Every hosts folder in `inventories/odoo/host_vars` gets an `odoo` suffix. Examples `notus` -> `notus_odoo`, `rhea_upgrade` -> `rhea_odoo_upgrade`
- Every hosts folder in `inventories/nextcloud/host_vars` gets an `nextcloud` suffix. Examples `eos` -> `eos_nextcloud`
- Apply the suffix in `inventories/odoo/hosts.yml`
- Apply the suffix in `inventories/nextcloud/hosts.yml`
- Rename the group `inventories/odoo/group_vars/all` to `inventories/nextcloud/group_vars/odoo`
- Rename the group `inventories/nextcloud/group_vars/all` to `inventories/nextcloud/group_vars/nextcloud`

Then once the "scoping" is finished do this:

- In `inventories/setup/hosts.yml` move all groups of `all` to a new child-group `setup`
- Content of `inventories/odoo/hosts.yml` goes into `inventories/setup/hosts.yml` under a new group `odoo`.
- Content of `inventories/nextcloud/hosts.yml` goes into `inventories/setup/hosts.yml` under a new group `nextcloud`.
- Move folders from `inventories/nextcloud/host_vars` to `inventories/setup/host_vars`
- Move folders from `inventories/odoo/host_vars` to `inventories/setup/host_vars`
- Rename `inventories/setup/group_vars/all` to `inventories/setup/group_vars/setup`
Then I want you to update the playbooks in `plays`.

- Make sure the odoo playbook only targets the odoo group
- Make sure the nextcloud playbook only targets the nextcloud group
- Make sure that setup playbook only targets the setup group
- Make sure that all playbook only targets the setup group

At then end of these process there should be only three folders in `inventories`: `opsone`, `sozialinfo`, `setup`.

The last step is to rename the `inventories/setup` folder to `inventories/mint_system`.

Update the `README.md` to reflect these changes.

## Worklog

@Clanker Add a summary here once the task has been completed.

@Clanker Set frontmatter state to completed and update info about model and token usage.
