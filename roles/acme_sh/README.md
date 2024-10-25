# Acme.sh role

Issue & renew the free certificates.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/neilpang/acme.sh
acme_sh_image: neilpang/acme.sh
acme_sh_hostname: acme01
acme_sh_description: FreeDNS # default: Accme.sh
acme_sh_mail: info@example.com
acme_sh_data_dir: /usr/share/cert # default: "/usr/share/{{ acme_sh_hostname }}"
nginx_data_dir: /usr/share/nginx # default: "/usr/share/{{ nginx_hostname }}"
nginx_proxies: # See nginx role for reference
```

And include it in your playbook.

```yml
- hosts: acme_sh
  roles:
  - role: acme_sh
```

## Docs

### Use FreeDNS

To use the FreeDNS set `dns: dns_freedns` in the proxy config and define these vars:

* `acme_sh_freedns_user`
* `vault_acme_sh_freedns_password`

### Use Vercel API

To use the Vercel API set `dns: dns_vercel` in the proxy config and define these vars:

* `vault_acme_sh_vercel_token`