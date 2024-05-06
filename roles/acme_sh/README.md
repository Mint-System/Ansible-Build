# acme.sh role

Issue & renew the free certificates.

## Usage

Configure the role.

**vars.yml**

```yml
acme_sh_image: neilpang/acme.sh
acme_sh_hostname: acme01
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
