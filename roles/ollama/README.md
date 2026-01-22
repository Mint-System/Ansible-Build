<img src="/logos/ollama.png" alt="ollama logo" width="100" height="100">

# Ollama role

Setup Ollama and deploy models.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/ollama/ollama
ollama_image: ollama/ollama:0.6.2
ollama_hostname: ollama01
ollama_description: LLM # default: Ollama
ollama_native: true # default: false
ollama_models:
  - name: olmo2:13b
  - name: olmo2:13b
ollama_api_key: # default: {{ vault_ollama_api_key }}
```

And include it in your playbook.

```yml
- hosts: ollama
  roles:
  - role: ollama  
```

## Docs

### Ollama cli

List models.

```bash
ollama list
```

### Ollama service

Show systemd logs.

```bash
sudo journalctl --unit=ollama.service --no-pager
```

### Connect LLM cli to remote model

Connecting the [LLM](https://llm.datasette.io/en/stable/) cli with a hosted model is simple.

Open the command line and export the env vars from the Ansible output.

```bash
export OLLAMA_HOST=http://llm.example.com:11434
llm -m olmo2:13b "Tell me a joke"
```