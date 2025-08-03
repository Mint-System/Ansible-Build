<img src="/logos/k3s.png" alt="k3s logo" width="100" height="100">

# K3s role

Deploy Kubernetes cluster with K3s.

## Usage

Configure the role.

```yml
# https://update.k3s.io/v1-release/channels
k3s_version: v1.33.3+k3s1
k3s_token: # default: {{ vault_k3s_token }}
k3s_server: true # default: false
k3s_agent: false # default: true
k3s_url: https://192.168.178.20:6443
```

And include it in your playbook.

```yml
- hosts: k3s
  roles:
  - role: k3s
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
