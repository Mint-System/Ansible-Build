<img src="/logos/timezone.png" alt="timezone logo" width="100" height="100">

# Timezone role

Define timezone.

## Usage

Configure the role.

```yml
timezone: "Europe/Zurich"
```

And include it in your playbook.

```yml
- hosts: timezone
  roles:
  - role: timezone
```