# Ansible Odoo Data role

Generate Odoo data modules.

## Usage

Configure the role.

**vars.yml**

```yml
odoo_data_dir: /usr/share/odoo # default: "/usr/share/{{ odoo_hostname }}"
odoo_data:
  - id: ir_mail_server_1
    model_name: "Mail Server"
    model: ir.mail_server
    fields:
      name: Infomaniak Outgoing
      smtp_host: mail.infomaniak.com
      smtp_port: 587
      smtp_encryption: starttls
      smtp_user: odoo@example.com
      smtp_pass: "{{ vault_odoo_data_smtp_pass }}"
```

Include the role in your playbook.

```yml
- hosts: odoo
  roles:
  - role: odoo-data
```