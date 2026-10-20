---
commit_ref:
title: "Delete views from thirdparty modules in Odoo upgrade"
author: "Janik von Rotz <login@janikvonrotz.ch>"
action: implement
state: draft
date_completed: YYYY-MM-DD
harness:
model:
input_tokens:
output_tokens:
---

# Delete views from thirdparty modules in Odoo upgrade

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

### scripts

The `docker_volume` role also has scripts. Move the scripts into the `docker` role.

Update `install` scripts and `docs/scripts.md`.

### inventory

Replace `docker_volume_scripts_dir` with `docker_scripts_dir`.

```
-docker_volume_scripts_dir: /home/odoo/bin
+docker_scripts_dir: /home/odoo/bin
```

@Clanker When task is completed set frontmatter state to review. Prompt the author to verify the results.

## Worklog

@Clanker Add a summary here once the task has been completed.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness and model. If you have access to session info also add token count.
