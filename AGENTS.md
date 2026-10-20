# AGENTS.md

This file has been created from `$HOME/taskfile.build/AGENTS.md.template`.

Note: @Clanker refers to the "ai agent" (you) who is working on this task.

## General agent guidance

This section outlines the universal rules and expectations for any LLM agent working within this repository.

**Safety and Quality First:** The highest priority is to produce secure, well-documented, and high-quality code. Do not introduce vulnerabilities, hardcoded secrets, or unreadable code.

**Propose a Plan:** For any new task, first provide a brief plan of action. This plan should clearly outline the intended changes and the rationale behind them.

**Maintain Context:** Before making any changes, an agent must read and understand the relevant files, including the project's main documentation and existing code structure.

**Be Sparse:** Only introduce new code if needed. Comment only what is worth commenting. When testing focus on the business use case. When writing documentations keep the explanation to a minimum.

**Never Commit:** Do not run `git commit`, `git push`, or any other version control write operation. Only the author is allowed to commit changes. You may stage files, run diffs, and prepare commit messages, but the actual commit and push must be done by the author.

## Project structure

- `README`: Checkout the section "Naming Conventions".
- `roles/`: In this folder are the Ansible roles. This is the main entry point.
- `roles/postgres/`: Use this role as template .
- `logos/`: There is a logo for each role.
- `inventories/`: Ignore this folder. It contains the ansible inventory files.
- `plays/`: The Ansible plabyook files.
- `test/`: Local inventory for the test setup.
- `roles.md`: Overview of all roles.
- `scripts.md`: Provides an overview of all roles that provide scripts.
## Environment & tooling

### Taskfile

This project uses the <https://taskfile.build/> standard.

The `./task` file is a bash script that provides all functions necessary to work with this project.

Always try to run a command with the `./task` file script.

### Session Info (pi harness)

Inside the **pi** harness, the model ID is in `$PI_MODEL` (e.g. `moonshotai/Kimi-K2.6`), and the session log is at `$PI_SESSION_FILE`. That JSONL file contains token usage in the `message.usage` fields (`input` and `output`). When completing a prompt file, extract the model and cumulative token counts from these sources.

### Prompt lifecycle

Tasks are tracked in `prompt.md` with a frontmatter state of `draft`, `wip`, `review`, `completed` or `cancelled`.

When the author tells you to stop (e.g. "stop" or "continue later"), preserve your work in progress:

- Add a `## WIP` section to `prompt.md` and capture the current progress there.
- Set the frontmatter state to `wip`.
- Store the prompt with `./task commit-prompt`.

When you resume work on a `wip` prompt, read the `## WIP` section and continue from there.

### New tools

Do not automatically install new software packages. Always ask for permission.

### Temporary files

When creating temporary fiels and scripts, use the `./tmp` directory.


### Encrypted secrets

All required env vars are stored in `secrets.env`. You can load the env vars like this:

```bash
eval "$(task show-dotenv secrets)"
```

Set `SOPS_AGE_KEY_FILE=/home/$USER/.config/sops/age/keys.txt` to decrypt.

## Common tasks

@Clanker this is specific to every project. Update according to your discoveries.
## Coding conventions

### General

**Avoid try catch:** Prefer default values or default params over try catch statements.


### Bash

The following guideline is heavily based on the [Bash Style Guide | ysap.sh](https://style.ysap.sh/), which should be considered the primary reference for style. Adhere to the following principles to ensure scripts are safe, predictable, and maintainable.

**Shebang:** Start scripts with `#!/usr/bin/env bash` for portability.

**Quoting:** This is critical.

- Use double quotes `"` for strings that require variable expansion.
- Use single quotes `'` for all other strings.

**Always quote variable expansions** `"$var"` to prevent word-splitting and globbing issues.

**Variables:** Distinct between local and environment vars.

- Use `local` for all variables inside functions.
- Use lowercase names for local variables (e.g., `buildx_output`).
- Use uppercase names for environment variables (e.g. `export BUILDX_PLATFORM`)

**Functions:**

- Do not use the `function` keyword.
- Use `my-func() { ... }` syntax.
- Function names are in kebab case.

**Conditionals:**

- Always use `[[ ... ]]` for conditional testing, not `[ ... ]` or `test`.
- Use `((...))` for arithmetic comparisons (e.g., `((a > b))`).
- When replacing `[]` with `[[]]` make sure to escape the brackets. The `[]` is a regex filter.

**Command Substitution:**

- Always use `$(...)` for command substitution, not backticks.

**Arrays:**

- Use Bash arrays to manage lists of items instead of space-separated strings.
- Iterate over arrays using `for item in "${my_array[@]}"; do ... done`.

**Avoid External Commands:**

- Use Bash's built-in parameter expansion for string manipulation (e.g., `${var/foo/bar}`).
- Use globbing (`*`) to iterate over files, not `ls`.
- Avoid `cat` when a command can read a file directly (e.g., `grep "pattern" file`).

**eval:** Never use `eval`.

**Logging:**

- Use single quotes for outputs without variables.
- Use double quotes for outputs with variables.
- Do not finish sentence with a dot if action is following (e.g. `"Backup file"`).
- Finish sentence with a dot if echo is after action (e.g. `"Backup finished."`).