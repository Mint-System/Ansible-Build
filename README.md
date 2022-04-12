![logo](./logo.png)

# Ansible Playbooks

[![Ansible Lint](https://github.com/Mint-System/Ansible-Playbooks/workflows/Ansible%20Lint/badge.svg)](https://github.com/Mint-System/Ansible-Playbooks/actions?query=workflow%3A"Ansible+Lint")

The [Mint System](https://www.mint-system.ch/) collection of Ansible playbooks and roles.

## Requirements

- Install python 3.8+ with [pyenv](https://github.com/pyenv/pyenv-installer)

## Usage

Clone this repository.

`git clone https://github.com/Mint-System/Ansible-Playbooks.git`

Set this task alias.

`alias task=./task`

### Setup

Navigate to the playbook folder.

`cd Ansible-Playbooks`

Generate a password file for Ansible vault.

`task generate-passwordfile $PASSWORD`

Install Ansible and Python dependencies.

`task install`

Create an inventory and configure a role.

[Ansbile Documentation > Build Your Inventory](https://docs.ansible.com/ansible/latest/network/getting_started/first_inventory.html)

## Docs

### Roles

List of all avaialable Ansible roles.

| Role                                                                   | Description                                                      |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------- |
| [bigbluebutton-exporter](roles/bigbluebutton-exporter/README.md)       | Deploy BigBlueButton exporter container.                         |
| [bigbluebutton](roles/bigbluebutton/README.md)                         | Install BigBlueButton with https and greenlight.                 |
| [blackbox-exporter](roles/blackbox-exporter/README.md)                 | Deploy Blackbox exporter container.                              |
| [bookstack](roles/bookstack/README.md)                                 | Deploy BookStack container.                                      |
| [cadvisor](roles/cadvisor/README.md)                                   | Deploy cAdvisor Docker container.                                |
| [cargo](roles/cargo/README.md)                                         | Setup Rust toolchain and cargo package manager.                  |
| [certbot](roles/certbot/README.md)                                     | Deploy Let's Encrypt certificates.                               |
| [clean](roles/clean/README.md)                                         | Cleanup Ansible roles.                                           |
| [commento](roles/commento/README.md)                                   | Deploy Commento container.                                       |
| [cron](roles/cron/README.md)                                           | Setup cron jobs.                                                 |
| [debug](roles/debug/README.md)                                         | Debug Ansible variables.                                         |
| [docker](roles/docker/README.md)                                       | Install Docker for Ubuntu and CentOS.                            |
| [docker-compose](roles/docker-compose/README.md)                       | Deploy Docker Compose project.                                   |
| [docker-network](roles/docker-network/README.md)                       | Configure Docker network.                                        |
| [docker-swarm](roles/docker-swarm/README.md)                           | Configure Docker Swarm.                                          |
| [docker-volume](roles/docker-volume/README.md)                         | Configure Docker volume.                                         |
| [elasticsearch](roles/elasticsearch/README.md)                         | Deploy Elasticsearch Docker cluster.                             |
| [fail2ban](roles/fail2ban/README.md)                                   | Install and configure fail2ban.                                  |
| [fathom](roles/fathom/README.md)                                       | Deploy Fathom container.                                         |
| [fstab](roles/fstab/README.md)                                         | Configure the fstab file.                                        |
| [grafana](roles/grafana/README.md)                                     | Deploy Grafana Docker container.                                 |
| [iam](roles/iam/README.md)                                             | Configures users and groups.                                     |
| [innernet-client](roles/innernet-client/README.md)                     | Setup WireGuard based internal network.                          |
| [innernet-server](roles/innernet-server/README.md)                     | Setup WireGuard based internal network.                          |
| [keycloak](roles/keycloak/README.md)                                   | Deploy Keycloak Docker container.                                |
| [keycloak-client](roles/keycloak-client/README.md)                     | Configure Keycloak client.                                       |
| [kibana](roles/elasticsearch/README.md)                                | Deploy Kibana Docker container.                                  |
| [locale](roles/locale/README.md)                                       | Set system locale.                                               |
| [loki](roles/loki/README.md)                                           | Deploy Loki container.                                           |
| [logstash](roles/logstash/README.md)                                   | Deploy Logstash Docker container.                                |
| [maintenance](roles/maintenance/README.md)                             | Maintain operating system and disk space.                        |
| [mariadb](roles/mariadb/README.md)                                     | Deploy MariaDB database container.                               |
| [metricbeat](roles/metricbeat/README.md)                               | Deploy Metricbeat Docker container.                              |
| [moodle](roles/moodle/README.md)                                       | Deploy Moodle container.                                         |
| [mysql](roles/mysql/README.md)                                         | Deploy MySQL database container.                                 |
| [nextcloud](roles/nextcloud/README.md)                                 | Deploy Nextcloud container.                                      |
| [nextcloud-apps](roles/nextcloud-apps/README.md)                       | Install, update and remove Nextcloud apps.                       |
| [nextcloud-exporter](roles/nextcloud-exporter/README.md)               | Deploy Nextcloud exporter container.                             |
| [nginx](roles/nginx/README.md)                                         | Deploy Nginx proxy with Certbot.                                 |
| [nginx-waf](roles/nginx-waf/README.md)                                 | Deploy Nginx with ModSecurity and Core Rule Set.                 |
| [node-exporter](roles/node-exporter/README.md)                         | Deploy Node exporter container and install custom metric script. |
| [odoo](roles/odoo/README.md)                                           | Deploy Odoo container.                                           |
| [odoo-apps](roles/odoo-apps/README.md)                                 | Install Odoo apps from file, url, public or private GitHub repo. |
| [odoo-data](roles/odoo-data/README.md)                                 | Generate Odoo data modules.                                      |
| [odoo-databases](roles/odoo-databases/README.md)                       | Configure Odoo databases.                                        |
| [odoo-enterprise](roles/odoo-enterprise/README.md)                     | Checkout the Odoo Enterprise git repository.                     |
| [odoo-patches](roles/odoo-patches/README.md)                           | Apply custom Odoo patches.                                       |
| [odoo-scripts](roles/odoo-scripts/README.md)                           | Install Odoo scripts.                                            |
| [onlyoffice-documentserver](roles/onlyoffice-documentserver/README.md) | Deploy OnlyOffice Document Server container.                     |
| [openldap](roles/openldap/README.md)                                   | Deploy OpenLDAP Docker container.                                |
| [package](roles/package/README.md)                                     | Set env vars and install packages.                               |
| [pgadmin](roles/pgadmin/README.md)                                     | Install pgAdmin container.                                       |
| [postfix](roles/postfix/README.md)                                     | Deploy Postfix relay host.                                       |
| [postgres](roles/postgres/README.md)                                   | Deploy PostgreSQL database container.                            |
| [postgres-exporter](roles/postgres-exporter/README.md)                 | Deploy PostgreSQL exporter container.                            |
| [prometheus](roles/prometheus/README.md)                               | Deploy Prometheus Docker container.                              |
| [promtail](roles/promtail/README.md)                                   | Deploy Promtail container.                                       |
| [redis](roles/redis/README.md)                                         | Deploy Redis container.                                          |
| [remark42](roles/remark42/README.md)                                   | Deploy Remark42 container.                                       |
| [resolv](roles/resolv/README.md)                                       | Manage resolv configuration.                                     |
| [restic-client](roles/restic-client/README.md)                         | Configure Restic client backup jobs.                             |
| [restic-server](roles/restic-server/README.md)                         | Deploy Restic server container.                                  |
| [s3cmd](roles/s3cmd/README.md)                                         | Install and configure s3cmd.                                     |
| [simple-mail-forwarder](roles/simple-mail-forwarder/README.md)         | Deploy Simple Mail Forwarder container container.                |
| [systemd](roles/systemd/README.md)                                     | Setup systemd service.                                           |
| [ufw](roles/ufw/README.md)                                             | Configure UFW rules.                                             |
| [update](roles/update/README.md)                                       | Install system and package updates.                              |
| [vercel](roles/vercel/README.md)                                       | Manage vercel domain and dns entries.                            |
| [wordpress](roles/wordpress/README.md)                                 | Deploy WordPress container.                                      |

Work in progress:

| Role                                             | Description                          |
| ------------------------------------------------ | ------------------------------------ |
| [htpasswd](roles/htpasswd/README.md)             | Configure .htpasswd basic auth file. |
| [birt](roles/birt/README.md)                     | Deploy BIRT container.               |
| [rclone](roles/rclone/README.md)                 | Sync files with RClone.              |
| [coturn](roles/coturn/README.md)                 | Deploy Coturn container.             |
| [synapse](roles/synapse/README.md)               | Deploy Matrix Synapse container.     |
| [collabora-code](roles/collabora-code/README.md) | Deploy Collabora Code container.     |

### Commands

List hosts in inventory.\
`task list-hosts inventories/setup`

Load virtualenv.\
`source task source`

Test connection.\
`ansible all -m ping -i inventories/odoo`

Deploy multiple inventories.\
`ansible-playbook -i inventories/setup -i inventories/odoo -i inventories/proxy play-odoo.yml`

Deploy Odoo stack.\
`ansible-playbook -i inventories/odoo play-odoo.yml`

Deploy role only.\
`ansible-playbook -i inventories/odoo play-odoo.yml -t postgres`

Deploy without dependencies.\
`ansible-playbook -i inventories/odoo play-odoo.yml --skip-tags depends`

Deploy role to specific host.\
`ansible-playbook -i inventories/odoo play-odoo.yml -t docker -l host.example.com`

Deploy role to specific group with non-default user.\
`ansible-playbook -i inventories/odoo play-odoo.yml -t docker -l europe -u username`

Clean Odoo stack.\
`ansible-playbook -i inventories/odoo play-clean.yml -t odoo,odoo-volume,odoo-data,postgres,postgres-volume`

Clean role only.\
`ansible-playbook -i inventories/odoo play-clean.yml -t docker-network`

Clean dry run.\
`ansible-playbook -i inventories/odoo play-odoo.yml -t odoo --check`

Install odoo-scripts and odoo-apps locally.\
`ansible-playbook -i inventories/odoo play-localhost.yml --skip-tags depends`

List all Odoo databses.\
`ansible all -i inventories/odoo -a "docker-postgres-list -c {{ postgres_hostname }}"`

### Quality

Lint the project using Ansible lint.

`task lint`

### Configuration

Whenever possible use env variables to configure the container.

**Env Config**

```yml
env:
  POSTGRES_USER: "{{ postgres_user }}"
  POSTGRES_PASSWORD: "{{ postgres_password }}"
  POSTGRES_DB: "{{ postgres_db }}"
```

### Data

To persist data use Docker volumes.

**Volume Mount**

Mount the folder without subfolder.

```yml
volumes:
  - "{{ postgres_volume_name }}:/var/lib/postgresql/data"
```

For Ansible config files use file mounts.

**Bind Mount**

```yml
volumes:
  - "{{ nginx_data_dir }}/:/etc/nginx/conf.d/:ro"
```

### Guidelines

Every role folder must contain a `README.md` file.

Mark fix-me-comments with `# FIXME: <your text>`.

### Naming

Template for role vars:

```yml
# Basics:
# Url to Docker repsitory
ROLENAME_image: URL
ROLENAME_hostname: SHORTNAME + COUNTER
ROLENAME_port:
ROLENAME_volume_name: SHORTNAME_data + COUNTER
ROLENAME_data_dir: /usr/share/SHORTNAME + COUNTER
# Database connection:
ROLENAME_db_type: mysql
ROLENAME_db_user:
ROLENAME_db_password: "{{ vault_ROLENAME_db_password }}"
ROLENAME_db_hostname:
ROLENAME_db_name:
# Credentials user:
ROLENAME_user:
ROLENAME_password: "{{ vault_ROLENAME_password }}"
# Credentials admin:
ROLENAME_admin_user:
ROLENAME_admin_password: "{{ vault_ROLENAME_admin_password }}"
# Named database connection:
ROLENAME_postgres_hostname:
ROLENAME_postgres_user:
ROLENAME_postgres_password: "{{ vault_ROLENAME_postgres_password }}"
# SMTP
ROLENAME_smtp_hostname:
ROLENAME_smtp_auth:
ROLENAME_smtp_secure:
ROLENAME_smtp_port:
ROLENAME_smtp_domain:
ROLENAME_smtp_from:
ROLENAME_smtp_username:
ROLENAME_smtp_password:
```

Role names must be lower case and may contain a `-`.

### Role and Tags

Roles can have multiple tags.

**example one tag**

To define a Postgres role, you would:

- Create role `postges`
- Assign the tag `postgres`
- Create a task file `postgres.yml`

**example multiple tags**

To define a Nginx role with a config tag, you would:

- Create role `nginx`
- Assign the tags `nginx` and `nginx-config`
- Create the task files `nginx.yml` and `nginx-config.yml`

In the `main.yml` you would include the tasks as followed:

```yml
- name: "Include {{ role_name }} config tasks"
  include_tasks: "{{ role_name }}-config.yml"
  when: nginx_data_dir is defined
  tags:
    - nginx
    - nginx-config

- name: "Include {{ role_name }} tasks"
  include_tasks: "{{ role_name }}.yml"
  when: nginx_image is defined
  tags:
    - nginx
```
