---
title: "Analyse PHP2Shell vulnerability for Nextcloud instances"
author: "Janik von Rotz <login@janikvonrotz.ch>"
action: implement
state: draft
date_completed: YYYY-MM-DD
harness:
model:
input_tokens:
output_tokens:
---

# Analyse PHP2Shell vulnerability for Nextcloud instances

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

A critical vulnerability for PHP has been found: https://en.wikipedia.org/wiki/PHP2Shell

Every PHP-based application is affected. I want you to give a status report for Nextcloud.

Please create the Ansible commands that retrieve the PHP version in the Nextcloud containers on selected hosts.

In the Ansible inventory the Nextcloud host vars have the alias `$ALIAS_nextcloud`. For example `inventories/mint_system/host_vars/zeus_nextcloud/vars.yml`.

The container name is `nextcloud_hostname` var.

You can run commands like this:

```
ansible nextcloud -i inventories/mint_system -a "docker exec  {{ nextcloud_hostname }} php version"
```

I am not sure if this is correct.

Create table with rows host, container, php version and affected. I want to know which instances are affected by the issue.

### Resolution

In second step I will start updating the container images. Do not take any action. 

@Clanker When task is completed set frontmatter state to review. Prompt the author to verify the results.

## Worklog

@Clanker Add a summary here once the task has been completed.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness and model. If you have access to session info also add token count.
