# Ansible cAdvisor role

Deploys cAdvisor container.

## Usage

Configure the role.

**vars.yml**

```yml
cadvisor_hostname: cadvisor01
cadvisor_description: docker monitoring for server1
cadvisor_image: gcr.io/google-containers/cadvisor:v0.34.0
cadvisor_port: 8081
cadvisor_nginx_data_dir: /usr/share/nginx01
```

Ensure the nginx proxy includes the cadvisor config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    ssl: true
    options: |
      include /etc/nginx/conf.d/*.nginx;
```

And include it in your playbook.

```yml
- hosts: cAdvisor
  roles:
  - role: cadvisor
    tags: cadvisor
```
