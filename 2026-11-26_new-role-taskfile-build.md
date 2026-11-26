---
commit_ref: bcd365c3014e88af4eaa838ebbc0a7ed60f3c4db
title: "New role Taskfile Build"
author: "Janik von Rotz <login@janikvonrotz.ch>"
session_id: 01a217d9-d1a1-715f-bd71-1231a95d1739
action: execute
state: completed
date_completed: 2026-11-26
harness: pi
provider: mistral
model: deepseek-v4-1-flash-1017
input_tokens: 188566
output_tokens: 39445
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

New role `roles/taskfile_build` created using `roles/postgres` as template, plus a new `add-ssh-key` command in the taskfile.build project.

### Image (`~/taskfile.build`)

- `bin/add-ssh-key`: new command that creates `~/.ssh`, writes `GIT_SSH_PUBLIC_KEY`, the base64 decoded `GIT_SSH_PRIVATE_KEY`, `GIT_SSH_CONFIG`, scans the host into `known_hosts` and starts an ssh-agent. Uses `source ~/.ssh/agent.env` instead of `eval`. Scans the `Hostname` from the ssh config so port-443 rewrites are trusted. Appends the trailing newline ssh requires.
- `image/Dockerfile`: installs `openssh-client` and adds `/root/taskfile.build/bin` to `PATH`.
- `image/entrypoint.sh`: sources `bin/add-ssh-key` and runs it before the git clone.
- `task` / `task.template` / `docs/library.md`: command registered, new "Git SSH deploy key" env var section (`GIT_SSH_PUBLIC_KEY`, `GIT_SSH_PRIVATE_KEY`, `SSH_ID_ALGORITHM`, `GIT_SSH_HOST`, `GIT_SSH_CONFIG`).
- `docs/image.md`: "SSH deploy keys" section. CHANGELOG updated.

### Role (`roles/taskfile_build`)

- `defaults/main.yml`: `taskfile_build_image`, `taskfile_build_hostname`, `taskfile_build_git_url`, `taskfile_build_task_commands` (`TASK_COMMANDS`), `taskfile_build_command`, `taskfile_build_caddy_root`, `taskfile_build_sops_age_key` (default `vault_taskfile_build_sops_age_key`), deploy key vars, volume, ports, `taskfile_build_cron_jobs`.
- Deploy keys are passed as env vars, no data dir and no `.ssh` mount. The private key is read with `lookup('file', ...)` (vault friendly) and base64 encoded into `GIT_SSH_PRIVATE_KEY`. Empty vars are dropped from the container env.
- `tasks/taskfile_build_cron.yml`: cron jobs running `docker exec <hostname> <command>`.
- `plays/all.yml` tag, `galaxy.yml` tag, `logos/taskfile_build.png`, `docs/roles.md`, CHANGELOG and README (vars, deploy key example, port-443 config).

### Testing

Local `test_inventory` against a locally built image `mintsystem/taskfile.build:test`, cleaned up afterwards: verified the container env, the absence of an `.ssh` mount, `Identity added` on start and the ssh clone attempt reaching GitHub. The throwaway key is not a deploy key on that repo, so auth was refused as expected. `shellcheck bin/add-ssh-key`, `./task lint` and `./task list-tags plays/all.yml` pass.

Not tested: the `clio` deployment and sops decryption with a real age key.
