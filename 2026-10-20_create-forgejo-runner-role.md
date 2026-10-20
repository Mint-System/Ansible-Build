---
commit_ref:
title: "Create Forgejo Runner role"
author: "Janik von Rotz <login@janikvonrotz.ch>"
action: implemented
state: wip
date_completed: 2026-10-20
harness: pi
model: deepseek-v4-flash-0731
input_tokens: 908011
output_tokens: 26637
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

Created the new `forgejo-runner` role by copying the `coturn` role:

- `roles/forgejo-runner/`: default vars, tasks, handler, meta and README.
- Deploys `code.forgejo.org/forgejo/runner:9` container that uses the host Docker daemon (`/var/run/docker.sock` mount) to spawn jobs.
- First start registers the runner (guard on `/data/.runner`), then runs `forgejo-runner daemon`.
- Vars: `forgejo_runner_instance_token` defaults to `vault_forgejo_runner_instance_token`. All other vars have defaults (image, hostname, description, instance_url, labels, name, volume).
- Added role to `plays/all.yml` (tag `forgejo-runner`).
- Prepared dione vars (`forgejo_runner_hostname: forgejo-runner01`, description, instance url) in `inventories/mint_system/host_vars/dione/vars.yaml`. The vault secret `vault_forgejo_runner_instance_token` still has to be generated.
- Ran `update-docs` (added entry to `docs/roles.md`) and `lint` (no findings for the new role).
- Logo not added (author will add).

### Runner connection setup

The author created a runner on Codeberg and the role was updated to the new Forgejo Runner connection model (v13):

- Image changed to `code.forgejo.org/forgejo/runner:13.2.0`; replaced the deprecated `register` + registration-token flow with the modern `daemon --config` connection model.
- New `templates/config.yaml` defines `server.connections.forgejo` with `url`, `uuid`, `token` and `labels`.
- Added vars `forgejo_runner_instance_uuid`, `forgejo_runner_labels` (default `docker:docker://node:lts`), `forgejo_runner_data_dir` (default `/usr/share/{hostname}`); config is rendered mode 0600 and mounted read-only into the container.
- dione vars: `forgejo_runner_instance_uuid: 3e027763-5262-4781-8d60-def47f6a9afd`, instance url with trailing slash.
- Encrypted the Codeberg runner token into the dione vault: `vault_forgejo_runner_instance_token` (replaced the previously generated random value).

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness and model. If you have access to session info also add token count.

## WIP

Saved on author request (`save wip`). State set to `wip`. Progress:

- Role `forgejo-runner` is implemented and updated to the Forgejo Runner v13 connection model with `templates/config.yaml` (server.connections.forgejo: url/uuid/token/labels).
- Logo added by author, resized to 200x200 via `./task resize-logos` and renamed to `logos/forgejo-runner.png` (matches docs reference `/logos/forgejo-runner.png`).
- dione vars prepared (`forgejo_runner_hostname: forgejo-runner01`, description, instance url, uuid).
- Vault updated: `vault_forgejo_runner_instance_token` encrypted with the Codeberg runner token `34548c979bd024a429df2f54fb9b8eb987b20096` (replaced previously generated random value).
- `update-docs` and `lint` run, `plays/all.yml` syntax check passes.

Next steps (author):
- Deploy to dione: `task play -i inventories/mint_system plays/all.yml -t forgejo-runner -l dione`.
- Verify runner appears on Codeberg: https://codeberg.org/org/Mint-System/settings/actions/runners
- Then set state to `completed` (or `aborted`) and update token counts from `$PI_SESSION_FILE`.

Nothing committed (only author commits).
