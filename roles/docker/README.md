# Docker role

Installs Docker for Ubuntu and CentOS.

## Requires

The Ansible Docker role has the following requirements:

* Distribution: Ubuntu, Debian, CentOS or Rocky

## Usage

Configure all depending roles.

```yml
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
docker_apt_url: "https://download.docker.com/linux/ubuntu/gpg"
docker_apt_repo: "deb https://download.docker.com/linux/ubuntu xenial stable"
docker_packages:
  - name: apt-transport-https
    version: 1.2.32
  - name: ca-certificates
    version: 20170717~16.04.2
  - name: curl
    version: 7.47.0-1ubuntu2.14
  - name: software-properties-common
    version: 0.96.20.9
  - name: python3-pip
    version: 8.1.1-2ubuntu0.4
  - name: python3-setuptools
  - name: docker-ce
    version: 5:19.03.8~3-0~ubuntu-xenial

# yum package manager
docker_yum_url: https://download.docker.com/linux/centos/docker-ce.repo
docker_yum_repo: docker-ce-edge
docker_packages:
  - name: docker-ce
    version: 19.03.12
  - name: docker-ce-cli
    version: 19.03.12
  - name: containerd.io
    version: 1.2.13
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
