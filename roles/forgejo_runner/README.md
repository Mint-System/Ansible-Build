---
kind: service
---

<img src="/logos/forgejo_runner.png" alt="forgejo_runner logo" width="100" height="100">

# Forgejo Runner role

Deploy Forgejo runner container. The runner uses the host Docker daemon to spawn jobs.

## Usage

Configure the role.

```yml
# https://code.forgejo.org/forgejo/runner/pkgs/container/runner
forgejo_runner_image: code.forgejo.org/forgejo/runner:13.2.0 # default
forgejo_runner_hostname: runner01 # default: runner
forgejo_runner_description: Forgejo Runner # default: Forgejo Runner
forgejo_runner_connections: # default: "{{ vault_forgejo_runner_connections }}"
  - name: forgejo
    url: https://codeberg.org/
    uuid: 3e027763-5262-4781-8d60-def47f6a9afd
    token: <runner token>
    labels: ["docker:docker://node:lts"] # optional, default: "{{ forgejo_runner_labels }}"
forgejo_runner_labels: ["docker:docker://node:lts"] # default
forgejo_runner_force_pull: false # default
forgejo_runner_volume_name: runner01 # default: "{{ forgejo_runner_hostname }}"
forgejo_runner_data_dir: /usr/share/runner01 # default: "/usr/share/{{ forgejo_runner_hostname }}"
```

And include it in your playbook.

```yml
- hosts: setup
  roles:
  - role: forgejo_runner
```

## Docs

### Create runner

Create a runner on the Forgejo instance: https://codeberg.org/org/Mint-System/settings/actions/runners/new

Add the connection to the encrypted vault variable.

```yml
vault_forgejo_runner_connections:
  - name: forgejo
    url: https://codeberg.org/
    uuid: 3e027763-5262-4781-8d60-def47f6a9afd
    token: <runner token>
```

Encrypt the value with `ansible-vault encrypt_string` and store it in the host `vault.yml`. The runner token and UUID are shown only once when the runner is created.

Each entry in `forgejo_runner_connections` registers the runner on another instance or organization.

### Jobs with Docker

The runner connects to the host Docker daemon over `/var/run/docker.sock`. Workflows declare a label, e.g. `runs-on: docker`, to run jobs in containers.

Set `forgejo_runner_force_pull: true` to pull job images even when a local copy of the tag exists. Without it the runner reuses a stale `latest` image indefinitely.
