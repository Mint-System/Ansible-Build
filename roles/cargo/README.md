# cargo role

Setup Rust toolchain and cargo package manager.

## Usage

Configure the role.

**vars.yml**

```yml
cargo_enabled: true
cargo_packages:
  - name: client
    git: https://github.com/tonarino/innernet
    tag: v1.5.0
  - name: server
    git: https://github.com/tonarino/innernet
    tag: v1.5.0
```

And include it in your playbook.

```yml
- hosts: cargo
  roles:
  - role: cargo
```
