# Ansible Nginx WAF role

Deploys Nginx with ModSecurity and Core Rule Set.

## Usage

Configure the role.

**vars.yml**

```yml
nginx_waf_image: owasp/modsecurity-crs:3.3-nginx
nginx_waf_hostname: waf01
nginx_waf_data_dir: /usr/share/waf01
```

And include it in your playbook.

```yml
- hosts: nginx-waf
  roles:
  - role: nginx-waf
    tags: nginx-waf
```
