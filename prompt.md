---
title: "multiple connections for forgejo runner"
author: "Janik von Rotz <login@janikvonrotz.ch>"
action: implement
state: completed
date_completed: 2026-11-05
harness: pi
provider: mistral
model: deepseek-v4-1-flash-1017
input_tokens: 100814
output_tokens: 21456
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

Refactored the `forgejo_runner` role to support multiple runner registrations.

- `roles/forgejo_runner/defaults/main.yml`: removed `forgejo_runner_instance_url` and `forgejo_runner_instance_token`, added `forgejo_runner_connections: "{{ vault_forgejo_runner_connections }}"`.
- `roles/forgejo_runner/templates/config.yaml`: loops over `forgejo_runner_connections` and renders one `server.connections.<name>` block per entry. Each entry needs `name`, `url`, `uuid` and `token`. `labels` is optional and falls back to `forgejo_runner_labels`.
- `roles/forgejo_runner/README.md`: documented the new var and the vault workflow.
- `inventories/mint_system/host_vars/dione/vars.yaml`: removed `forgejo_runner_instance_url` and `forgejo_runner_instance_uuid`.
- `inventories/mint_system/host_vars/dione/vault.yml`: replaced `vault_forgejo_runner_instance_token` with `vault_forgejo_runner_connections` holding two connections (codeberg.org and git.mint-system.ch).

### Vault format

The dione `vault.yml` was converted from inline `!vault` strings to a fully encrypted file (`$ANSIBLE_VAULT;1.2;AES256;mint_system`), so `./task decrypt-file` and `./task encrypt-file` work on it. The file now holds both `vault_coturn_static_auth_secret` and `vault_forgejo_runner_connections` as plain YAML.

Edit workflow:

```bash
./task decrypt-file inventories/mint_system/host_vars/dione/vault.yml
# edit YAML
./task encrypt-file mint_system inventories/mint_system/host_vars/dione/vault.yml
```

Always re-encrypt after decrypting; the decrypted file contains plaintext secrets.

### Verification

- `vault_forgejo_runner_connections` decrypts to the expected connection list.
- Template rendered against the real `dione` inventory (`--check --diff`) produces the expected `config.yaml`.
- Template rendered with two connections produces valid YAML with per-connection label override.
- Deployed to dione. Container logs show both runners declared: `Dione` (git.mint-system.ch) and `Forgejo Runner` (codeberg.org), and the first job was fetched from git.mint-system.ch.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness, provider and model. If you have access to session info also add token count.
