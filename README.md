# Ansible Playbooks

Collection of ansible playbooks and roles.

## Playbooks

* odoo - Deploys Odoo instance
* wiki - Deploys Nextcloud and Bookstack instance
* proxy - Deploys Nginx proxy instance

## Roles

* [docker](./roles/docker/README.md) - Installs Docker for Ubuntu
* [docker-network](./roles/docker-network/README.md) - Defines internal Docker network
* [postgres](./roles/postgres/README.md) - Deploys PostgreSQL database container
* [openldap](./roles/openldap/README.md) - Openldap server
* [odoo](./roles/odoo/README.md) - Deploy Odoo container
* [debug](./roles/debug/README.md) - Debug Ansible variables
* [modescurity](./roles/modescurity/README.md) - Downloads and configures ModSecurity with OWASP CRS
* [nginx](./roles/nginx/README.md) - Deploys Nginx proxy with Let's Encrypt certificates and ModSecurity
* [clean](./roles/clean/README.md) - Cleanup Ansible roles
* [mysql](./roles/mysql/README.md) - Deploys MySQL database container
* [bookstack](./roles/bookstack/README.md) - Deploys BookStack Docker container
* [nextcloud](./roles/nextcloud/README.md) - Deploys Nextcloud container

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

`vim ./inventory_odoo/hosts.yml`

Install jmespath with pip.

`pip3 install jmespath`

### Deployment

List inventory

`ansible-inventory --list -y -i inventory_odoo`

Test connection

`ansible all -m ping -i inventory_odoo`

Deploy odoo stack

`ansible-playbook -i inventory_odoo odoo.yml`

Deploy role only

`ansible-playbook -i inventory_odoo odoo.yml --tags docker`

Deploy role to localhost

`ansible-playbook -i inventory_odoo odoo.yml --tags docker --extra-vars "ehosts=local"`

Deploy role to localhost with non-default user

`ansible-playbook -i inventory_odoo docker.yml --tags docker --extra-vars "ehosts=local" -u username`

Clean odoo stak

`ansible-playbook -i inventory_odoo odoo-clean.yml`

Clean role only

`ansible-playbook -i inventory_odoo odoo-clean.yml --tags docker`

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

Lint the project using Ansible lint.

`ansible-lint odoo.yml all-clean.yml`
