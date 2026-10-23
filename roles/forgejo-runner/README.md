---
kind: service
---

<img src="/logos/forgejo-runner.png" alt="forgejo-runner logo" width="100" height="100">

# Forgejo Runner role

Deploy Forgejo runner container. The runner uses the host Docker daemon to spawn jobs.

## Usage

Configure the role.

```yml
# https://code.forgejo.org/forgejo/runner/pkgs/container/runner
forgejo_runner_image: code.forgejo.org/forgejo/runner:13.2.0 # default
forgejo_runner_hostname: runner01 # default: runner
forgejo_runner_description: Forgejo Runner # default: Forgejo Runner
forgejo_runner_instance_url: https://codeberg.org/ # default
forgejo_runner_instance_uuid: 3e027763-5262-4781-8d60-def47f6a9afd
forgejo_runner_instance_token: # default: "{{ vault_forgejo_runner_instance_token }}"
forgejo_runner_labels: ["docker:docker://node:lts"] # default
forgejo_runner_volume_name: runner01 # default: "{{ forgejo_runner_hostname }}"
forgejo_runner_data_dir: /usr/share/runner01 # default: "/usr/share/{{ forgejo_runner_hostname }}"
```

And include it in your playbook.

```yml
- hosts: setup
  roles:
  - role: forgejo-runner
```

## Docs

### Create runner

Create a runner on the Forgejo instance: https://codeberg.org/org/Mint-System/settings/actions/runners/new

Set the connection details.

```bash
task encrypt-string mint_system "vault_forgejo_runner_instance_token" "<runner token>"
```

The runner token and UUID are shown only once when the runner is created.

### Jobs with Docker

The runner connects to the host Docker daemon over `/var/run/docker.sock`. Workflows declare a label, e.g. `runs-on: docker`, to run jobs in containers.
