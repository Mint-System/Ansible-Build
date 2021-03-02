# Ansible Synapse role

Deploy Matrix Synapse container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://registry.hub.docker.com/r/matrixdotorg/synapse
synapse_image: matrixdotorg/synapse:v1.28.0
synapse_hostname: synapse01
synapse_description: Matrix # default: Synapse
synapse_volume_name: synapse_data01
synapse_data_dir: /usr/share/synapse # default: "/usr/share/{{ synapse_hostname }}"
synapse_db_hostname: postgres01
synapse_db_user: synapse
synapse_db_password: "{{ vault_synapse_db_password }}"
synapse_db_name: synapse
```

And include it in your playbook.

```yml
- hosts: synapse
  roles:
  - role: synapse
```
