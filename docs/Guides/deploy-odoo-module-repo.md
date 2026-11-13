# Deploy Odoo module repo

This guide walks you through deploying the [OCA partner-contact](https://github.com/OCA/partner-contact/) modules on an Odoo server. The modules are pulled from a git repo into the addons directory of the Odoo deployment.

The example assumes an Odoo 19.0 deployment with the hostname `odoo01`, which results in the addons path `/usr/share/odoo01/addons`.

## Requirements

The [odoo_repos](../../scripts/#odoo_repos) scripts must be installed on the server. They allow users in the `odoo_group` to manage the module repos.

```bash
curl -L https://ansible.build/odoo_repos/install | sudo bash
```

Check that the scripts are available.

```bash
odoo-repos-list help
```

## Prepare the addons directory

Ensure the addons directory exists and is owned by the Odoo owner and group. The user running the scripts must be a member of the Odoo group.

```bash
sudo mkdir -p /usr/share/odoo01/addons
sudo chown root:odoo /usr/share/odoo01/addons
sudo usermod -aG odoo "$USER"
```

!!! note
    The `odoo-repos-clone` script applies the group of the addons path to the cloned repo. Set the group before cloning.

## Add the repo

Clone the `partner-contact` repo on branch `19.0` into the addons directory.

```bash
odoo-repos-clone \
    -p /usr/share/odoo01/addons \
    -r https://github.com/OCA/partner-contact.git \
    -b 19.0 \
    -t oca-partner-contact
```

The parameters are:

- `-p` the addons path.
- `-r` the git repo url.
- `-b` the git branch, use the branch matching the Odoo version.
- `-t` the target path relative to the addons path.

The repo is cloned to `/usr/share/odoo01/addons/oca-partner-contact`.

## Verify the repo

List the repos in the addons directory.

```bash
odoo-repos-list -p /usr/share/odoo01/addons
```

The output is a YAML list that can be copied into the `odoo_repos` var of the role.

```yaml
odoo_repos:
  - path: oca-partner-contact
    url: https://github.com/OCA/partner-contact.git
    branch: 19.0
```

## Update the repo

Pull the latest changes of all repos in the addons directory.

```bash
odoo-repos-pull -p /usr/share/odoo01/addons
```

Or pull a single repo.

```bash
odoo-repos-pull -p /usr/share/odoo01/addons/oca-partner-contact
```

## Install the modules

Restart the Odoo container to load the new addons path.

```bash
docker restart odoo01
```

Then install a module from the repo, for example `partner_firstname`.

```bash
docker-odoo-init -c odoo01 -d odoo -i partner_firstname
```

## Manage the repo with Ansible

To keep the repo in sync with the deployment, add it to the `odoo_repos` var of the [odoo_repos](../../roles/odoo_repos/) role.

```yml
odoo_repos:
  - path: oca-partner-contact
    url: https://github.com/OCA/partner-contact.git
    branch: 19.0
```

!!! warning
    The role removes directories in the addons path that are not listed in `odoo_repos`. Add all manually cloned repos to the var before running the role.
