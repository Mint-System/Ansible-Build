# K3s role

Deploy Kubernetes cluster with K3s. 

## Usage

Configure the role.

**vars.yml**

```yml
k3s_version: v1.23.5
```

And include it in your playbook.

```yml
- hosts: server
  roles:
  - role: k3s
- hosts: agent
  roles:
  - role: k3s
```
