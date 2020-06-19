# Ansible Playbooks

![Ansible Lint](https://github.com/Mint-System/Ansible-Playbooks/workflows/Ansible%20Lint/badge.svg)

Collection of Ansible playbooks and roles.

## Roles

* [docker](roles/docker/README.md) - Install Docker for Ubuntu
* [docker-network](roles/docker-network/README.md) - Define internal Docker network
* [postgres](roles/postgres/README.md) - Deploy PostgreSQL database container
* [openldap](roles/openldap/README.md) - Deploy OpenLDAP Docker container
* [odoo](roles/odoo/README.md) - Deploy Odoo container
* [odoo-scripts](roles/odoo-scripts/README.md) - Install Odoo scripts
* [debug](roles/debug/README.md) - Debug Ansible variables
* [modsecurity](roles/modsecurity/README.md) - Download and configure ModSecurity with OWASP CRS
* [nginx](roles/nginx/README.md) - Deploy Nginx proxy with Let's Encrypt certificates and ModSecurity
* [clean](roles/clean/README.md) - Cleanup Ansible roles
* [mysql](roles/mysql/README.md) - Deploy MySQL database container
* [bookstack](roles/bookstack/README.md) - Deploy BookStack Docker container
* [nextcloud](roles/nextcloud/README.md) - Deploy Nextcloud container
* [colabora-code](roles/colabora-code/README.md) - Deploy Nextcloud container
* [moodle](roles/moodle/README.md) - Deploy Moodle container
* [iam](roles/iam/README.md) - Configures users and groups
* [restic-client](roles/restic-client/README.md) - Configure Restic client backup jobs
* [restic-server](roles/restic-server/README.md) - Deploy Restic server container
* [elasticsearch](roles/elasticsearch/README.md) - Deploy ElasticSearch Docker cluster
* [kibana](roles/elasticsearch/README.md) - Deploy Kibana Docker container
* [logstash](roles/logstash/README.md) - Deploy Logstash Docker container
* [metricbeat](roles/metricbeat/README.md) - Deploy Metricbeat Docker container
* [cadvisor](roles/cadvisor/README.md) - Deploy cAdvisor Docker container
* [node-exporter](roles/node-exporter/README.md) - Deploy node-exporter Docker container
* [prometheus](roles/prometheus/README.md) - Deploy Prometheus Docker container
* [grafana](roles/grafana/README.md) - Deploy Grafana Docker container
* [keycloak](roles/keycloak/README.md) - Deploy Keycloak Docker container
* [update](roles/update/README.md) - Install system and package updates
* [bigbluebutton](roles/bigbluebutton/README.md) - Install BigBlueButton with https and greenlight.
* [package](roles/package/README.md) - Install and pin packages.
* [odoo-apps](roles/odoo-apps/README.md) - Install Odoo apps.

## Usage

Clone this repository.

`git clone https://github.com/Mint-System/Ansible-Playbooks.git && cd Ansible-Playbooks`

### Setup

Set a password to encry the Ansible vault.

`export VAULTPASSWORD=PASSWORD`

Create a password file.

`echo "$VAULTPASSWORD" > .vault_pass`

Make it executable.

`chmod 600 .vault_pass`

Install jmespath with pip.

`pip3 install jmespath`

Install dnspython with pip.

`pip3 install dnspython`

Create an inventory and configure a role.

### Deployment

List inventory

`ansible-inventory --list -y -i inventories/odoo`

Test connection

`ansible all -m ping -i inventories/odoo`

Deploy multiple inventories

`ansible-playbook -i inventories/setup -i inventories/odoo -i inventories/proxy odoo.yml`

Deploy odoo stack

`ansible-playbook -i inventories/odoo odoo.yml`

Deploy role only

`ansible-playbook -i inventories/odoo odoo.yml -t postgres`

Deploy without dependencies

`ansible-playbook -i inventories/odoo odoo.yml --skip-tags depends`

Deploy role to specific host

`ansible-playbook -i inventories/odoo odoo.yml -t docker -l host.example.com`

Deploy role to specific group with non-default user

`ansible-playbook -i inventories/odoo docker.yml -t docker -l europe -u username`

Clean odoo stack

`ansible-playbook -i inventories/odoo clean.yml -t odoo,odoo-volume,odoo-data-dir,postgres,postgres-volume`

Clean role only

`ansible-playbook -i inventories/odoo clean.yml -t docker-network`

Install odoo-scripts and odoo-apps locally

`anp -i inventories/odoo localhost.yml --skip-tags depends`

## Docs

### Quality

Lint the project using Ansible lint.

`ansible-lint *.yml`

### Config

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

Mark fixme comments with `# FIXME: <your text>`.

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
