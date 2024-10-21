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