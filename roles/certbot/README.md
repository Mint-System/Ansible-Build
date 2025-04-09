<img src="/logos/certbot.png" alt="certbot logo" width="100" height="100">

# Certbot role

Deploy Let's Encrypt certificates.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/certbot/certbot
certbot_image: certbot/certbot
certbot_build_image: true # default: false
certbot_hostname: cert01
certbot_data_dir: /usr/share/cert # default: "/usr/share/{{ certbot_hostname }}"
certbot_email: info@example.com

# https://hub.docker.com/_/nginx/
nginx_image: nginx:1.25.2-alpine
nginx_hostname: nginx01
nginx_data_dir: /usr/share/nginx # default: "/usr/share/{{ nginx_hostname }}"
nginx_proxies: # See nginx role for reference
```

And include it in your playbook.

```yml
- hosts: certbot
  roles:
  - role: certbot
```

## Docs

### Install Certbot command line tools

The installation script requires that you have sudo access to root.

Run `curl -L https://raw.githubusercontent.com/mint-system/ansible-build/main/roles/certbot/files/install | bash` in your terminal.

### FreeDNS Authenticator

Set `certbot_build_image`, `certbot_authenticator` and `certbot_preferred_challenges` in the hosts inventory. Pass the the FreeDNS credentials using `certbot_secrets`. Here is an example:

```yml
certbot_build_image: true
certbot_preferred_challenges: dns # default: http
certbot_authenticator: dns-freedns
certbot_secrets:
  - file: credentials.ini
    content: |
      dns_freedns_username = example
      dns_freedns_password = {{ vault_dns_freedns_password }}
```

### Wildcard certificates

For wildcard certificates set `certbot_preferred_challenges: dns`. This will intentionally fail the certbot challenge and give you a manuall command, which must be executed on the server.
