# Ansible Node Exporter role

Deploys node-exporter container.

## Requires

The Ansible node-exporter role requires the following roles:

* docker
* docker-network

## Usage

Configure the role.

**vars.yml**

```yml
node_exporter_image: prom/node-exporter:v0.18.1
node_exporter_hostname: node01
```

And include it in your playbook.

```yml
- hosts: node-exporter
  roles:
  - role: docker
    tags: docker
  - role: docker-network
    tags: docker-network
  - role: node-exporter
    tags: node-exporter
```

## Docs

By default to node-exporter mounts the host filesystem to `/hostfs`.