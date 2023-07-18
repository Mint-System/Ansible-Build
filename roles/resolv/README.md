# resolv role

Manage resolv configuration.

## Usage

Configure the role.

**vars.yml**

```yml
resolv_enabled: true # default: false
resolv_name_servers:
  - 1.1.1.1
resolv_domain_name: test.example.com
resolv_domain_search:
  - ansible.com
  - redhat.com
  - cisco.com
resolv_hosts:
  - name: server.example.com
    ip: 10.42.5.1
```

And include it in your playbook.

```yml
- hosts: system
  roles:
  - role: system
```