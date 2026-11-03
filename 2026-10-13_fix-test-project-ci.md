---
commit_ref: 7e0fd22b5a3a21b46b94bd92c415fba35813604d
title: "Fix test project ci"
author: "Janik von Rotz <login@janikvonrotz.ch>"
action: implement
state: completed
date_completed: 2026-11-02
harness: pi
model: moonshotai/Kimi-K2.6
input_tokens: 60248
output_tokens: 8228
---

# Fix test project ci

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read the `AGENTS.md` and `README.md` to get an understanding of the project
- Read entire task section and prepare a list of todos
- Update the todo list while working on task

## Task

```
TEST: Test postgres scripts
Installing docker-postgres-backup ...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  1860    0  1860    0     0   3643      0 --:--:-- --:--:-- --:--:--  3647
Installing docker-postgres-create ...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  1151    0  1151    0     0   1635      0 --:--:-- --:--:-- --:--:--  1634
Installing docker-postgres-list ...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  1027    0  1027    0     0   2155      0 --:--:-- --:--:-- --:--:--  2157
Installing docker-postgres-restore ...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  1770    0  1770    0     0   2559      0 --:--:-- --:--:-- --:--:--  2557
Installing docker-postgres-drop ...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  1682    0  1682    0     0   2403      0 --:--:-- --:--:-- --:--:--  2402
Installing docker-postgres-patch ...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  1162    0  1162    0     0   1647      0 --:--:-- --:--:-- --:--:--  1645
Installing docker-postgres-duplicate ...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  2102    0  2102    0     0   2987      0 --:--:-- --:--:-- --:--:--  2990
Installing docker-postgres-size ...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  1208    0  1208    0     0   1759      0 --:--:-- --:--:-- --:--:--  1758
Installing docker-postgres-shell ...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  1450    0  1450    0     0   2895      0 --:--:-- --:--:-- --:--:--  2900
Installing docker-postgres-upgrade ...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  3313    0  3313    0     0   4763      0 --:--:-- --:--:-- --:--:--  4766
Installing docker-postgres-rename ...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  1952    0  1952    0     0   1913      0 --:--:--  0:00:01 --:--:--  1913
[WARNING]: Deprecation warnings can be disabled by setting `deprecation_warnings=False` in ansible.cfg.
[DEPRECATION WARNING]: DEFAULT_MANAGED_STR option. Reason: The `ansible_managed` variable can be set just like any other variable, or a different variable can be used.
Alternatives: Set the `ansible_managed` variable, or use any custom variable in templates. This feature will be removed from ansible-core version 2.23.

[ERROR]: The 'community.general.yaml' callback plugin has been removed. The plugin has been superseded by the option `result_format=yaml` in callback plugin ansible.builtin.default from ansible-core 2.13 onwards. This feature was removed from collection 'community.general' version 12.0.0.
Error: Process completed with exit code 1.

````

@Clanker When task is completed set frontmatter state to review. Prompt the author to verify the results.

## Worklog

1. Fixed the CI failure by updating `ansible.cfg.template` (and matching `ansible.cfg`) to use `stdout_callback = default` with `callback_result_format = yaml`. The previous setting `stdout_callback = yaml` was redirecting to the `community.general.yaml` callback plugin, which was removed in `community.general` version 12.0.0. Using the built-in `default` callback with `result_format=yaml` achieves the same YAML-formatted output without the removed plugin.

2. Fixed `Non-string value found for env option. Ambiguous env options must be wrapped in quotes` error by replacing `| int` with `| string` for `WORKERS`, `LIMIT_REQUEST`, `LIMIT_TIME_CPU`, and `LIMIT_TIME_REAL` environment variables in:
   - `roles/odoo/tasks/odoo.yml`
   - `roles/odoo/tasks/odoo_configmap.yml`

Please verify by triggering the CI run or running `./task test-scripts` locally. Update frontmatter state to completed once confirmed.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness and model. If you have access to session info also add token count.
