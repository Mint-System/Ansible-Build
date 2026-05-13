---
title: "Remove docker network dependencies"
---

# Run 14

Note: @Agent refers to the AI agent (you) who is working on this task.

@Agent when working on this task, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on the task

## Context

Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

I used `task visualize-dependencies` to create a list of all roles that depend on `docker_network`:

```
graph TD
    pgadmin --> docker_network
    postfix --> docker_network
    postgres --> docker_network
    alloy --> docker_network
    cadvisor --> docker_network
    onlyoffice_documentserver --> docker_network
    mailhog --> docker_network
    open_webui --> docker_network
    meilisearch --> docker_network
    grafana --> prometheus
    meilisync --> docker_network
    caddy --> docker_network
    simple_mail_forwarder --> docker_network
    mariadb --> docker_network
    acme_sh --> docker_network
    php_fpm --> docker_network
    openldap --> docker_network
    pushgateway --> docker_network
    restic_server --> docker_network
    node_exporter --> docker_network
    coturn --> docker_network
    blackbox_exporter --> docker_network
    iam --> docker_network
    postgres_exporter --> docker_network
    certbot --> docker_network
    clamav --> docker_network
    prometheus --> docker_network
    alertmanager --> docker_network
    superset --> docker_network
    bigbluebutton_exporter --> docker_network
    jenkins --> docker_network
    nextcloud_exporter --> docker_network
    mysql --> docker_network
    redis --> docker_network
    mysqld_exporter --> docker_network
    fathom --> docker_network
    remark42 --> docker_network
    dind --> docker_network
    collabora_code --> docker_network
    rabbitmq --> docker_network
    mailpit --> docker_network
    loki --> docker_network
    nginx --> docker_network
    promtail --> docker_network
```

This roles depends on `docker_network` because they use the `docker_network_name` var. The roles also use `docker_log_driver`, `docker_log_max_size` and `docker_log_max_file` vars from the `docker` role.

Instead of depending on `docker_network` I would like to remove the vars from the role templates.

Here is an example: `roles/odoo/tasks/main.yml`

Before:

```yaml
	...
    networks:
      - name: "{{ docker_network_name }}"
    log_driver: "{{ docker_log_driver }}"
    log_options:
      max-size: "{{ docker_log_max_size }}"
      max-file: "{{ docker_log_max_file }}"
      tag: "{{ odoo_hostname }}|{{ role_name }}"
```

After:

```yaml
	...
    networks:
      - name: "{{ docker_network_name }}"
    log_options:
      tag: "{{ odoo_hostname }}|{{ role_name }}"
```

These default values shall be set on as global defaults in the `docker` role. They can be added like this:

```json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
```

Please do the following:

- Set global default for `docker_log-*` vars in docker daemon config
- Remove the docker_network dependency for all roles
- Remove `log_driver` and `log_options.max-size` and `log_options.max-file` from `community.docker.docker_container` tasks in all roles 

## Worklog

@Agent Add a summary here once the task has been completed.
