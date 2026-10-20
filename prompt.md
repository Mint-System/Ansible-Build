---
title: "Create Forgejo Runner role"
author: "Janik von Rotz <login@janikvonrotz.ch>"
action: implement
state: draft
date_completed: YYYY-MM-DD
harness:
model:
input_tokens:
output_tokens:
---

# Create Forgejo Runner role

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

I would like to deploy a forgejo runner container that can spawn job with docker. Docker in Docker (DinD) or access to the host docker driver.

I already created Kubernetes Helm chart `~/Kubernetes-Build/forgejo-runner`. Compared to this the Ansible role is simple.

Make a copy of the `coturn` role. Create a env var `forgejo_runner_instance_token` with default `vault_forgejo_runner_instance_token`.

Otherwise not further non-default vars are required.

Run `update-docs`.

I will add a logo.

### Testing

I will deploy the runner to the `dione` server. You can prepare the vars (hostname, description, ...).

Then I will generate the secret with with `task generate-encrypted-string` and deploy the runner.

@Clanker When task is completed set frontmatter state to review. Prompt the author to verify the results.

## Worklog

@Clanker Add a summary here once the task has been completed.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness and model. If you have access to session info also add token count.
