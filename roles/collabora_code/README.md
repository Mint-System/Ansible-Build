# Collabora Code role

Deploy Collabora Online Development Edition (CODE) container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/collabora/code
collabora_code_image: collabora/code:21.11.4.2.1
collabora_code_hostname: colla01
collabora_code_aliasgroup1: nextcloud\\.example\\.com
collabora_code_description: Code for Nextcloud # default: Collabora Code
collabora_code_port: 9981 # default: 9980
collabora_code_username: code # default: admin
collabora_code_password: # default: "{{ vault_collabora_code_password }}"
```

And include it in your playbook.

```yml
- hosts: nextcloud
  roles:
  - role: collabora_code
```

## Docs

Access the admin console at <https://%HOSTNAME/browser/dist/admin/admin.html>
