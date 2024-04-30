# Caddy role

Deploy Caddy container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/_/caddy
caddy_image: caddy:2.7.5-alpine
caddy_build_image: true # default: false
caddy_hostname: caddy01
caddy_description: Reverse-Proxy # default: Caddy
caddy_data_dir: /usr/share/caddy # default: "/usr/share/{{ caddy_hostname }}"
caddy_ports:
  - 8080:80 # default: 80:80
  - 8443:443 # default: 443:443
  - 8443:443/udp # default: 443:443/udp
caddy_proxies:
  - address: 
    upstream: 
```

And include it in your playbook.

```yml
- hosts: caddy
  roles:
  - role: caddy
```
