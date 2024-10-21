# K3s role

Deploy Kubernetes cluster with K3s. 

## Usage

Configure the role.

**vars.yml**

```yml
k3s_version: v1.23.5
k3s_token: # default: {{ vault_k3s_token }}
k3s_url: https://192.168.178.20:6443
```

And include it in your playbook.

```yml
- name: K3s server
  hosts: server
  roles:
    - role: k3s
  tags:
    - k3s
    - k3s_server

- name: K3s agent
  hosts: agent
  roles:
    - role: k3s
  tags:
    - k3s
    - k3s_agent
```

The following tags are available:

* k3s
* k3s_sever
* k3s_agent

## Docs

### Setup cluster access

```bash
sudo chmod 644 /etc/rancher/k3s/k3s.yaml
cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
```