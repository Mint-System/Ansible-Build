---
commit_ref:
title: "New role Taskfile Build"
author: "Janik von Rotz <login@janikvonrotz.ch>"
session_id:
action: execute
state: draft
date_completed: YYYY-MM-DD
harness:
provider:
model:
input_tokens:
output_tokens:
---

# New role Taskfile Build

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read the `AGENTS.md` to get an understanding of the project
- Read task section and prepare a list of todos
- Update the todo list while working on task

@Clanker When task is completed set frontmatter state to review. If you have access to session info add token count and session id. Prompt the author to verify the results.

## Task

Build a new role `roles/taskfile_build`.

It simly deploys a Docker container with image <https://hub.docker.com/r/mintsystem/taskfile.build/>.

It takes `taskfile_build_git_url` as an argument.

The source of the image is at `~/taskfile.build/image`.

The container hostname is `taskfile_build_hostname`.

For references look at `roles/postgres`.

### Support deploy keys

The `roles/ssh` role supports generating deploy keys.

Instead of setting up deploy keys for the user, I would like to setup deploy keys for the taskfile_build deployment.

Introduce new vars `taskfile_build_ssh_public_key` and `taskfile_build_ssh_private_key`.

Add example to `## Docs` in the new `README.md` shows how a deploy key can be generated and added.

### SOPS Age key secret

The project that I am going to deploy contains files encrypted with sops / age.

Add support to set a `SOPS_AGE_KEY` from `taskfile_build_sops_age_key` with default `vault_taskfile_build_sops_age_key`.

### Start command

Another var is the `taskfile_build_task_commands` / `TASK_COMMANDS`.

I also want `taskfile_build_command` that allows overwriting the caddy start command.

### Testing

I will test the deployment for the `clio` host. First I will setup the deployment keys and then run the deployment with:

```bash
task play -i inventories/mint_system plays/all.yml -l clio -t taskfile_build
```

In addition I will setup a cron job that runs the command in the container.

## Worklog

@Clanker Add a summary here once the task has been completed.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness, provider and model. If you have access to session info update token count. Finally, update the changelog with the most important changes.
