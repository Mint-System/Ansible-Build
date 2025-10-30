<img src="/logos/odoo_scripts.png" alt="odoo_scripts logo" width="100" height="100">

# Odoo Scripts role

Install Odoo scripts.

## Usage

Configure the role.

```yml
bash_completion_dir: /home/odoo-prod/bin/.local/share/bash-completion/completions # defaults: /etc/bash_completion.d
odoo_scripts_dir: /home/odoo-prod/bin # default: /usr/local/bin
```

Include the role in your playbook.

```yml
- hosts: odoo
  roles:
  - role: odoo_scripts
```
