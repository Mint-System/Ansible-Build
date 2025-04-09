<img src="/logos/n8n.png" alt="n8n logo" width="100" height="100">

# N8N role

Deploy N8N container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/n8nio/n8n
n8n_image: n8nio/n8n:1.67.1
n8n_build_image: true # default: false
n8n_hostname: n8n01
n8n_description: Workflow Automation # default: N8N
n8n_state: stopped # default: started
n8n_data_dir: /usr/share/n8n # default: "/usr/share/{{ n8n_hostname }}"
n8n_volume_name: n8n_data01 # default: "{{ n8n_hostname }}"
n8n_config_map:
  - name: prod
    webhook_url: https://n8n.example.com/
  - name: int
    webhook_url: https://n8n-int.example.com/
n8n_timezone: Europe/Paris # default: Europe/Zurich
n8n_db_type: # default: postgresdb
n8n_postgresdb_host: postgres01
n8n_postgresdb_port: # default: "5432"
n8n_postgresdb_database: workflow # default: n8n
n8n_postgresdb_schema: n8n # default: public
n8n_postgresdb_user: workflow # default: n8n
n8n_postgresdb_password: # default: "{{ vault_n8n_postgresdb_password }}"
n8n_secure_cookie: "false" # default: "true"
```

And include it in your playbook.

```yml
- hosts: n8n
  roles:
  - role: n8n
```

## Docs

### Nginx config

Setup this Nginx configuration for the `n8n01-prod` host:

```yaml
nginx_proxies:
  - src_hostname: n8n.example.com
    dest_hostname: n8n01-prod
    dest_port: 5678
    ssl: true
    options: |
      include /etc/nginx/conf.d/proxy-params.conf;
```

### Deploy selected config map

Run `ansible-playbook` with extra variables and set the `cm_name` (config map name) with the name of the config map.

```bash
task play -i inventories/setup plays/all.yml -t n8n -e "cm_name=int"
```