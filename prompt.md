---
title: "Test project cleanup missing containers"
author: "Janik von Rotz <login@janikvonrotz.ch>"
action: implement
state: draft
date_completed: YYYY-MM-DD
harness:
provider:
model:
input_tokens:
output_tokens:
---

# Test project cleanup missing containers

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read the `AGENTS.md` and `README.md` to get an understanding of the project
- Read entire task section and prepare a list of todos
- Update the todo list while working on task

## Task

The `test-project cleanup` command is missing containers. I had to remove them manually:

```
[main][~/Odoo-Build]$ docker rm -f doc01 keycloak01 pgbouncer01 open_webui01
doc01
keycloak01
pgbouncer01
open_webui01
```

Dobule check the list.


@Clanker When task is completed set frontmatter state to review. Prompt the author to verify the results.

## Worklog

@Clanker Add a summary here once the task has been completed.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness, provider and model. If you have access to session info also add token count.
