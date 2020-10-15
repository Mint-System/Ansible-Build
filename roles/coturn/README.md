# Ansible Coturn role

Deploy Cotainer.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/instrumentisto/coturn
coturn_image: instrumentisto/coturn:4.5.1
coturn_hostname: turn01
coturn_description: Turn server for BigblueButton # default: Coturn
coturn_domain: turn.example.com
coturn_realm: example.com
```
