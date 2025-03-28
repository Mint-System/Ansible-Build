# Nextcloud apps role

Install, update and remove Nextcloud apps.

## Usage

Configure the role.

```yml
nextcloud_hostname: nextcloud01 # default: "/usr/share/{{ odoo_hostname }}"
nextcloud_apps:
  - name: activity
    state: present
  - name: calendar
    state: present
  - name: files_external
    state: disabled
  - name: admin_audit
    state: absent
  - name: contacts
    state: enabled
```

And include it in your playbook.

```yml
- hosts: nextclcoud_apps
  roles:
  - role: nextcloud_apps
```
