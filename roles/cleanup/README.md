<img src="/logos/cleanup.png" alt="clean logo" width="100" height="100">

# Cleanup role

Cleanup Ansible roles.

## Usage

Include it in your playbook.

```yml
- hosts: cleanup
  roles:
  - role: cleanup
```

Run the playbook and use the role with suffixes as tags. Here is an example for Odoo:

* `odoo`: This will remove the Odoo container.
* `odoo_data`: This will remove the Odoo data directory.
* `odoo_volume`: This will remove the Odoo volume.

So to remove everything you would run `task play -i inventories/odoo plays/cleanup .yml.yml -l host.example.com -t odoo,odoo_volume,odoo_data`

## Docs

### Available tags for cleanup

- bigbluebutton
- bookstack
- cadvisor
- certbot
- collabora_code
- commento
- crowdsec
- docker_compose
- docker_network
- docker_swarm
- fail2ban
- fathom
- grafana
- iam
- innernet
- keycloak
- loki
- mailhog
- meilisearch
- metabase
- moodle
- mysql
- n8n
- nextcloud
- nginx
- node_exporter
- odoo
- odoo_scripts
- openldap
- packages
- pgadmin
- postgres
- prometheus
- promtail
- rabbitmq
- redis
- restic
- wordpress
