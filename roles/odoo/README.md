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
odoo_master_password_hash: "{{ vault_odoo_master_password_hash }}"
odoo_conf: |
  dbfilter = ^%d$
odoo_apps:
  - name: show_db_name
    url: https://github.com/Mint-System/Odoo-App-Show-DB-Name/archive/v1.0.0.zip
  - name: web_enterprise
    file: web_enterprise-13.0+e.20200414.zip
```

And include it in your playbook.

```yml
- hosts: odoo
  roles:
  - role: docker
    tags: docker
  - role: docker-network
    tags: docker-network
  - { role: postgres, tags: ["postgres"] }
  - { role: odoo, tags: ["odoo"] }
```

## Docs

Odoo container exposes port 8069 to localhost only for backup requests.

### Install apps

```bash
MODULE=show_db_name
DATABASE=odoo
CONTAINER=odoo02
docker exec -it $CONTAINER /bin/bash -c "odoo -i $MODULE -c /etc/odoo/odoo.conf -d $DATABASE --db_host \$HOST -r \$USER -w \$PASSWORD --stop-after-init" && docker restart $CONTAINER
```

## Troubleshooting

### Odoo boot fails

**Behavior**

Odoo starts, but throws internal error.

**Error**

```
2020-02-14 10:44:37,227 1 ERROR odoo odoo.modules.loading: Database odoo not initialized, you can force it with `-i base` 
```

**Reference**

https://github.com/odoo/odoo/issues/27447

*Workaround**

```
export MODULES=base
docker exec -it odoo01 /bin/bash -c "odoo -i $MODULES -d odoo --stop-after-init --db_host=\$HOST -r \$USER -w \$PASSWORD --without-demo=all"
docker restart odoo01
```