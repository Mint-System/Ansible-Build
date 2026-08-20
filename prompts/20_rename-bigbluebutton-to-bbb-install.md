---
title: "Rename bigbluebutton to bbb_install"
state: completed
model: Kimi-K2.6
input_tokens: ~13000
---

# Run 20

Note: @Clanker refers to the "ai agent" (you) who is working on this task.

@Clanker when working on this task, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on the task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

In want you to rename the role `roles/bigbluebutton` to `roles/bbb_install`. This includes also renaming all `bigbluebutton_` prefixed variables in `inventories`.

Ensure that you do not rename the `bigbluebutton_exporter` role variables. 

## Worklog

- Renamed `roles/bigbluebutton` to `roles/bbb_install`.
- Renamed task files inside the role (`bbb_install_ubuntu1804.yml`, `bbb_install_ubuntu2004.yml`).
- Updated all `bigbluebutton_` prefixed variables to `bbb_install_` within the role (`bbb_install_hostname`, `bbb_install_certbot_email`, `bbb_install_repo_is_present`, `bbb_install_api_status`).
- Updated tags from `bigbluebutton` to `bbb_install` in `tasks/main.yml`.
- Updated role `README.md` with new name and variable references.
- Renamed `logos/bigbluebutton.png` to `logos/bbb_install.png` and updated `roles.md`.
- Updated inventory files (`selene/vars.yml`, `themis/vars.yml`) replacing `bigbluebutton_hostname`, `bigbluebutton_certbot_email`, and `bigbluebutton_api_url` with `bbb_install_*` equivalents.
- Updated dependent roles:
  - `greenlight` (`defaults/main.yml`, `tasks/greenlight.yml`, `README.md`) to reference `bbb_install_hostname` and `bbb_install_api_url`/`bbb_install_api_secret`.
  - `cleanup` (`tasks/main.yml`, `tasks/bbb_install.yml`, `README.md`) to use `bbb_install` tag and task file.
  - `ufw` (`defaults/main.yml`, `README.md`) to use `bbb_install` rule set name.
- Left all `bigbluebutton_exporter` related variables, files, and references untouched as requested.
- Left references to the actual BigBlueButton software (package names, URLs, Docker images, system paths) unchanged.
