# Apache Superset role

Deploy Apache Superset container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/apache/superset
superset_image: apache/superset:latest
superset_build_image: true # default: false
superset_hostname: superset01
superset_description: Business Intelligence # default: Apache Superset
superset_volume_name: superset_data01 # default: "{{ superset_hostname }}"
superset_secret_key: # default: "{{ vault_superset_secret_key }}"
superset_admin_username: admin
superset_admin_email: superset@example.com
superset_admin_password: "{{ vault_superset_admin_password }}"
```

And include it in your playbook.

```yml
- hosts: superset
  roles:
  - role: superset
```
