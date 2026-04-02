---
title: Add open webui env vars for OpenAI API url and bearer auth
---

# Run 10

IMPORTANT: When working on this task, make sure to:
1. Update the Worklog section as you progress through the task
2. Fill in the Summary section once the task is completed
3. Remove all `==` markers when done

## Context

Read the `AGENTS.md` and `README.md` to get understanding of the project.

## Task

Have a look at the `open_webui` role. I want to be able to set the openapi url and bearer auth with `open_webui_openapi_url` and `open_webui_openapi_secret`.

Update the README.md with example url `https://api.infomaniak.com/1/ai/105852/openai`.

Add example for secret: `open_webui_openapi_secret: # default: "{{ vault_open_webui_openapi_secret }}"`

Set this as default in `defaults/main.yml`.

The new vars are supposed to be passed to an env vars. Check the docs of Open WebUI for details.

## Worklog

==Fill this in as you work on the task==

## Summary

==Fill this once you completed the task==
