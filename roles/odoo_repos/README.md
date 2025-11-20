<img src="/logos/odoo_repos.png" alt="odoo_repos logo" width="100" height="100">

# Odoo Repos role

Setup Odoo modules from public or private git repos.

## Usage

Configure the role.

```yml
odoo_data_dir: /usr/share/odoo # default: "/usr/share/{{ odoo_hostname }}"
odoo_revision: "18.0.20250725"
odoo_repo_key_file: /home/bot/.ssh/id_ed25519
github_pat: # default: "{{ vault_github_pat }}"
odoo_repos:
  - path: enterprise
    url: https://bot-mintsys:{{ github_pat | urlencode() }}@github.com/odoo/enterprise
    version: 9642f7d8026149a6524e036c523b65ccbdf17258
  - path: addons/oca-partner-contact
    url: git@github.com:OCA/partner-contact.git
    version: 16.0 # default: "{{ odoo_revision }}"
  - path: addons/mint-system-server-tools
    url: git@github.com:Mint-System/Odoo-Apps-Server-Tools.git
    version: 17.0-mig-session_db # default: "{{ odoo_version }}"
    single_branch: false
  - path: addons/oca-partner-contact
    url: git@github.com:OCA/partner-contact.git
  - path: addons/oca-server-backend
    url: git@github.com:OCA/Server-Backend.git
  - path: addons/mint-system-management-system
    url: git@github.com:Mint-System/Odoo-Apps-Management-System.git
  - path: addons/bemade-addons
    url: https://git.bemade.org/bemade/bemade-addons.git
    sparse_dirs:
      - caldav_sync
```

And include it in your playbook.

```yml
- hosts: odoo_repos
  roles:
  - role: odoo_repos
```

## Docs

### Clone with http url

To clone private repos with an http url set the `github_pat` var and define `github_username`. Use the following format to clone repos with http:

```yml
odoo_repos:
  - path: enterprise
    url: https://{{ github_username }}:{{ github_pat }}@github.com/odoo/enterprise.git
    version: 13db977fca67da8278fbdc5753f425583b304c67
```

### Pull repo manually

Navigate into the repo directory on the server `cd /usr/share/odoo01/enterprise` and run:

```bash
ODOO_VERSION=16.0
sudo ssh-agent /bin/bash -c "ssh-add /home/bot/.ssh/id_ed25519; git fetch origin ${ODOO_VERSION}:${ODOO_VERSION}"
sudo ssh-agent /bin/bash -c "ssh-add /home/bot/.ssh/id_ed25519; git switch ${ODOO_VERSION}"
```

### Checkout commit manually

Navigate into the repo directory on the server `cd /usr/share/odoo01/enterprise` and run:

```bash
COMMIT=13db977fca67da8278fbdc5753f425583b304c67
sudo ssh-agent /bin/bash -c "ssh-add /home/bot/.ssh/id_ed25519; git checkout $COMMIT"
```

### Checkout branch manually

Navigate into the repo directory on the server `cd /usr/share/odoo01/addons/$REPO` and run:

```bash
BRANCH=18.0-sale_triple_discount-sps
sudo ssh-agent /bin/bash -c "ssh-add /home/bot/.ssh/id_ed25519; git fetch origin $BRANCH"
sudo ssh-agent /bin/bash -c "ssh-add /home/bot/.ssh/id_ed25519; git pull origin $BRANCH"
```
