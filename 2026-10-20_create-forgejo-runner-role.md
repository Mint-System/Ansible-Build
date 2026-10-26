---
commit_ref: 594fd321f93d0068218c26d8a110d8d9ec86ddc1
title: "Create Forgejo Runner role"
author: "Janik von Rotz <login@janikvonrotz.ch>"
action: implemented
state: completed
date_completed: 2026-10-23
harness: pi
model: deepseek-v4-flash-0731
input_tokens: 1830014
output_tokens: 55557
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

### Role implementation

Created the `forgejo_runner` role by copying the `coturn` role (commits `af49548c`, `a36729c5`, `d03c9506`):

- `roles/forgejo_runner/`: default vars, tasks, handler, meta and README.
- Deploys `code.forgejo.org/forgejo/runner:13.2.0` container that uses the host Docker daemon (`/var/run/docker.sock` mount) to spawn jobs.
- Vars: `forgejo_runner_instance_token` defaults to `vault_forgejo_runner_instance_token`; all other vars have defaults (image, hostname `runner`, description, instance_url, labels, volume, data_dir).
- Added role to `plays/all.yml` with tag `forgejo_runner` and to `docs/roles.md` via `update-docs`.
- Logo `logos/forgejo_runner.png` added by author (matches docs reference).

### Runner connection setup (Forgejo Runner v13)

- New `templates/config.yaml` uses the modern connection model: `server.connections.forgejo` with `url`, `uuid`, `token`, `labels` (default `docker:docker://node:lts`).
- Config rendered mode 0600, mounted read-only into the container; data dir default `/usr/share/{{ forgejo_runner_hostname }}`.
- Naming standardized to snake_case: role dir `forgejo_runner`, tag `forgejo_runner`, logo `forgejo_runner.png`, hostname `runner` (dione: `runner01`, dashes not allowed in hostnames).

### Deployment to dione

- Prepared dione vars (`forgejo_runner_hostname: runner01`, description, instance url `https://codeberg.org/`, uuid).
- Encrypted the Codeberg runner token into the dione vault (`vault_forgejo_runner_instance_token`).
- Runner requires the `mint-system.com` docker network (created by the `docker_network` role, tagged separately). Deployed with both tags:
  `task play -i inventories/mint_system plays/all.yml -l dione -t docker_network,forgejo_runner`
- Verified: container `runner01` (code.forgejo.org/forgejo/runner:13.2.0) is up and actively executing jobs (e.g. `Mint-System/taskfile.build`: Deploy Docs, Run Tests) reported to https://codeberg.org/org/Mint-System/settings/actions/runners.

Author verifies the results on Codeberg; if not OK, set state to `aborted` instead. Token counts are cumulative: prior sessions (input 908011 / output 26637) + finalization session (input 922003 / output 28920).
