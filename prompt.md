---
title: "Create task commands for logo scripts."
author: "Janik von Rotz <login@janikvonrotz.ch>"
state: completed
date_completed: 2026-10-12
model: moonshotai/Kimi-K2.6
input_tokens: 33379
output_tokens: 7388
---

# Create task commands for logo scripts.

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

There are two scripts to update the logos `logos/resize-logos` and `logos/convert-logos`.

I want you to create two new task commands from these scripts.

Then remove the scripts.

I will test the new commands by running `./task resize-logos` and `task convert-logos`.

## Worklog

- Read `AGENTS.md` and `README.md` to understand the project and coding conventions.
- Added `resize-logos` and `convert-logos` functions to `./task` with a new `LOGOS` help section.
- Functions `cd` into the `logos/` directory before operating, unlike the original standalone scripts.
- Added `[[ -e "$file" ]]` guard to `convert-logos` for consistency with `resize-logos` and to avoid errors when no `.jpg` files exist.
- Removed `logos/resize-logos` and `logos/convert-logos`.
- Tested both commands: `./task resize-logos` resized all PNGs successfully; `./task convert-logos` exits cleanly when no JPGs are present.
