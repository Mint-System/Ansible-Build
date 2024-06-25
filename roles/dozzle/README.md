# Dozzle role

Deploy Dozzle container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/amir20/dozzle
dozzle_image: amir20/dozzle:v7.0.7
dozzle_hostname: logview01
dozzle_description: Log Viewer # default: Dozzle
dozzle_data_dir: /usr/share/dozzle # default: "/usr/share/{{ dozzle_hostname }}"
dozzle_username: logs # default: dozzle
dozzle_password: # default: "{{ vault_dozzle_password }}"
dozzle_base: /logs # default: /
dozzle_filter: "name=keycloak-cd|odoo-cd" # default: ""
```

And include it in your playbook.

```yml
- hosts: dozzle
  roles:
  - role: dozzle
```
