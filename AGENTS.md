# AGENTS.md

## General agent guidance

This section outlines the universal rules and expectations for any LLM agent working within this repository.

**Safety and Quality First:** The highest priority is to produce secure, well-documented, and high-quality code. Do not introduce vulnerabilities, hardcoded secrets, or unreadable code.

**Propose a Plan:** For any new task, first provide a brief plan of action. This plan should clearly outline the intended changes and the rationale behind them.

**Maintain Context:** Before making any changes, an agent must read and understand the relevant files, including the project's main documentation and existing code structure.

**Clear Contributions:** All contributions must be submitted via a pull request with a clear, concise commit message and a brief description of the changes.

## Project structure

- `roles/`: In this folder are the Ansible roles. This is the main entry point.
- `inventories/`: Ignore this folder. It contains the ansible inventory files.

## Coding conventions

### Bash

The following guideline is heavily based on the [Bash Style Guide | ysap.sh](https://style.ysap.sh/), which should be considered the primary reference for style. Adhere to the following principles to ensure scripts are safe, predictable, and maintainable.

**Shebang:** Start scripts with `#!/usr/bin/env bash` for portability.

**Quoting:** This is critical.

- Use double quotes (`"`) for strings that require variable expansion.
- Use single quotes (`'`) for all other literal strings.

**Always quote variable expansions** (`"$var"`) to prevent word-splitting and globbing issues.

**Variables:** Distinct between local and environment vars.

- Use `local` for all variables inside functions.
- Use lowercase names for local variables (e.g., `buildx_output`).
- Use uppercase names for environment variables (e.g. `BUILDX_PLATFORM`)

**Functions:**

- Do not use the `function` keyword.
- Use `my-func() { ... }` syntax.
- Function names are in kebab case.

**Conditionals:**

- Always use `[[ ... ]]` for conditional testing, not `[ ... ]` or `test`.
- Use `((...))` for arithmetic comparisons (e.g., `((a > b))`).
- When you replace `[]` with `[[]]` make sure to escape the brakets. The `[]` is a regex filter.

**Command Substitution:**

- Always use `$(...)` for command substitution, not backticks.

**Arrays:**

- Use Bash arrays to manage lists of items instead of space-separated strings.
- Iterate over arrays using `for item in "${my_array[@]}"; do ... done`.

**Avoid External Commands:**

- Use Bash's built-in parameter expansion for string manipulation (e.g., `${var/foo/bar}`).
- Use globbing (`*`) to iterate over files, not `ls`.
- Avoid `cat` when a command can read a file directly (e.g., `grep "pattern" file`).

**`eval`:** Never use `eval`.
