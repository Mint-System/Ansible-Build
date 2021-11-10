# Ansible BIRT role

Deploy BIRT container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/phusion/baseimage
birt_image: phusion/baseimage:0.9.18
birt_hostname: birt01
birt_description: Reporting # default: BIRT
birt_data_dir: /usr/share/birt # default: "/usr/share/{{ birt_hostname }}"
```

And include it in your playbook.

```yml
- hosts: birt
  roles:
  - role: birt
```

## Docs

### Build locally

Copy the build files.

```bash
mkdir /var/tmp/birt && cd $_
cp /home/$USERNAME/Ansible-Playbooks/roles/birt/templates/* .
cp /home/$USERNAME/Ansible-Playbooks/roles/birt/files/* .
```

Pull dependencies.

```bash
./get_dependencies
```

Build with Docker.

```bash
docker build . -t birt:custom
```