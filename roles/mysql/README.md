# Ansible MySQL role

Deploys MySQL database container.

## Requires

The Ansible MySQL role requires the following roles:

* docker
* docker-network

## Usage

Configure the role.

**vars.yml**

```yml
mysql_image: mysql:5
mysql_hostname: mysql01
mysql_data_dir: /usr/share/mysql01
mysql_volume_name: mysql_data01
mysql_root_password: "{{ vault_mysql_root_password }}"
mysql_database: example
mysql_user: example
mysql_password:  "{{ vault_mysql_password }}"
```

And include it in your playbook.

```yml
- hosts: mysql
  roles:
  - role: docker
    tags: docker
  - role: docker-network
    tags: docker-network
  - { role: mysql, tags: ["mysql"] }
```