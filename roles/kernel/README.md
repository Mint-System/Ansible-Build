---
kind: system
---

<img src="/logos/kernel.png" alt="kernel logo" width="100" height="100">

# kernel role

Manage kernel module blacklisting.

## Usage

Configure the role.

```yml
kernel_blacklist:
  - name: algif_aead
  - name: another_module
```

And include it in your playbook.

```yml
- hosts: kernel
  roles:
  - role: kernel
```

The following tag is available:

* kernel
