<img src="/logos/resolv.png" alt="resolv logo" width="100" height="100">

# resolv role

Manage DNS configuration.

## Usage

Configure the role.

```yml
resolv_enabled: true # default: false
resolv_dns: 9.9.9.9 149.112.112.112
resolv_fallback_dns: 2620:fe::fe 2620:fe::9
resolv_nameserver: 1.1.1.1
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
- hosts: resolv
  roles:
  - role: resolv
```