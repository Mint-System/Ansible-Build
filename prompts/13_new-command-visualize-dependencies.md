---
title: "New command visualize dependencies"
---

# Run 13

Note: @Agent refers to the AI agent (you) who is working on this task.

@Agent when working on this task, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on the task

## Context

Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

I have copied the `bin/visualize-dependencies` script from another project. Please adapt it to visualize the dependencies between Anbile roles. The data is stored in `roles/*/meta/main.yml`. Here is an example:

`roles/bigbluebutton/meta/main.yml`

```yml
---
dependencies:
  - role: postgres
    tags:
      - postgres
      - depends

```

Please make the following changes to the script:

- `find_manifest_files` -> `find_meta_files`
- `__manifest__.py` -> `main.yml`
- In `extract_dependencies` use python yaml
- `tmp/odoo-module-dependencies.html` -> `tmp/ansible-role-dependencies.html`
- "Odoo Module Dependencies" -> "Ansible Role Dependencies"
- "modules" -> "roles"

Add a command `visuaize-dependencies` to the `task` file that calls the script and then opens the html file.

```bash
./bin/visualize-dependencies
open-with-os tmp/ansible-role-dependencies.html
```

Run the command test if it works.

## Worklog

@Agent Task completed successfully.

### Changes made:

1. **Adapted `bin/visualize-dependencies` script:**
   - Renamed `find_manifest_files` → `find_meta_files`
   - Changed from `__manifest__.py` to `main.yml`
   - Replaced `ast.literal_eval` with `yaml.safe_load` for YAML parsing
   - Updated output files to `tmp/ansible-role-dependencies.html` and `tmp/ansible-role-dependencies.mmd`
   - Changed "Odoo Module Dependencies" → "Ansible Role Dependencies"
   - Changed "modules" → "roles"
   - Fixed role name extraction: `os.path.dirname(os.path.dirname(meta_path))` to get role from `roles/<role>/meta/main.yml`
   - Added `find_all_roles()` function to list all roles in the roles directory
   - Updated `build_graph()` to include all roles (even those without meta/main.yml)
   - Roles without dependencies are shown in gray (#9E9E9E), roles with dependencies in green (#4CAF50)

2. **Added `visualize-dependencies` command to `task` file:**
   - Created function that runs the script and opens the HTML file
   - Added help table entry

### Test results:

```
Found 70 main.yml files
Found 108 roles in total
Graph built with 108 roles and 69 dependencies
```

The visualization correctly shows all 108 roles including those without meta/main.yml files. Dependencies shown include:
- `odoo --> postgres`
- `postgres --> docker_network`
- `docker_network --> docker`
