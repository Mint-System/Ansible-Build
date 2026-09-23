---
title: "Add postgres volume config to each host"
state: completed
date_completed: 2026-09-23
model: moonshotai/Kimi-K2.6
input_tokens: 632371
output_tokens: 8617
---

# Run 23

Note: @Clanker refers to the "ai agent" (you) who is working on this task.

@Clanker when working on this task, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on the task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

With postgres 18 the default mount path changes from `/var/lib/postgresql/data` to `/var/lib/postgresql`. I already changed the role default values `roles/postgres/defaults/main.yml`. This change is breaking for all existing postgres configs. I want you to add the `postgres_volumes` vars to all existing postgres deployments. Here is an example: `inventories/mint_system/host_vars/ares_odoo/vars.yml`

Before:

```
# https://hub.docker.com/_/postgres
postgres_image: postgres:14-alpine
postgres_hostname: postgres34
postgres_description: Database odoo01
postgres_user: odoo
```

After:

```
# https://hub.docker.com/_/postgres
postgres_image: postgres:14-alpine
postgres_hostname: postgres34
postgres_description: Database odoo01
postgres_volumes:
  - "{{ postgres_volume_name }}:/var/lib/postgresql/data"
postgres_user: odoo
```

Add this for all postgres <= 17.

## Worklog

Added `postgres_volumes` with the legacy mount path `{{ postgres_volume_name }}:/var/lib/postgresql/data` to all existing Postgres deployment configs using an image version <= 17.

- Modified **56** `vars.yml` files across `inventories/mint_system/` and `inventories/opsone/`.
- Skipped `inventories/mint_system/host_vars/themis_odoo/vars.yml` because it uses `postgres:18-alpine` (>= 18, which already uses the new default `/var/lib/postgresql`).
- Skipped `inventories/mint_system/host_vars/ares_odoo/vars.yml` because `postgres_volumes` was already present.

The change ensures existing deployments keep their data in `/var/lib/postgresql/data` even though `roles/postgres/defaults/main.yml` now defaults to `/var/lib/postgresql` for Postgres 18+.
