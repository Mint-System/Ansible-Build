# Ansible cAdvisor role

Deploy cAdvisor container.

## Usage

Configure the role.

**vars.yml**

```yml
cadvisor_hostname: cadvisor01
cadvisor_description: docker monitoring for server1
cadvisor_image: gcr.io/google-containers/cadvisor:v0.34.0
cadvisor_port: 8081
cadvisor_nginx_data_dir: /usr/share/nginx01/proxies
```

Ensure the nginx proxy includes the cadvisor config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    ssl: true
    options: |
      include /etc/nginx/conf.d/proxies/node-exporter.nginx;
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
* cadvisor-nginx-config