# Ansible OnlyOffice Document Server role

Deploys OnlyOffice Document Server container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/onlyoffice/documentserver
onlyoffice_documentserver_image: onlyoffice/documentserver:5.6
onlyoffice_documentserver_hostname: doc01
onlyoffice_documentserver_description: Nexcloud OnlyOffice # default: OnlyOffice Document Server
```

And include it in your playbook.

```yml
- hosts: nextcloud
  roles:
  - role: collabora-code
```
