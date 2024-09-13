# Timezone role

Define timezone.

## Usage

Configure the role.

**vars.yml**

```yml
timezone: "Europe/Zurich"
```

And include it in your playbook.

```yml
- hosts: timezone
  roles:
  - role: timezone
```