<img src="/logos/locale.png" alt="locale logo" width="100" height="100">

# locale role

Set system locale.

## Usage

Configure the role.

```yml
config_system_locale: pt_PT.UTF-8 # default: en_US.UTF-8
config_system_language: pt_PT.UTF-8 # default: en_US.UTF-8
```

Include it in your playbook.

```yml
- hosts: locale
  roles:
  - role: locale
```
