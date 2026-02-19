---
title: Update Odoo scripts postgres env vars
---

# Run 07

Replace the `==` marked instructions in this file while you work on the task.

## Context

Read the `AGENTS.md` and `README.md` to get understanding of the project.

## Task

The new Odoo image does not longer provide the the env vars HOST, USER and PASSWORD for Postgres connection.
Instead the env vars are PGHOST, PGUSER and PGPASSWORD.

Update the env vars for scripts in the `roles/odoo/files` folder.

## Worklog

- Analyzed all Odoo scripts in the `roles/odoo/files` folder
- Identified all instances of the old PostgreSQL environment variables (HOST, USER, PASSWORD)
- Updated all scripts to use the new PostgreSQL environment variables (PGHOST, PGUSER, PGPASSWORD)
- Verified that all changes were applied correctly

## Summary

All Odoo scripts in the `roles/odoo/files` folder have been successfully updated to use the new PostgreSQL environment variables. The following changes were made:

- Updated `HOST` to `PGHOST`
- Updated `USER` to `PGUSER`
- Updated `PASSWORD` to `PGPASSWORD`

A total of 17 scripts were updated:
- docker-odoo-backup (already correct)
- docker-odoo-cloc
- docker-odoo-drop
- docker-odoo-duplicate
- docker-odoo-init
- docker-odoo-list
- docker-odoo-neutralize
- docker-odoo-patch
- docker-odoo-rename
- docker-odoo-restore
- docker-odoo-shell
- docker-odoo-update
- docker-odoo-upgrade (already uses correct variables)
- docker-odoo-user
- docker-odoo-uninstall
- docker-odoo-clear-assets
- docker-odoo-clear-views

The scripts now use the standard PostgreSQL environment variables that are provided by the new Odoo image.
