---
title: "Support ansible -e for connect host"
author: "Janik von Rotz <login@janikvonrotz.ch>"
action: implement
state: cancelled
date_completed: 2026-11-03
harness: pi
provider: deepseek
model: deepseek-v4-1-flash-1017
input_tokens: 35484
output_tokens: 3624
---

# Support ansible -e for connect host

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read the `AGENTS.md` and `README.md` to get an understanding of the project
- Read entire task section and prepare a list of todos
- Update the todo list while working on task

## Task

I would like to login with a different user with `connect-host` command.

```bash
task connect-host clio_odoo_staging -u odoo-development
````

Implment `-u/--user` param similar to `ansible-playbook` command. Keep the flag check to a minimum. Here is an example:

```
local global=false
if [[ "${1:-}" == "-g" || "${1:-}" == "--global" ]]; then
    global=true
fi
```

@Clanker When task is completed set frontmatter state to review. Prompt the author to verify the results.

## Worklog

Implemented `-u/--user` support for `connect-host` in `./task`, mirroring `ansible-playbook`:

- Added minimal flag parsing to the `connect-host` function. Accepted forms: `-u <user>`, `--user <user>`, `-u<user>`, `--user=<user>`. The flag may appear before or after the host.
- Removed the implicit positional user argument (`connect-host <host> <user>`); the user must now be passed with `-u/--user`.
- Falls back to the inventory `ansible_user` when no flag is given.
- Missing flag value (`connect-host <host> -u`) no longer hangs; it falls back to `ansible_user`.
- Updated the help table row to `connect-host|[host] [-u user]|Connect to host with configs.`

Verified with a stubbed `ssh` against `inventories/mint_system/hosts.yml` (host `aeolus`, which has `ansible_port` and `ansible_ssh_common_args`): all four flag forms produced `ssh -p 48022 -J jump.mint-system.com <user>@odoo.aerolite.ch`; omitting the flag fell back to the inventory user; a missing host returns `Host name cannot be empty` with exit 1.

Note: `connect-host` itself was not executed against a real host during testing (author request).

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness, provider and model. If you have access to session info also add token count.
