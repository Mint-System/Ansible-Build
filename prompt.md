---
title: "Remove users on test project cleanup"
author: "Janik von Rotz <login@janikvonrotz.ch>"
action: implement
state: completed
date_completed: 2026-11-07
harness: pi
provider: mistral
model: deepseek-v4-1-flash-1017
input_tokens: 132883
output_tokens: 11986
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

The `iam` cleanup task only removes users with `state: absent`, and `test-project cleanup` did not pass the `iam` tag. A first attempt added a `cleanup_iam_remove_users` flag to the cleanup role; the author rejected that, so the role stays untouched and the users and groups are removed manually.

Change:

- `task`: `test-project cleanup` runs ad-hoc `ansible.builtin.user` and `ansible.builtin.group` commands after the cleanup playbook, following the existing pattern in `test-scripts cleanup`. Users are removed with `remove=yes force=yes`, groups without.
- The names are read from the inventory with `ansible-inventory --host localhost` and `jq`, so `iam_users` and `iam_groups` stay the single source of truth.

No role, playbook or inventory file was modified.

Verification:

- `bash -n task` passes.
- `ansible-inventory --host localhost` resolves `iam_users` to `admin operator` and `iam_groups` to `wheel operators`.
- All four ad-hoc commands resolve to `CHANGED` in `--check` mode against `test_inventory`.

Note: the ad-hoc calls pass `-e ansible_python_interpreter=$PWD/.venv/bin/python`. The value in `test_inventory/hosts.yml` is relative to `playbook_dir`, which does not resolve for ad-hoc commands.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness, provider and model. If you have access to session info also add token count.
