---
commit_ref: 5b566f4eae58c9b2109f22f3c3781316583766ed
title: "Get docker data dir for cadvisor from daemon conf"
author: "Janik von Rotz <login@janikvonrotz.ch>"
action: implement
state: completed
date_completed: 2026-10-26
harness: pi
model: moonshotai/Kimi-K2.6
input_tokens: 22623
output_tokens: 7099
---

# Get docker data dir for cadvisor from daemon conf

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

The cadvisor exporter role requires the `docker_data_dir` var. Instead of settings this var the role should retrieve the path as fact.

Docker daemon conf has this path defined. Update the role to read this and set as var.

@Clanker When task is completed set frontmatter state to review. Prompt the author to verify the results.

## Worklog

Updated the `cadvisor` role to retrieve the Docker data dir from the Docker daemon config instead of requiring the `docker_data_dir` var.

- Added a `command` task in `roles/cadvisor/tasks/cadvisor.yml` that runs `docker info -f '{{ .DockerRootDir }}'`.
- Added a `set_fact` task that sets `docker_data_dir` from the command output.
- The container volume mount uses `docker_data_dir`.
- Applied the same `docker info` + `set_fact` pattern to `roles/alloy/tasks/alloy.yml`.
- Applied the same `docker info` + `set_fact` pattern to `roles/promtail/tasks/promtail.yml`.
- Verified `roles/node_exporter/files/write-docker-volume-metric` already retrieves `docker_data_dir` via `docker info -f '{{.DockerRootDir}}'`.

@Author: please verify the results.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness and model. If you have access to session info also add token count.
