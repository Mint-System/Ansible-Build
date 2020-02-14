
# Ansible Playbooks

Collection of ansible playbooks and roles.

## Playbooks

* odoo - Deploys odoo docker instance

## Roles

* docker - Install docker for Ubuntu
* clean - Remove any role

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

`vim ./inventory/hosts.yml`

### Deployment

Test connection

`ansible all -m ping -i inventory`

Deploy odoo stack

`ansible-playbook -i inventory odoo.yml`

Deploy role only

`ansible-playbook -i inventory odoo.yml --tags docker`

Deploy role to localhost

`ansible-playbook -i inventory odoo.yml --tags docker --extra-vars "ehosts=local"`

Deploy role to localhost with non-default user

`ansible-playbook -i inventory docker.yml --tags docker --extra-vars "ehosts=local" -u username`

Clean odoo stak

`ansible-playbook -i inventory odoo-clean.yml`

Clean role only

`ansible-playbook -i inventory odoo-clean.yml --tags docker`

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

`ansible-lint elk.yml elk-clean.yml`
