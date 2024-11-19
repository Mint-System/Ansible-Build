# Cleanup role

Cleanup Ansible roles.

## Usage

Include it in your playbook.

```yml
- hosts: clean
  roles:
  - role: clean
```

Run the playbook and use the role with suffixes as tags. Here is an example for Odoo:

* `odoo`: This will remove the Odoo container.
* `odoo_data`: This will remove the Odoo data directory.
* `odoo_data`: This will remove the Odoo volume.

So to remove everything you would run `ansible-playbook -i inventories/odoo plays/clean.yml.yml -l host.example.com -t odoo,odoo_volume,odoo_data`
