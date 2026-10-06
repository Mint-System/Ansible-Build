---
title: "Move Vuepress pages into docs folder"
author: "Janik von Rotz <login@janikvonrotz.ch>"
state: completed
date_completed: 2026-10-06
model: moonshotai/Kimi-K2.6
input_tokens: 1235049
output_tokens: 16602
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

Yes, it is possible to symlink the root-level docs and build the VuePress site from a `docs` folder.

The following changes were made:

- Created `docs/` as the new VuePress source directory.
- Moved `roles.md`, `scripts.md`, and `upgrade-odoo.md` into `docs/`.
- Added symlinks inside `docs/` pointing to the root `README.md` and `roles/` folder.
- Added a root symlink `roles.md -> docs/roles.md` to keep the GitHub README link and the `task docs` command working.
- Updated `.vuepress/config.js` to explicitly set `dest`, `public`, `temp`, and `cache` to absolute paths under the root `.vuepress/` directory, so the build output and public assets stay where the existing `task` script expects them.
- Updated `package.json` scripts to invoke `vuepress dev docs --config ./.vuepress/config.js` and `vuepress build docs --config ./.vuepress/config.js`.

With these changes VuePress builds correctly from `docs/` while the original `README.md`, `roles/`, and `.vuepress/` configuration remain in place.
