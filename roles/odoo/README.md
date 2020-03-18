# Ansible Odoo role

Deploys Odoo Docker container.

## Requires

The Ansible Odoo role requires the following roles:

* docker
* docker-network
* postgres

## Usage

Configure the role.

**vars.yml**

```yml
odoo_image: odoo:13
odoo_hostname: odoo01
odoo_port: 8069
odoo_data_dir: /usr/share/odoo01
odoo_volume_name: odoo_data01
odoo_postgres_hostname: postgres01
odoo_postgres_user: example
odoo_postgres_password: "{{ vault_postgres_password }}"
odoo_conf: |
  dbfilter = ^%d$
````

And include it in your playbook.

```yml
- hosts: odoo
  roles:
  - { role: docker, tags: ["docker"] }
  - { role: docker-network, tags: ["docker-network"] }
  - { role: postgres, tags: ["postgres"] }
  - { role: odoo, tags: ["odoo"] }
```