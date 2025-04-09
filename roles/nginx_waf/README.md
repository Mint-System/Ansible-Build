<img src="/logos/nginx_waf.png" alt="nginx_waf logo" width="100" height="100">

# Nginx WAF role

Deploy Nginx with ModSecurity and Core Rule Set.

## Requirements

This role requires the role `nginx` with tag `nginx_config`.

## Usage

Configure the role.

```yml
nginx_waf_image: owasp/modsecurity-crs:3.3-nginx
nginx_waf_descriptions: WAF for server1 # default: Nginx WAF
nginx_waf_hostname: waf01
nginx_waf_data_dir: /usr/share/waf # default: "/usr/share/{{ nginx_waf_hostname }}"
nginx_waf_anomaly_inbound: "10" # default: 5
nginx_waf_modsec_rule_engine: "DetectionOnly" # default: "On"
nginx_waf_http_port: 8080 # default: 80
nginx_waf_https_port: 8443 # default: 443
nginx_waf_allowed_methods: "GET PATCH DELETE" # default: "GET HEAD POST OPTIONS"
```

And include it in your playbook.

```yml
- hosts: nginx_waf
  roles:
  - role: nginx_waf
```
