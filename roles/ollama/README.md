# Ollama role

Setup Ollama and deploy models.

## Usage

Configure the role.

```yml
ollama_enabled: true
ollama_models:
  - name: olmo2:13b
  - name: olmo2:13b
ollama_api_key: # default: {{ vault_ollama_api_key }}
openweb_ui_image: ghcr.io/open-webui/open-webui:main
openweb_ui_hostname: openwebui01
openweb_ui_description: Ollama Chat # default: LLM Chat
openweb_ui_ports: # default: []
  - 8080:3000
```

And include it in your playbook.

```yml
- hosts: ollama
  roles:
  - role: ollama  
```

## Docs

### Connect LLM cli to remote model

Connecting the [LLM](https://llm.datasette.io/en/stable/) cli with a hosted model is simple.

Open the command line and export the env vars from the Ansible output.

```bash
 export OLLAMA_HOST=http://llm.example.com:11434 
llm -m olmo2:13b "Tell me a joke"
```