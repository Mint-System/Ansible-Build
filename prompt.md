---
title: "multiple connections for forgejo runner"
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

# multiple connections for forgejo runner

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read the `AGENTS.md` and `README.md` to get an understanding of the project
- Read entire task section and prepare a list of todos
- Update the todo list while working on task

## Task


I want to support multiple registrations for the `forgejo_runner` role.

This requires refactoring `roles/forgejo_runner/templates/config.yaml`.

Instead of having `forgejo_runner_instance_url`, `forgejo_runner_instance_uuid` and `forgejo_runner_instance_token` vars I want one `forgejo_runner_connections` var.

Update the role to support this var. Setup a default `forgejo_runner_connections: "{{ vault_forgejo_runner_connections }}"`.

Update the existing host vars `inventories/mint_system/host_vars/dione/vars.yaml` by moving the existing connection into `inventories/mint_system/host_vars/dione/vault.yaml`.

Use `decrypt-file` to edit the vault file.

@Clanker When task is completed set frontmatter state to review. Prompt the author to verify the results.

## Worklog

@Clanker Add a summary here once the task has been completed.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness, provider and model. If you have access to session info also add token count.
