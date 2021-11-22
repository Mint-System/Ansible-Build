# Ansible systemd role

Setup systemd service.

## Usage

Configure the role.

**vars.yml**

```yml
systemd_units:
  - name: frappebench
    description: Frappe Bench Webserver
    after: syslog.target # default: undefined
    syslog_identifier: frappebench # default: undefined
    restart: on-failure # default: "always"
    standard_output: syslog # default: undefined
    exec_start: docker exec -w /workspace/frappe-bench frappe-bench bench start
    wanted_by: multi-user.target # default: multi-user.target
```

And include it in your playbook.

```yml
- hosts: systemd
  roles:
  - role: systemd
```