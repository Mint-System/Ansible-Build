# Ansible IAM role

Configures users and groups.

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
```

And include it in your playbook.

```yml
- hosts: iam
  roles:
  - role: iam
    tags: iam
```
