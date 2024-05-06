![logo](./logo.png)

# Ansible Build

The [Mint System](https://www.mint-system.ch/) collection of Ansible playbooks and roles.

## Requirements

* Install python 3.8+ with [pyenv](https://github.com/pyenv/pyenv-installer)
* bash/zsh alias `task='./task'` with optional [completion](https://github.com/janikvonrotz/dotfiles/blob/master/oh-my-zsh-completions/_task)

## Usage

Clone this repository.

`git clone git@github.com:Mint-System/Ansible-Build.git`

See `task help` or [task](./task.md) for details about the project commands.

### Setup

Navigate into the playbook folder.

`cd Ansible-Build`

Generate a password file for Ansible vault.

`task generate-passwordfile $PASSWORD`

Install Ansible and Python dependencies.

`task install`

Create an inventory and configure a role.

[Ansbile Documentation > Build Your Inventory](https://docs.ansible.com/ansible/latest/network/getting_started/first_inventory.html)

## Docs

### Roles

List of all available Ansible roles.

| Role                                                                   | Description                                                      |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------- |
| [acme_sh](roles/acme_sh/README.md)                                     | Issue & renew the free certificates.                             |
| [bigbluebutton_exporter](roles/bigbluebutton_exporter/README.md)       | Deploy BigBlueButton exporter container.                         |
| [bigbluebutton](roles/bigbluebutton/README.md)                         | Install BigBlueButton with https and greenlight.                 |
| [birt](roles/birt/README.md)                                           | Deploy BIRT container.                                           |
| [blackbox_exporter](roles/blackbox_exporter/README.md)                 | Deploy Blackbox exporter container.                              |
| [bookstack](roles/bookstack/README.md)                                 | Deploy BookStack container.                                      |
| [cadvisor](roles/cadvisor/README.md)                                   | Deploy cAdvisor Docker container.                                |
| [cargo](roles/cargo/README.md)                                         | Setup Rust toolchain and cargo package manager.                  |
| [certbot](roles/certbot/README.md)                                     | Deploy Let's Encrypt certificates.                               |
| [clean](roles/clean/README.md)                                         | Cleanup Ansible roles.                                           |
| [collabora_code](roles/collabora_code/README.md)                       | Deploy Collabora Code container.                                 |
| [commento](roles/commento/README.md)                                   | Deploy Commento container.                                       |
| [coturn](roles/coturn/README.md)                                       | Deploy Coturn cotainer.                                          |
| [cron](roles/cron/README.md)                                           | Setup cron jobs.                                                 |
| [debug](roles/debug/README.md)                                         | Debug Ansible variables.                                         |
| [dind](roles/dind/README.md)                                           | Deploy Docker in Docker container.                               |
| [docker_compose](roles/docker_compose/README.md)                       | Deploy Docker Compose project.                                   |
| [docker_hosts](roles/docker_hosts/README.md)                           | Docker hostname resolver.                                        |
| [docker_network](roles/docker_network/README.md)                       | Configure Docker network.                                        |
| [docker_swarm](roles/docker_swarm/README.md)                           | Configure Docker Swarm.                                          |
| [docker_volume](roles/docker_volume/README.md)                         | Configure Docker volume.                                         |
| [docker](roles/docker/README.md)                                       | Install Docker for Ubuntu and CentOS.                            |
| [dozzle](roles/dozzle/README.md)                                       | Deploy Dozzle container.                                         |
| [dribdat](roles/dribdat/README.md)                                     | Deploy dribdat container.                                        |
| [elasticsearch](roles/elasticsearch/README.md)                         | Deploy Elasticsearch Docker cluster.                             |
| [fail2ban](roles/fail2ban/README.md)                                   | Install and configure fail2ban.                                  |
| [fathom](roles/fathom/README.md)                                       | Deploy Fathom container.                                         |
| [fstab](roles/fstab/README.md)                                         | Configure the fstab file.                                        |
| [git](roles/git/README.md)                                             | Checkout Git repositories.                                       |
| [gitea](roles/gitea/README.md)                                         | Deploy Gitea container.                                          |
| [grafana](roles/grafana/README.md)                                     | Deploy Grafana Docker container.                                 |
| [htpasswd](roles/htpasswd/README.md)                                   | Configure .htpasswd basic auth file.                             |
| [iam](roles/iam/README.md)                                             | Configures users and groups.                                     |
| [innernet_client](roles/innernet_client/README.md)                     | Setup WireGuard based internal network.                          |
| [innernet_server](roles/innernet_server/README.md)                     | Setup WireGuard based internal network.                          |
| [jenkins](roles/jenkins/README.md)                                     | Deploy Jenkins container.                                        |
| [keycloak_client](roles/keycloak_client/README.md)                     | Configure Keycloak client.                                       |
| [keycloak](roles/keycloak/README.md)                                   | Deploy Keycloak Docker container.                                |
| [kibana](roles/elasticsearch/README.md)                                | Deploy Kibana Docker container.                                  |
| [locale](roles/locale/README.md)                                       | Set system locale.                                               |
| [logstash](roles/logstash/README.md)                                   | Deploy Logstash Docker container.                                |
| [loki](roles/loki/README.md)                                           | Deploy Loki container.                                           |
| [mailhog](roles/mailhog/README.md)                                     | Deploy MailHog Docker container.                                 |
| [maintenance](roles/maintenance/README.md)                             | Maintain operating system and disk space.                        |
| [mariadb](roles/mariadb/README.md)                                     | Deploy MariaDB database container.                               |
| [matomo](roles/matomo/README.md)                                       | Deploy Matomo container.                                         |
| [meilisearch](roles/meilisearch/README.md)                             | Deploy Meilisearch container.                                    |
| [metricbeat](roles/metricbeat/README.md)                               | Deploy Metricbeat Docker container.                              |
| [moodle](roles/moodle/README.md)                                       | Deploy Moodle container.                                         |
| [mysql](roles/mysql/README.md)                                         | Deploy MySQL database container.                                 |
| [nextcloud_apps](roles/nextcloud_apps/README.md)                       | Install, update and remove Nextcloud apps.                       |
| [nextcloud_exporter](roles/nextcloud_exporter/README.md)               | Deploy Nextcloud exporter container.                             |
| [nextcloud](roles/nextcloud/README.md)                                 | Deploy Nextcloud container.                                      |
| [nginx_waf](roles/nginx_waf/README.md)                                 | Deploy Nginx with ModSecurity and Core Rule Set.                 |
| [nginx](roles/nginx/README.md)                                         | Deploy Nginx proxy with Certbot.                                 |
| [node_exporter](roles/node_exporter/README.md)                         | Deploy Node exporter container and install custom metric script. |
| [odoo_apps](roles/odoo_apps/README.md)                                 | Install Odoo apps from file, url, public or private GitHub repo. |
| [odoo_data](roles/odoo_data/README.md)                                 | Generate Odoo data modules.                                      |
| [odoo_databases](roles/odoo_databases/README.md)                       | Configure Odoo databases.                                        |
| [odoo_enterprise](roles/odoo_enterprise/README.md)                     | Checkout the Odoo Enterprise git repository.                     |
| [odoo_patches](roles/odoo_patches/README.md)                           | Apply custom Odoo patches.                                       |
| [odoo_scripts](roles/odoo_scripts/README.md)                           | Install Odoo scripts.                                            |
| [odoo](roles/odoo/README.md)                                           | Deploy Odoo container.                                           |
| [onlyoffice_documentserver](roles/onlyoffice_documentserver/README.md) | Deploy OnlyOffice Document Server container.                     |
| [openldap](roles/openldap/README.md)                                   | Deploy OpenLDAP Docker container.                                |
| [package](roles/package/README.md)                                     | Set env vars and install packages.                               |
| [pgadmin](roles/pgadmin/README.md)                                     | Deploy pgAdmin container.                                        |
| [php_fpm](roles/php_fpm/README.md)                                     | Deploy PHP-FPM container.                                        |
| [postfix](roles/postfix/README.md)                                     | Deploy Postfix relay host.                                       |
| [postgres_exporter](roles/postgres_exporter/README.md)                 | Deploy PostgreSQL exporter container.                            |
| [postgres](roles/postgres/README.md)                                   | Deploy PostgreSQL database container.                            |
| [prometheus](roles/prometheus/README.md)                               | Deploy Prometheus Docker container.                              |
| [promtail](roles/promtail/README.md)                                   | Deploy Promtail container.                                       |
| [rclone](roles/rclone/README.md)                                       | Sync files with RClone.                                          |
| [rabbit](roles/rabbitmq/README.md)                                     | Deploy RabbitMQ container.                                       |
| [redis](roles/redis/README.md)                                         | Deploy Redis container.                                          |
| [remark42](roles/remark42/README.md)                                   | Deploy Remark42 container.                                       |
| [resolv](roles/resolv/README.md)                                       | Manage resolv configuration.                                     |
| [restic_client](roles/restic_client/README.md)                         | Configure Restic client backup jobs.                             |
| [restic_server](roles/restic_server/README.md)                         | Deploy Restic server container.                                  |
| [s3cmd](roles/s3cmd/README.md)                                         | Install and configure s3cmd.                                     |
| [simple_mail_forwarder](roles/simple_mail_forwarder/README.md)         | Deploy Simple Mail Forwarder container container.                |
| [superset](roles/superset/README.md)                                   | Deploy Apache Superset container.                                |
| [systemd](roles/systemd/README.md)                                     | Setup systemd service.                                           |
| [ufw](roles/ufw/README.md)                                             | Configure UFW rules.                                             |
| [update](roles/update/README.md)                                       | Install system and package updates.                              |
| [vercel](roles/vercel/README.md)                                       | Manage vercel domain and dns entries.                            |
| [wordpress](roles/wordpress/README.md)                                 | Deploy WordPress container.                                      |

### Scripts

Various roles install command line tools that can be used independent of Ansible. See [scripts](./scripts.md) for details. 

### Commands

List hosts in inventory.

```bash
task list-hosts inventories/setup
```

Load virtualenv.

```bash
source task source
```

Test connection.

```bash
ansible all -m ping -i inventories/odoo
```

Deploy multiple inventories.

```bash
ansible-playbook -i inventories/setup -i inventories/odoo play_odoo.yml
```

Deploy Odoo stack.

```bash
ansible-playbook -i inventories/odoo play_odoo.yml
```

Deploy role only.

```bash
ansible-playbook -i inventories/odoo play_odoo.yml -t postgres
```

Deploy without dependencies.

```bash
ansible-playbook -i inventories/setup play_setup.yml --skip-tags depends
```

Deploy role to specific host.

```bash
ansible-playbook -i inventories/setup play_setup.yml -t docker -l host.example.com
```

Deploy role to specific group with non-default user.

```bash
ansible-playbook -i inventories/setup play_setup.yml -t docker -l host.example.com -u username
```

Clean Odoo stack.

```bash
ansible-playbook -i inventories/odoo play_clean.yml -t odoo,odoo_volume,odoo_data,postgres,postgres_volume
```

Clean role only.

```bash
ansible-playbook -i inventories/setup play_clean.yml -t docker_network
```

Clean dry run.

```bash
ansible-playbook -i inventories/odoo play_odoo.yml -t odoo --check
```

Install odoo_scripts and odoo_apps locally.

```bash
ansible-playbook -i inventories/setup play_localhost.yml --skip-tags depends
```

List all Odoo databses.

```bash
ansible all -i inventories/odoo -a "docker-postgres-list -c {{ postgres_hostname }}"
```

### Quality

Lint the project using Ansible lint.

```bash
task lint
```

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
- Assign the tags `nginx` and `nginx_config`
- Create the task files `nginx.yml` and `nginx_config.yml`

In the `main.yml` you would include the tasks as followed:

```yml
- name: "Include {{ role_name }} config tasks"
  include_tasks: "{{ role_name }}-config.yml"
  when: nginx_data_dir is defined
  tags:
    - nginx
    - nginx_config

- name: "Include {{ role_name }} tasks"
  include_tasks: "{{ role_name }}.yml"
  when: nginx_image is defined
  tags:
    - nginx
```
