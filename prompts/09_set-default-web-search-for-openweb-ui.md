---
title: Set default web search for openweb ui
---

# Run 09

IMPORTANT: When working on this task, make sure to:
1. Update the Worklog section as you progress through the task
2. Fill in the Summary section once the task is completed
3. Remove all `==` markers when done

## Context

Read the `AGENTS.md` and `README.md` to get understanding of the project.

## Task

Update the `roles/open_webui` role to enable web serach with DDGS provider by default. Add the option as an env var and ansible variable `open_webui_web_search_enabled`. 

## Worklog

- Added `open_webui_web_search_enabled` variable to `defaults/main.yml` (default: `false`)
- Added `ENABLE_WEB_SEARCH` and `WEB_SEARCH_PROVIDER` environment variables to `tasks/open_webui.yml`
- Updated `README.md` with documentation for the new variable

## Summary

The `roles/open_webui` role now supports enabling web search with DDGS provider via the `open_webui_web_search_enabled` variable. Set it to `true` in your inventory to enable web search functionality.
