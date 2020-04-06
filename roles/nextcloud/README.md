# Ansible Nextcloud role

Deploys Nextcloud Docker container.

## Requires

The Ansible Nextcloud role requires the following roles:

* docker
* docker-network
* postgres

## Usage

Configure the role.

**vars.yml**

```yml
nextcloud_image: nextcloud:18-apache
nextcloud_hostname: nextcloud01
nextcloud_volume_name: nextcloud_data01
nextcloud_admin_user: admin
nextcloud_admin_password: "{{ vault_nextcloud_admin_password }}"
nextcloud_postgres_hostname: postgres01
nextcloud_postgres_user: nextcloud
nextcloud_postgres_password: "{{ vault_postgres_password }}"
nextcloud_postgres_db: nextcloud
```

And include it in your playbook.

```yml
- hosts: nextcloud
  roles:
  - role: docker
    tags: docker
  - role: docker-network
    tags: docker-network
  - role: postgres
    tags: postgres
  - role: nextcloud
    tags: nextcloud
```
