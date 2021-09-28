# Ansible Docker role

Installs Docker for Ubuntu and CentOS.

## Requires

The Ansible Docker role has the following requirements:

* Distribution: Ubuntu, Debian or CentOS

## Usage

Configure all depending roles.

```yml
docker_data_dir: /mnt/server-disk2/docker # defaults: /var/lib/docker
docker_pip_packages:
  - name: docker==4.2.0  # defaults: "docker"
docker_log_driver: "local" # defaults: "json-file
docker_log_max_size: "50m" # defaults: "10m"
docker_log_max_file: "5" # defaults: "3"
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
docker_login_username: janikvonrotz
docker_login_password: "{{ vault_docker_login_password }}"
docker_login_email: login@janikvonrotz.ch
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