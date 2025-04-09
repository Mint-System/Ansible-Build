<img src="/logos/coturn.png" alt="coturn logo" width="100" height="100">

# Coturn role

Deploy Coturn cotainer.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/instrumentisto/coturn
coturn_image: instrumentisto/coturn:4.5.2
coturn_hostname: turn01
coturn_description: Turn server for BigblueButton # default: Coturn
coturn_data_dir: /usr/share/coturn # default: "/usr/share/{{ coturn_hostname }}"
coturn_external_ip: 78.47.155.157
coturn_domain: turn.example.com
coturn_realm: example.com
```
