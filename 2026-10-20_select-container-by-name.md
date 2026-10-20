---
commit_ref: 65fdf65fa42a4b704a20322fe13521680fe409da
title: "Select container by name"
author: "Janik von Rotz <login@janikvonrotz.ch>"
action: implement
state: completed
date_completed: 2026-10-20
harness: pi
model: moonshotai/Kimi-K2.6
input_tokens: 71414
output_tokens: 11856
---

# Select container by name

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

There are scripts like `docker-odoo-backup` that get the container_id by name:

```bash
container_id=$(docker ps -f "name=${container}" -q | head -n1)
[[ -z "$container_id" ]] && { echo >&2 "Container id for $container not found"; exit 1; }
```

This often ends up as an issue when having a `odooXX` and a `odooXX-staging` container:

```bash
root@themis:/home/janikvonrotz# cron-job-run -i 2
Running command: docker-odoo-backup -d odoo -c odoo43 -o /mnt/sdb/backup -f tar && restic-main backup /mnt/sdb/backup/odoo.tar --tag odoo --tag odoo43; write-node-exporter-metric -c 'Backup Odoo database' -v $?

Backup database odoo to /mnt/sdb/backup/odoo.tar
Copy filestore from container
Error response from daemon: Could not find the file /var/lib/odoo/filestore/odoo in container 879590ca2d91
Write metric node_cron_job_exit_code for code "Backup Odoo database" with value 1.
root@themis:/home/janikvonrotz# docker ps
CONTAINER ID   IMAGE                            COMMAND                  CREATED       STATUS                 PORTS                                      NAMES
879590ca2d91   mintsystem/odoo:20.0.20260926    "/entrypoint.sh odoo"    4 days ago    Up 4 days (healthy)    8068-8069/tcp, 8071-8072/tcp, 8080/tcp     odoo43-staging
7446004d7916   mintsystem/odoo:20.0.20260926    "/entrypoint.sh odoo"    6 days ago    Up 5 days (healthy)    8068-8069/tcp, 8071-8072/tcp, 8080/tcp     odoo43
bcb8b234f2bc   postgres:18-alpine       
```

I think it is easiest to get rid of this get container id functionality and alway run exec commands by container name.

@Clanker When task is completed set frontmatter state to review. Prompt the author to verify the results.

## Worklog

Removed the container ID lookup (`docker ps -f "name=..." -q | head -n1`) from all affected scripts and replaced every `docker exec`, `docker cp`, `docker inspect`, `docker stop`, and `docker rm` invocation to use the container name directly. This fixes the issue where a container name like `odoo43` would partially match `odoo43-staging` and operate on the wrong container.

Scripts updated (13 total):

- `roles/docker/files/docker-export`
- `roles/docker/files/docker-import`
- `roles/postgres/files/docker-postgres-upgrade`
- `roles/postgres/files/docker-postgres-rename`
- `roles/postgres/files/docker-postgres-duplicate`
- `roles/odoo/files/docker-odoo-backup`
- `roles/odoo/files/docker-odoo-drop`
- `roles/odoo/files/docker-odoo-duplicate`
- `roles/odoo/files/docker-odoo-init`
- `roles/odoo/files/docker-odoo-rename`
- `roles/odoo/files/docker-odoo-shell`
- `roles/odoo/files/docker-odoo-uninstall`
- `roles/odoo/files/docker-odoo-update`

All modified scripts passed `bash -n` syntax validation.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness and model. If you have access to session info also add token count.
