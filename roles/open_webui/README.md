<img src="/logos/open_webui.png" alt="open-webui logo" width="100" height="100">

# Open WebUI role

Deploy Open WebUI container.

## Usage

Configure the role.

```yml
# https://github.com/open-webui/open-webui
open_webui_image: ghcr.io/open-webui/open-webui:v0.7.0
open_webui_description: Open WebUI
open_webui_hostname: open_webui01
open_webui_volume_name: openwebui_data # default: "{{ open_webui_hostname }}"
open_webui_volumes:
  - "{{ open_webui_volume_name }}:/app/backend/data" # default: "{{ open_webui_volume_name }}:/app/backend/data"
open_webui_ports:
  - "8080:8080" # default: ["8080:8080"]
open_webui_proivder_name: Login Example
open_webui_oauth_client_id: "chatgpt.example.com"
open_webui_oauth_client_secret: # default: "{{ vault_open_webui_oauth_client_secret }}"
open_webui_openid_provider_url: "https://login.example.com/realms/example.com/.well-known/openid-configuration"
```

And include it in your playbook.

```yml
- hosts: open_webui
  roles:
  - role: open_webui
```

The following tags are available:

* open_webui