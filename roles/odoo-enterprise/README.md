# Ansible Odoo Enterprise role

Checkout the Odoo Enterprise git repository.

## Usage

Configure the role.

**vars.yml**

```yml
odoo_revision: "14.0.2021.0817"
odoo_enterprise_repo: git@github.com:odoo/enterprise.git
odoo_enterprise_key_file: /home/bot/.ssh/id_ed25519
odoo_data_dir: /usr/share/odoo # default: "/usr/share/{{ odoo_hostname }}"
odoo_enterprise_commit: 264e7bb9e1420fc9384352eb9c1f210c1c4ac8e7
```

Include the role in your playbook.

```yml
- hosts: odoo
  roles:
  - role: odoo-enterprise
```
