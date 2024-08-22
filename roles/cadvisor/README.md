# cAdvisor role

Deploy cAdvisor container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://github.com/google/cadvisor
cadvisor_image: gcr.io/google-containers/cadvisor:v0.47.2
cadvisor_hostname: cadvisor01
cadvisor_description: docker monitoring for server1 # default: "cAdvisor {{ inventory_hostname_short }}"
cadvisor_nginx_data_dir: /usr/share/nginx/proxies # default: "{{ nginx_data_dir }}/proxies"
cadvisor_requires_package: python2-passlib # default: python3-passlib
cadvisor_proxy_basic_auth_username: exporter # default: cadvisor
cadvisor_proxy_basic_auth_password: # default: "{{ vault_cadvisor_proxy_basic_auth_password }}"
```

Ensure the nginx proxy includes the cadvisor config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    ssl: true
    options: |
      include /etc/nginx/conf.d/proxies/cadvisor.nginx;
```

And include it in your playbook.

```yml
- hosts: cadvisor
  roles:
  - role: cadvisor
```

The following tags are available:

* cadvisor
* cadvisor_nginx_config