---
commit_ref: b1d7e0253c8d283dc6a758cd4f612b7ef4f018a0
title: "Remove docker volume role"
author: "Janik von Rotz <login@janikvonrotz.ch>"
state: completed
date_completed: 2026-11-04
harness: pi
model: deepseek-v4-1-flash-1017
input_tokens: 439628
output_tokens: 25331
---

# Remove docker volume role

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

I want to get rid of `docker_volume` replce. It is an unnecessary wrapper for the builtin role.

Replace:

```
- name: Include docker volume role
  ansible.builtin.include_role:
    name: docker_volume
  vars:
    docker_volume_name: "{{ matomo_volume_name }}"
  when: matomo_volume_name is defined
```

With this:

```
- name: Create {{ role_name }} volume
  community.docker.docker_volume:
    name: "{{ matomo_volume_name }}"
```

Check all roles / task not only `matomo`.

@Clanker When task is completed set frontmatter state to review. Prompt the author to verify the results.

## Worklog

Removed the `docker_volume` role. Volume creation is now a direct `community.docker.docker_volume` task in every role that used the wrapper (16 task blocks across 16 roles, plus `docker_compose`).

**Volume creation replaced**

- `matomo`, `nextcloud`, `moodle`, `dribdat`, `gitea`, `remark42`, `odoo`, `odoo_configmap`, `grafana`, `jenkins`, `loki`, `open_webui`, `php_fpm`, `postgres`, `wordpress`, `forgejo_runner`: `include_role: docker_volume` replaced with a `Create {{ role_name }} volume` task. The `when: <role>_volume_name is defined` guard is preserved.
- `docker_compose`: `include_role` with `docker_volumes` replaced by a loop over `docker_compose_volumes`. The `docker_volume` dependency was dropped from `roles/docker_compose/meta/main.yml`.

**Scripts kept, moved to `docker` role**

The role also deployed CLI tools (`docker-volume-backup`, `docker-volume-export`, ...) that `roles/restic/tasks/restic_docker_volume_backup.yml` requires. These moved into the `docker` role, which already ships `docker-export`/`docker-import` via `docker_scripts_dir`:

- 7 scripts moved to `roles/docker/files/` (byte-identical, executable bits kept).
- `roles/docker/tasks/docker_scripts.yml` and `roles/docker/files/install` extended with the volume scripts.
- `docker_scripts_dir` documented in `roles/docker/README.md`.

All inventory hosts set `docker_volume_scripts_dir` to the same value as `docker_scripts_dir`, so behavior is unchanged.

**Inventories**

Removed the now-dead `docker_volume_scripts_dir` var from 7 host_vars files (`barys`, `barys_odoo`, `barys_odoo_staging`, `clio`, `clio_odoo`, `clio_odoo_development`, `clio_odoo_staging`). `docker_scripts_dir` was kept — it is the var the `docker` role reads. Note `inventories/` is gitignored, so these edits are on-disk only and do not appear in the commit.

The scripts still deploy on those hosts: `plays/setup.yml` → `maintenance`/`docker_network` → `docker` role → `docker_scripts.yml`.

**Docs and assets**

- Deleted `roles/docker_volume/` and `logos/docker_volume.png`.
- `docs/roles.md` regenerated with `./task prepare-docs`.
- `docs/scripts.md` updated: `docker_volume` section removed, volume scripts listed under `docker`.

**Verification**

- `ansible-playbook --syntax-check` passes for `plays/localhost.yml` and `plays/cleanup.yml`.
- `./task lint` reports no new issues (baseline diff is line-number shifts only).
- `./task test-project` passes: `ok=180 failed=0`, all service endpoints return HTTP 200, volumes created by the new tasks.
- Volume scripts executed from their new location and validated; `docker-volume-*` files confirmed byte-identical to the originals.

**Follow-up: removed hardcoded binary paths in `restic`**

The `restic` role verified backup commands via `stat` on `/usr/local/bin/<command>`, which breaks when `docker_scripts_dir` points elsewhere (e.g. `/home/odoo/bin`). All six verification tasks now resolve the command on `PATH`:

```yml
- name: Verify docker-volume-backup command exists
  ansible.builtin.set_fact:
    backup_stat: "{{ lookup('ansible.builtin.pipe', 'command -v docker-volume-backup || true') }}"
  failed_when: backup_stat | length == 0
```

Applied to `restic_docker_volume_backup.yml`, `restic_docker_mysql_backup.yml`, `restic_docker_mariadb_backup.yml`, `restic_docker_odoo_backup.yml`, `restic_docker_postgres_backup.yml` and `restic_odoo_backup.yml`.

Note: `ansible.builtin.command: command -v ...` does **not** work, because `command -v` is a shell builtin and the module cannot exec it (fails with rc=2). The `pipe` lookup is used instead. The existing `command: which cron` in `roles/node_exporter` has the same latent problem but was left untouched.

Two pre-existing task-name/condition bugs were also corrected: `restic_docker_mysql_backup.yml` was named `Verify docker-odoo-backup`, and `restic_docker_mariadb_backup.yml` guarded its verify task on `item.type == "docker-mysql-backup"` instead of `docker-mariadb-dump` (so the check never ran for mariadb).

Verified: syntax check passes, no new lint issues, `./task test-project` passes (`ok=180 failed=0`), and the lookup resolves a present binary and fails on a missing one.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness and model. If you have access to session info also add token count.
