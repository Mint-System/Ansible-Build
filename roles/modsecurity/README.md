# Ansible ModSecurity role

Downloads and configures ModSecurity with OWASP CRS.

## Usage

Configure the role.

**vars.yml**

```yml
modsecurity_image: owasp/modsecurity:3-nginx
modsecurity_data_dir: /usr/share/modsecurity
modsecurity_crs_url: "https://github.com/SpiderLabs/owasp-modsecurity-crs/archive/v3.2.0.tar.gz"
modsecurity_engine_mode: "On"
modsecurity_default_action: "phase:1,deny,log"
modsecurity_http_allowed_methods: "GET HEAD POST OPTIONS PUT PATCH DELETE"
modsecurity_request_allowed_content_type: "application/x-www-form-urlencoded|multipart/form-data|text/xml|application/xml|application/soap+xml|application/x-amf|application/json|application/octet-stream|application/csp-report|application/xss-auditor-report|text/plain|image/png"
modsecurity_exclude_rules_before_crs:
  - |
    # ModSecurity Rule Exclusion: Disable selected XSS rules for /web/example/call request uri
    SecRule REQUEST_URI "@beginsWith /web/example/call" \
        "id:1001,\
        phase:1,\
        pass,\
        nolog,\
        ctl:ruleRemoveById=941100"
modsecurity_inbound_anomaly_score_threshold: 10
```

And include it in your playbook.

```yml
- hosts: modsecurity
  roles:
  - role: modsecurity
    tags: modsecurity
```