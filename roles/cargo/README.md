# cargo role

Setup Rust toolchain and cargo package manager.

## Usage

Configure the role.

```yml
cargo_enabled: true
cargo_packages:
  - name: client
    git: https://github.com/tonarino/innernet
    tag: v1.5.5
  - name: server
    git: https://github.com/tonarino/innernet
    tag: v1.5.5
```

And include it in your playbook.

```yml
- hosts: cargo
  roles:
  - role: cargo
```
