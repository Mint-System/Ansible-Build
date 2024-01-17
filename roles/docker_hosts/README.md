# Docker Hosts role

Configures Docker Hostname in /etc/hosts.

## Usage

Configure the role.

**vars.yml**

```yml
docker_hosts_enable: true # default: false
```

And include it in your playbook.

```yml
- hosts: docker_hosts
  roles:
  - role: docker_hosts
```
