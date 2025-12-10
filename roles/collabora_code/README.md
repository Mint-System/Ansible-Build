<img src="/logos/collabora_code.png" alt="collabora_code logo" width="100" height="100">

# Collabora Code role

Deploy Collabora Online Development Edition (CODE) container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/collabora/code
collabora_code_image: collabora/code:24.04.8.2.1
collabora_code_hostname: doc01
collabora_code_data_dir: /usr/share/doc # default: /usr/share/{{ collabora_code_hostname }}
collabora_code_server_name: doc.example.com
collabora_code_host: https://next.example.com:443 # default: ""
collabora_code_alias1: https://cloud.example.com:443 # default: ""
collabora_code_description: Collabora for Nextcloud # default: Collabora Code
collabora_code_port: 9981 # default: 9980
collabora_code_username: code # default: admin
collabora_code_password: # default: "{{ vault_collabora_code_password }}"
collabora_code_ssl_enabled: false # default: true
collabora_code_remote_font_config_url: https://nextcloud.example.com/apps/richdocuments/settings/fonts.json
```

And include it in your playbook.

```yml
- hosts: nextcloud
  roles:
  - role: collabora_code
```

## Docs

### Nginx config

Setup this Nginx configuration for the `doc01` host:

```conf
  - src_hostname: doc.example.com
    dest_hostname: doc01
    dest_port: 9980
    tls: true
    monitor: false
    options: |
      # static files
      location ^~ /browser {
        proxy_pass https://doc01:9980;
        proxy_set_header Host $http_host;
      }

      # WOPI discovery URL
      location ^~ /hosting/discovery {
        proxy_pass https://doc01:9980;
        proxy_set_header Host $http_host;
      }

      # Capabilities
      location ^~ /hosting/capabilities {
        proxy_pass https://doc01:9980;
        proxy_set_header Host $http_host;
      }

      # main websocket
      location ~ ^/cool/(.*)/ws$ {
        proxy_pass https://doc01:9980;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_set_header Host $http_host;
        proxy_read_timeout 36000s;
      }

      # download, presentation and image upload
      location ~ ^/(c|l)ool {
        proxy_pass https://doc01:9980;
        proxy_set_header Host $http_host;
      }

      # Admin Console websocket
      location ^~ /cool/adminws {
        proxy_pass https://doc01:9980;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_set_header Host $http_host;
        proxy_read_timeout 36000s;
      }
```
