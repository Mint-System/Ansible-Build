---
kind: service
---

<img src="/logos/coturn.png" alt="coturn logo" width="100" height="100">

# Coturn role

Deploy Coturn cotainer.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/coturn/coturn/
coturn_image: coturn/coturn:4.5.2
coturn_hostname: turn01
coturn_description: Coturn TURN server for Nextcloud # default: Coturn
coturn_data_dir: /usr/share/coturn # default: "/usr/share/{{ coturn_hostname }}"
```
