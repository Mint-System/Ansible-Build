# Ansible Nginx WAF role

Deploys Nginx with ModSecurity and Core Rule Set.

## Requirements

This role requires the role `nginx` with tag `nginx-config`.

## Usage

Configure the role.

**vars.yml**

```yml
nginx_waf_image: owasp/modsecurity-crs:3.3-nginx
nginx_waf_descriptions: WAF for server1 # default: Nginx WAF
nginx_waf_hostname: waf01
nginx_waf_data_dir: /usr/share/waf01
nginx_waf_http_port: 8080 # default: 80
nginx_waf_https_port: 8443 # default: 443
```

And include it in your playbook.

```yml
- hosts: nginx-waf
  roles:
  - role: nginx-waf
```