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
coturn_static_auth_secret: # default: "{{ vault_coturn_static_auth_secret }}"
coturn_realm: turn.example.com
```

## Docs

### Test STUN response

```bash
docker exec -it turn01 turnutils_stunclient turn.example.com
```