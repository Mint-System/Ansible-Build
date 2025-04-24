<img src="/logos/docker.png" alt="docker logo" width="100" height="100">

# Docker role

Installs Docker for Ubuntu and CentOS.

## Requires

The Ansible Docker role has the following requirements:

* Distribution: Ubuntu, Debian, CentOS or Rocky

## Usage

Configure all depending roles.

```yml
docker_ipv6_enabled: true # default: false
docker_dns: "[\"172.17.4.1\", \"8.8.8.8\"]"
docker_data_dir: /mnt/sdb/docker # defaults: /var/lib/docker
docker_build_dir: /tmp/build # defaults: /srv/build
docker_group: container # default: docker
docker_log_driver: "local" # defaults: "json-file
docker_log_max_size: "50m" # defaults: "10m"
docker_log_max_file: "5" # defaults: "3"
docker_login_username: example
docker_login_password: # default: "{{ vault_docker_login_password }}"
docker_login_users: # default: root
  - git-bot

# apt package manager
docker_apt_url: "https://download.docker.com/linux/debian/gpg"
docker_apt_repo: "deb https://download.docker.com/linux/debian bookworm stable"
docker_packages:
  - name: docker-ce

# yum package manager
docker_yum_url: https://download.docker.com/linux/centos/docker-ce.repo
docker_yum_repo: docker-ce-edge
docker_packages:
  - name: docker-ce 
  - name: docker-ce-cli
  - name: containerd.io
```

Include it in your playbook.

```yml
- hosts: docker
  roles:
  - role: docker
```

The following tags are available:

* docker
* docker-ubuntu
* docker-centos
* docker-debian
* docker-rocky

## Docs

### Manage Docker service

Restart Docker service:

```bash
sudo service docker restart
```

### Show Docker log

Show logs for selected unit:

```bash
journalctl -u docker -f
```