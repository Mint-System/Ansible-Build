# Ansible Fathom role

Deploys Fathom container.

## Usage

Configure the role.

**vars.yml**

```yml
fathom_image: usefathom/fathom:version-1.2.1
fathom_hostname: fathom01
fathom_volume_name: fathom_data01
```

And include it in your playbook.

```yml
- hosts: fathom
  roles:
  - role: fathom
    tags: fathom
```

Once deployed create a user.

```bash
EMAIL=admin@example.com
PASSWORD=password
docker exec fathom01 /bin/bash -c "./fathom user register --email=$EMAIL --password=$PASSWORD"
```
