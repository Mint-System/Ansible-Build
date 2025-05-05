<img src="/logos/infomaniak.png" alt="infomaniak logo" width="100" height="100">

# Infomaniak role

Manage Infomaniak domain and dns entries.

## Usage

Configure the role.

```yml
infomaniak_token: # default: "{{ vault_infomaniak_token }}"
infomaniak_zones:
  - zone: example.com
    records:
      - { source: '*.exo', type: A, target: 172.30.249.152, state: present }
```

And include it in your playbook.

```yml
- hosts: infomaniak
  roles:
  - role: infomaniak
```
