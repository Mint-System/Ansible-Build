# Odoo Repos role

Setup Odoo modules from public or private GitHub repos.

## Usage

Configure the role.

```yml
odoo_data_dir: /usr/share/odoo # default: "/usr/share/{{ odoo_hostname }}"
odoo_revision: "16.0.20250207"
odoo_repo_key_file: /home/bot/.ssh/id_ed25519
github_personal_access_token: # default: "{{ vault_github_personal_access_token }}"
odoo_repos:
  - path: enterprise
    url: git@github.com:odoo/enterprise.git
    version: 937dc76d00362181fae12e623758d18321e15e5e
  - path: addons/partner-contact
    url: git@github.com:OCA/partner-contact.git
    version: 16.0
  - path: addons/web
    url: git@github.com:OCA/web.git
    version: 16.0
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

## Docs

### Clone with http url


To clone private repos with an http url set the `vault_github_personal_access_token` var and define `github_username`. Use the following format to clone repos with http:

```yml
odoo_repos:
  - path: enterprise
    url: https://{{ github_username }}:{{ github_personal_access_token }}@github.com/odoo/enterprise.git
    version: 937dc76d00362181fae12e623758d18321e15e5e
```

### Pull repo manually

Navigate into the repo directory on the server `cd /usr/share/odoo01/enterprise` and run:

```bash
sudo ssh-agent bash -c 'ssh-add /home/bot/.ssh/id_ed25519; git pull origin 16.0'
```

### Checkout commit manually

Navigate into the repo directory on the server `cd /usr/share/odoo01/enterprise` and run:

```bash
sudo ssh-agent bash -c 'ssh-add /home/bot/.ssh/id_ed25519; git checkout 937dc76d00362181fae12e623758d18321e15e5e'
```
