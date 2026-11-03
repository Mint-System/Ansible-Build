---
title: "Remove unmanaged odoo repo folders"
author: "Janik von Rotz <login@janikvonrotz.ch>"
action: implement
state: completed
date_completed: 2026-11-04
harness: pi
provider: mistral
model: deepseek-v4-1-flash-1017
input_tokens: 15530
output_tokens: 3548
---

# Remove unmanaged odoo repo folders

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read the `AGENTS.md` and `README.md` to get an understanding of the project
- Read entire task section and prepare a list of todos
- Update the todo list while working on task

## Task

Update task `roles/odoo_repos/tasks/odoo_repos.yml` to remove repo folders that are not defined in `odoo_repos`.

Similar to `roles/nginx/tasks/nginx_config.yml` create a list of unamanaged folders and delete them at the end of the task.

Do not check Ansible inventory.

@Clanker When task is completed set frontmatter state to review. Prompt the author to verify the results.

## Worklog

Added unmanaged repo folder cleanup to the end of `roles/odoo_repos/tasks/odoo_repos.yml`.

Changes:

- `Register odoo_repos repo directories`: lists all top-level directories in `odoo_data_dir` (`find -mindepth 1 -maxdepth 1 -type d`).
- `Create managed repo list from repo list`: derives the managed top-level folders from `odoo_repos[].path` (only the first path segment, e.g. `addons` for `addons/oca-partner-contact`).
- `Remove unmanaged odoo_repos repo directories`: deletes every top-level folder that is not in the managed list and notifies `Restart odoo container`.

Verification:

- `ansible-lint --offline roles/odoo_repos`: 0 failures, 0 warnings.
- Checked the managed-list expression with a throwaway playbook (`enterprise`, `addons/...` paths) which resolved to `[enterprise, addons]`.
- Not executed against a real host.

@Clanker Add a summary here once the task has been completed.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness, provider and model. If you have access to session info also add token count.
