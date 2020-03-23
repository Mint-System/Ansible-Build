# Ansible IAM role

Configures users and groups.

## Requires

The Ansible IAM role requires the following roles:

* docker

## Usage

Configure the role.

**vars.yml**

```yml
iam_options:
  add_wheel_to_sudoers: yes
  disallow_ssh_root_access: yes
iam_groups:
  - wheel
iam_users:
  - username: admin
    ssh_key: "ssh-rsa ANzaC1yc2EA...KHgKLVcBaeKQ== admin@example.com"
    groups: wheel,docker
    shell: /bin/bash
iam_packages:
  - vim=2:8.0.1453-1ubuntu1.1
```

And include it in your playbook.

```yml
- hosts: iam
  roles:
  - role: docker
    tags: docker
  - role: iam
    tags: iam
```
