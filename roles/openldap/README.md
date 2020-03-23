# Ansible OpenLDAP role

Deploys OpenLDAP Docker container.

## Requires

The Ansible OpenLDAP role requires the following roles:

* docker
* docker-network

## Usage

Configure the role.

**vars.yml**

```yml
openldap_image: osixia/openldap:1.3.0
openldap_hostname: ldap01
openldap_data_dir: /usr/share/openldap
openldap_password: "{{ vault_openldap_password }}"
openldap_domain: example.com
openldap_organisation: Example
```

And include it in your playbook.

```yml
- hosts: openldap
  roles:
  - role: docker
    tags: docker
  - role: docker-network
    tags: docker-network
  - { role: openldap, tags: ["openldap"] }
```