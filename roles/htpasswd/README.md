# Ansible .htpasswd role

Configure .htpasswd basic auth file.

## Usage

Configure the role.

**vars.yml**

```yml
htpasswd_name: users # default: "default"
htpasswd_requires_package: python2-passlib # default: python3-passlib
htpasswd_nginx_data_dir: /usr/share/nginx/proxies # default: "{{ nginx_data_dir }}/proxies"
htpasswd_credentials:
  - username: intern
    password: "{{ vault_htpasswd_intern_password }}"
```

Ensure the nginx proxy includes the node-exporter config:

```yml
nginx_proxies:
  - src_hostname: intern.example.com
    locations:
      - path: /static
        root: intern.example.com
        options: |
          auth_basic "intern";
          auth_basic_user_file /etc/nginx/conf.d/proxies/users.htpasswd;
```

And include it in your playbook.

```yml
- hosts: htpasswd
  roles:
  - role: htpasswd
```
