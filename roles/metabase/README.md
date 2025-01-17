# Metabase role

Deploy Metabase container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/metabaseio/metabase
metabase_image: metabaseio/metabase:1.67.1
metabase_build_image: true # default: false
metabase_hostname: metabase01
metabase_description: Workflow Automation # default: N8N
metabase_state: stopped # default: started
metabase_volume_name: metabase_data01 # default: "{{ metabase_hostname }}"
metabase_config_map:
  - name: prod
    webhook_url: https://metabase.example.com/
  - name: int
    webhook_url: https://metabase-int.example.com/
metabase_timezone: Europe/Paris # default: Europe/Zurich
metabase_db_type: # default: postgresdb
metabase_postgresdb_host: postgres01
metabase_postgresdb_port: # default: "5432"
metabase_postgresdb_database: workflow # default: metabase
metabase_postgresdb_schema: metabase # default: public
metabase_postgresdb_user: workflow # default: metabase
metabase_postgresdb_password: # default: "{{ vault_metabase_postgresdb_password }}"
metabase_secure_cookie: "false" # default: "true"
```

And include it in your playbook.

```yml
- hosts: metabase
  roles:
  - role: metabase
```
