# Odoo Repos role

Setup Odoo modules from public or private GitHub repos.

## Usage

Configure the role.

```yml
odoo_data_dir: /usr/share/odoo # default: "/usr/share/{{ odoo_hostname }}"
odoo_revision: "16.0.20240603"
odoo_repo_key_file: /home/bot/.ssh/id_ed25519
odoo_repos:
  - path: enterprise
    url: git@github.com:odoo/enterprise.git
    version: 8638ccc9cc26b997caee852e266b7ecc6f7c632a
  - path: addons/partner-contact
    url: git@github.com:OCA/partner-contact.git
    version: 16.0
  - path: addons/web
    url: git@github.com:OCA/web.git
    version: d83e8543db74363b71ce71b32243766b986da335
  - path: addons/mint-system-server-tools
    url: git@github.com:Mint-System/Odoo-Apps-Server-Tools.git
    version: 16.0
```

And include it in your playbook.

```yml
- hosts: odoo_repos
  roles:
  - role: odoo_repos
```

The following tags are available:

* odoo_repos

## Docs

### Pull repo manually

Navigate into the repo directory on the server `cd /usr/share/odoo01/enterprise` and run:

```bash
sudo ssh-agent bash -c 'ssh-add /home/bot/.ssh/id_ed25519; git pull origin 16.0'
```

### Checkout commit manually

Navigate into the repo directory on the server `cd /usr/share/odoo01/enterprise` and run:

```bash
sudo ssh-agent bash -c 'ssh-add /home/bot/.ssh/id_ed25519; git checkout 8638ccc9cc26b997caee852e266b7ecc6f7c632a'
```
