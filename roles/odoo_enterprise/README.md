# Odoo Enterprise role

Checkout the Odoo Enterprise git repository.

#DEPRECATED: Use the [Odoo Repos](../odoo_repos/README.md) role instead.

## Usage

Configure the role.

```yml
odoo_revision: "16.0.20250207"
odoo_enterprise_repo: git@gitlab.com:odoo/enterprise.git # default: "git@github.com:odoo/enterprise.git"
odoo_enterprise_key_file: /home/bot/.ssh/id_ed25519
odoo_data_dir: /usr/share/odoo # default: "/usr/share/{{ odoo_hostname }}"
odoo_enterprise_commit: 937dc76d00362181fae12e623758d18321e15e5e
odoo_enterprise_access_username: bot-mintsys
odoo_enterprise_access_token: # default: "{{ vault_odoo_enterprise_access_token }}"
```

Include the role in your playbook.

```yml
- hosts: odoo
  roles:
  - role: odoo_enterprise
```
