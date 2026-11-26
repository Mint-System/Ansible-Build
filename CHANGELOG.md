# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Security

- Updated the `nginx` image from `nginx:1.31.3-alpine` to `nginx:1.31.9-alpine`. Versions `1.9.5` through `1.31.8` are affected by [nginx2root](https://nginx2root.com/) (CVE-2026-123007, CVE-2026-123634, CVE-2026-123633, CVE-2026-121810, CVE-2026-113425).

### Removed

- Removed `snap_packages` from `packages` role.
- Removed `grafana-backup` script from `grafana` role.

### Added

- New `taskfile_build` role that deploys the `mintsystem/taskfile.build` container to clone, build and serve a git repo. Supports deploy keys (`taskfile_build_ssh_public_key`, `taskfile_build_ssh_private_key`), a sops age key (`taskfile_build_sops_age_key`), Taskfile commands, a container command override and cron jobs running `docker exec` in the container.
- `taskfile_build` role options `taskfile_build_etc_hosts` for extra `/etc/hosts` entries and `taskfile_build_extra_env` for additional container env vars.
- `taskfile_build_cron_jobs` supports `chdir` to set the working directory of the `docker exec` call.
- New `odoo_repos` scripts `odoo-repos-list`, `odoo-repos-clone` and `odoo-repos-pull` including an install script and role tasks.
- New "Guides" documentation section with `Guides.md` overview, "Deploy Odoo module repo" guide and relocated "Upgrade Odoo" guide.
- Do a port knocking in `certbot_check.yml` task.
- Command `run` to execute Ansible commands.
- New role "Open WebUI" created using `postgres` role as template.
- New scripts for writing Docker metrics.
- Completion section added to `scripts.md` for Docker Odoo.
- `list-hosts` command now displays hosting provider information in output table.
- New `upgrade-odoo` command for managing Odoo version upgrades between environments.
- Documentation for Odoo upgrade process in `upgrade-odoo.md`.
- Documentation link "Upgrade Odoo" added to navigation menu.
- Dotenv management commands: `copy-dotenv`, `create-dotenv`, `edit-dotenv`, `list-dotenv`, `load-dotenv`, `remove-dotenv`, `rename-dotenv`, `restore-dotenv-files`, `show-dotenv`.

### Changed

- Aligned the `nginx_image` version in `nginx` and `certbot` role documentation and in the test inventory to a single fixed tag.
- `keycloak` role uses hostname v2 options (`KC_HOSTNAME` with scheme, `KC_PROXY_HEADERS`, `KC_HTTP_ENABLED`) instead of the deprecated v1 option `KC_PROXY`, fixing `invalid_redirect_uri` on the admin console with Keycloak 26. New variable `keycloak_proxy_scheme` (default `https`).
- When the `nextcloud` container image is updated, the `occ` config tasks are skipped in that run while the entrypoint upgrade runs and applied on the next deployment; fresh deployments (no existing container) are still configured immediately.
- BREAKING!: Renamed variables with `_proxy_basic_auth_` to `_basic_auth_`.
- Renamed `clean` to `cleanup`.
- Updated bash scripts to follow coding conventions from AGENTS.md.
- Merged `odoo_scripts` into `odoo` role.
- Set Python version to `3.10`.
- Remove version check in `requirements.txt`.
- Renamed `ssl` to `tls`
- Optimized backup scripts to delete destination files before creating new dumps to save disk space.
- Fixed `test-localhost` task to correctly display logs for all containers instead of only failed ones.
- Updated `list-hosts` command to display `hosting_provider` field, increased customer column width, and fixed IFS handling for proper field separation.
- Updated Odoo scripts to use standard PostgreSQL environment variables (`PGHOST`, `PGUSER`, `PGPASSWORD`) instead of legacy variables (`HOST`, `USER`, `PASSWORD`).
- Updated `dev-vuepress` task to automatically open the browser after starting the development server.
- Updated PostgreSQL volume mount path from `/var/lib/postgresql/data` to `/var/lib/postgresql` in `README.md`, `roles/docker_compose/README.md`, `roles/postgres/README.md`, and `roles/postgres/defaults/main.yml`.
- Updated default PostgreSQL image version from `postgres:14-alpine` to `postgres:18-alpine` in `roles/postgres/README.md`.
- `odoo_repos` role creates repo directories with mode `2775` and grants the Odoo group write access, so group members can clone and pull.
- `certbot` role skips certificates that have a `dns` attribute, as those are issued by `acme_sh`, and sanitizes wildcard container names.
- Moved `docs/upgrade-odoo.md` to `docs/Guides/upgrade-odoo.md`.
- `odoo-repos-clone` only changes the repo group when it differs from the addons path group and warns instead of failing when the change is not permitted.
- `odoo_repos` role lists unmanaged repo directories instead of prompting for their removal, so deployments run unattended and never delete unmanaged repos.
- `cron` role sets script job files to `0700` and owned by the job user, since scripts may contain secrets.
- `iam` role supports `iam_ssh_configs` to manage a user's `~/.ssh/config`.
- `restic` role ensures the backup directory exists with `0750` and `restic_owner:restic_group`, so group members can read the backups.
- Fixed `cron` role failing on hosts without `/etc/rsyslog.d/50-default.conf`.
- Fixed `odoo` role backup tag not matching the docker odoo backup tasks.
- Fixed `nginx_waf` role `tasks_from` referencing a task file without the `.yml` extension.
