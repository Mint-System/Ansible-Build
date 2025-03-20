# Ollama role

Setup Ollama and deploy models.

## Usage

Configure the role.

```yml
ollama_enabled: true
ollama_models:
  - name: olmo2:13b
```

And include it in your playbook.

```yml
- hosts: ollama
  roles:
  - role: ollama
```
