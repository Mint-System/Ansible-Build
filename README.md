# Ansible Playbooks

Collection of ansible playbooks and roles.

## Playbooks

* odoo - Deploys Odoo instance
* wiki - Deploys Nextcloud and Bookstack instance
* proxy - Deploys Nginx proxy instance

## Roles

* [docker](roles/docker/README.md) - Installs Docker for Ubuntu
* [docker-network](roles/docker-network/README.md) - Defines internal Docker network
* [postgres](roles/postgres/README.md) - Deploys PostgreSQL database container
* [openldap](roles/openldap/README.md) - Openldap server
* [odoo](roles/odoo/README.md) - Deploy Odoo container
* [debug](roles/debug/README.md) - Debug Ansible variables
* [modescurity](roles/modescurity/README.md) - Downloads and configures ModSecurity with OWASP CRS
* [nginx](roles/nginx/README.md) - Deploys Nginx proxy with Let's Encrypt certificates and ModSecurity
* [clean](roles/clean/README.md) - Cleanup Ansible roles
* [mysql](roles/mysql/README.md) - Deploys MySQL database container
* [bookstack](roles/bookstack/README.md) - Deploys BookStack Docker container
* [nextcloud](roles/nextcloud/README.md) - Deploys Nextcloud container

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

Update inventory with hosts.

`vim odoo/hosts.yml`

Install jmespath with pip.

`pip3 install jmespath`

### Deployment

List inventory

`ansible-inventory --list -y -i odoo`

Test connection

`ansible all -m ping -i odoo`

Deploy odoo stack

`ansible-playbook -i odoo odoo.yml`

Deploy role only

`ansible-playbook -i odoo odoo.yml -t docker`

Deploy role to specific host

`ansible-playbook -i odoo odoo.yml -t docker -l host.example.com`

Deploy role to specific group with non-default user

`ansible-playbook -i odoo docker.yml -t docker -l europe -u username`

Clean odoo stak

`ansible-playbook -i odoo clean.yml`

Clean role only

`ansible-playbook -i odoo clean.yml -t docker`

### Localhost

Deploying to localhost requires local ssh access.

Install ssh server.

`sudo apt install openssh-server`

Copy the public key.

`echo $SSHKEY >> ~/.ssh/authorized_keys`

Enable passwordless sudo login.

`sudo /bin/bash -c "echo \"$USERNAME     ALL=(ALL) NOPASSWD:ALL\" >> /etc/sudoers"`

Test ssh access.

`ssh $USERNAME@localhost`

## Development

### Quality

Lint the project using Ansible lint.

`ansible-lint odoo.yml clean.yml`

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

**Volume Name**

Mount the folder without subfolder.

```yml
    volumes:
      - "{{ postgres_volume_name }}:/var/lib/postgresql/data"
```

For Ansible config files uses file mounts.

**Data Dir**

```yml
    volumes:
      - "{{ nginx_data_dir }}/:/etc/nginx/conf.d/:ro"
```