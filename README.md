# Ansible Playbooks

Collection of ansible playbooks and roles.

## Playbooks

* odoo - Deploys Odoo instance
* wiki - Deploys Nextcloud and Bookstack instance
* proxy - Deploys Nginx proxy instance

## Roles

* docker - Installs Docker for Ubuntu
* docker-network - Defines internal Docker network
* modescurity - Downloads and configures ModSecurity OWASP CRS
* proxy - Deploys Nginx proxy with Let's Encrypt certificates
* wiki - Wiki.js container
* postgres - Posgresql database
* openldap - Openldap server
* mysql - MySQL database
* bookstack - Bookstack Wiki
* nextcloud - Deploy Nextcloud container
* clean - Remove any role
* debug - Debug Ansible playbooks

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
