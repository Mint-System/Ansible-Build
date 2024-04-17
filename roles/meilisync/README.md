# Meilisync role

Deploy Meilisync container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/long2ice/meilisync
meilisyncc_image: long2ice/meilisync:main
meilisyncc_description: Sync Meilisearch with Postgresql # default: Meilisync
meilisyncc_hostname: meilisync01
``

And include it in your playbook.

```yml
- hosts: meilisync
  roles:
  - role: meilisync
```

