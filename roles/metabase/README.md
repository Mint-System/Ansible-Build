# Metabase role

Deploy Metabase container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/metabase/metabase
metabase_image: metabase/metabase:v0.51.12.1
metabase_build_image: true # default: false
metabase_hostname: metabase01
metabase_description: Business Intelligence # default: Metabase
metabase_state: stopped # default: started
metabase_config_map: # default: [ name: prod ]
  - name: prod
  - name: int
metabase_timezone: Europe/Paris # default: Europe/Zurich
metabase_db_host: postgres01
metabase_db_port: 2345 # default: "5432"
metabase_db_dbname: bi # default: metabase
metabase_db_user: bi # default: metabase
metabase_db_pass: # default: "{{ vault_metabase_db_pass }}"
```

And include it in your playbook.

```yml
- hosts: metabase
  roles:
  - role: metabase
```
