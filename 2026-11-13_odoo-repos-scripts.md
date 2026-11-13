---
commit_ref: d998d56737d99e824d71c2f0a27e126627402411
title: "Odoo Repos scripts"
author: "Janik von Rotz <login@janikvonrotz.ch>"
session_id: 01a1d423-fc38-74d5-8e30-13a9e6ccbc6c
action: execute
state: completed
date_completed: 2026-11-13
harness: pi
provider: deepseek
model: deepseek-v4-1-flash-1017
input_tokens: 4953880
output_tokens: 54683
---

# Odoo Repos scripts

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read the `AGENTS.md` to get an understanding of the project
- Read task section and prepare a list of todos
- Update the todo list while working on task

## Task

The `roles/odoo_repos` pulls Odoo modules from git repos. I want to enable users in group `{{ odoo_group }}` to manage these repos on the server.

To make this possible I wanto create multiple scripts.

### Reference

Build the commands similar to `roles/odoo/files/odoo-*`.

### List repos

The first command is: `odoo-repos-list -p /usr/share/odoo01/addons`

It simply outputs the git repos in the `-p` path:

```yaml
odoo_repos:
  - path: oca-partner-contact
    url: git@github.com:OCA/partner-contact.git
    branch: 19.0
  - path: addons/mint-system-server-tools
    url: git@github.com:Mint-System/Odoo-Apps-Server-Tools.git
    branch: 17.0-mig-session_db
```

The `path` is realtive to `-p`.

### Add repo

The next command is `odoo-repos-clone -p /usr/share/odoo01/addons -r https://github.com/OCA/partner-contact.git -b 19.0 -t oca-partner-contact`

The `-p` is path, `-r` is repo, `-b` is branch and `-t` is target path.

It simply clones the module. It applies user and group from `path`.

### Pull repo

The final command is `odoo-repos-pull -p /usr/share/odoo01/addons` / `odoo-repos-pull -p /usr/share/odoo01/addons/oca-partner-contact`.

This checks de dir and subdirs (2 levels) for `.git` folders and pulls them.

### Install

Create an `roles/odoo_repos/files/install` script similar to `roles/odoo/files/install`.

Create a role task `roles/odoo_repos/tasks/odoo_repos_scripts.yml` similar to `roles/odoo/tasks/odoo_scripts.yml`.

### Docs

Add an entry to `docs/scripts.md`.

### Testing

Extend the `task test-scripts` command with tests for these scripts. Try to follow the existing pattern.

Do not test every edge case.

### Guides

Create a new nav item "Guides" and move `docs/upgrade-odoo.md` to `docs/Guides/ugprade-odoo.md`.

Then create a new guide "Deploy Odoo module repo" `docs/Guides/deploy-odoo-module-repo.md` that wakt the user throught the process of deploying `https://github.com/OCA/partner-contact/` on the server.

### Misc

Remove the `grafana-backup` script, including the install script and `docs/scripts.md` entry.

@Clanker When task is completed set frontmatter state to review. If you have access to session info add token count and session id. Prompt the author to verify the results.

## Worklog

Created three scripts in `roles/odoo_repos/files/`, following the style of `roles/odoo/files/odoo-*`:

- `odoo-repos-list -p <path> [-d <depth>]` prints a YAML `odoo_repos` list with `path` (relative to `-p`), `url` and `branch`.
- `odoo-repos-clone -p <path> -r <repo> -b <branch> -t <target>` clones the repo, applies owner and group of the addons path and refuses to overwrite an existing target.
- `odoo-repos-pull -p <path> [-d <depth>]` pulls all repos found in the path (or the repo itself if `-p` points to a repo).

Note: the search depth default is `3` instead of `2`, because `find -maxdepth` counts the `.git` folder itself. This yields repos up to two directory levels below `-p` (e.g. `addons/oca-server-backend`).

Also added:

- `roles/odoo_repos/files/install` (supports `--user`).
- `roles/odoo_repos/tasks/odoo_repos_scripts.yml` and the include in `tasks/main.yml` (tags `odoo_repos`, `odoo_repos_scripts`).
- Default `odoo_repos_scripts_dir: /usr/local/bin`.
- Entry in `docs/scripts.md`.
- `test-scripts` block cloning `partner-contact` and `server-backend`, asserting list output and pull.
- Removed `grafana-backup`, `roles/grafana/files/install`, `roles/grafana/tasks/grafana_scripts.yml`, the include in `roles/grafana/tasks/main.yml` and the `grafana` section in `docs/scripts.md`.

Verified: `bash -n` on all scripts, `ansible-playbook --syntax-check`, `ansible-lint` on `odoo_repos` and `grafana`, and an isolated run of the new test block (all assertions passed).

### Guides

- Moved `docs/upgrade-odoo.md` to `docs/Guides/upgrade-odoo.md` and fixed its relative script links to `../../scripts/`.
- Added a `Guides` nav section in `zensical.toml` with the entries "Deploy Odoo module repo" and "Upgrade Odoo".
- Created `docs/Guides/deploy-odoo-module-repo.md` documenting the deployment of `OCA/partner-contact` with the `odoo_repos` scripts (install, addons dir ownership, add, list, pull, install modules, Ansible var).
- Added `docs/Guides.md` as an overview page listing the guides (pattern from `~/Odoo-Build/docs/Guides.md`) and kept the guide entries in the nav below it.
- Verified with `./task build-zensical-docs` (no issues) and checked the rendered links.

### Script refinements

After the initial implementation the scripts were refined during deployment testing on `hermes_odoo_20`:

- Renamed `odoo-repos-add` to `odoo-repos-clone`.
- `-b` and `-t` are now required parameters, the repo-name and `19.0` defaults were removed.
- `odoo-repos-list` and `odoo-repos-pull` register each repo in the invoking user's global git config as `safe.directory`, so repos owned by another user can be read.
- `odoo-repos-list` resolves `-p` with `realpath` and falls back to the short commit hash when the repo is in detached HEAD state.
- `odoo-repos-pull` re-fetches the commit instead of pulling a branch when in detached HEAD state.
- `odoo-repos-clone` applies the group of the addons path with `chgrp` instead of `chown`.

### Related fixes

- `odoo_repos` role creates repo directories with mode `2775` and grants the Odoo group write access, so members of `odoo_group` can clone and pull.
- `certbot` role skips certificates with a `dns` attribute, as those are issued by `acme_sh`, and sanitizes wildcard hostnames used as Docker container names.
- Added `host_iam_users` and `host_iam_groups` for `bot` on `hermes` and prepared `hermes_odoo_20` (renamed from `hermes_odoo_17`) with the `20.0.20261102` revision and the pgvector Postgres image.
- Added `20.odoo.build` nginx proxies on `hermes`.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness, provider and model. If you have access to session info update token count. Finally, update the changelog with the most important changes.
