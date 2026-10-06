---
title: "Move Vuepress pages into docs folder"
author: "Janik von Rotz <login@janikvonrotz.ch>"
state: draft
date_completed: YYYY-MM-DD
model:
input_tokens:
output_tokens:
---

# Move Vuepress pages into docs folder

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

In `.vuepress/config.js` you find:

```
pagePatterns: [
    'roles/**/*.md',
    'README.md',
    'roles.md',
    'scripts.md',
    'upgrade-odoo.md',
],
```

I want to move all docs into a `docs` folder, but keep the `README.md` and `roles/**/*.md`. Is it possible symlink these folder and build the Vuepress site from `docs`?

Let me know if this possible and then proceed with the update.

## Worklog

@Clanker Add a summary here once the task has been completed.

@Clanker Set frontmatter state to completed and update date and model. If you have access to session info also add token count.
