# Docker Network role

Configures a Docker network.

## Usage

Configure the role.

```yml
docker_network_name: example.com
docker_network_driver: overlay # defaults: bridge
docker_network_subnet: 172.18.0.0/24
```

And include it in your playbook.

```yml
- hosts: docker_network
  roles:
  - role: docker_network
```

## Docs

### IP tables

The `docker-proxy` ceates NAT routes in the ip tables. To list them run:

```
sudo iptables -t nat -L DOCKER -n -v
```
