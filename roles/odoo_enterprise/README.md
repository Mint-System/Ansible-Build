# Odoo Enterprise role

Checkout the Odoo Enterprise git repository.

#DEPRECATED: Use the [Odoo Repos](../odoo_repos/README.md) role instead.

## Usage

Configure the role.

```yml
odoo_revision: "16.0.20240603"
odoo_enterprise_repo: git@gitlab.com:odoo/enterprise.git # default: "git@github.com:odoo/enterprise.git"
odoo_enterprise_key_file: /home/bot/.ssh/id_ed25519
odoo_data_dir: /usr/share/odoo # default: "/usr/share/{{ odoo_hostname }}"
odoo_enterprise_commit: 264e7bb9e1420fc9384352eb9c1f210c1c4ac8e7
odoo_enterprise_access_username: bot-mintsys
odoo_enterprise_access_token: # default: "{{ vault_odoo_enterprise_access_token }}"
```

Include the role in your playbook.

```yml
- hosts: odoo
  roles:
  - role: odoo_enterprise
```
