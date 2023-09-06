# OnlyOffice Document Server role

Deploy OnlyOffice Document Server container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/onlyoffice/documentserver
onlyoffice_documentserver_image: onlyoffice/documentserver:7.4
onlyoffice_documentserver_hostname: doc01
onlyoffice_documentserver_description: Nexcloud OnlyOffice # default: OnlyOffice Document Server
onlyoffice_documentserver_jwt_secret: # default: vault_onlyoffice_documentserver_jwt_secret
```

And include it in your playbook.

```yml
- hosts: nextcloud
  roles:
  - role: onlyoffice_documentserver
```
