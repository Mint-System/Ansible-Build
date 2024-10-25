# RabbitMQ role

Deploy RabbitMQ container.

## Usage

Configure the role.

```yml
# https://registry.hub.docker.com/_/rabbitmq/
rabbitmq_image: rabbitmq:3.8-management
rabbitmq_build_image: true # default: false
rabbitmq_description: Database for website # default: RabbitMQ
rabbitmq_hostname: mq01
rabbitmq_volume_name: mq_data01 # default: "{{ rabbitmq_hostname}}"
rabbitmq_dir: /usr/share/mq # default: "/usr/share/{{ odoo_hostname }}"
rabbitmq_ports:
  - 127.0.0.1:5673:5672 # default: 127.0.0.1:5672:5672
  - 127.0.0.1:8080:15672
rabbitmq_user: example
rabbitmq_password: # default: "{{ vault_rabbitmq_password }}"
```

And include it in your playbook.

```yml
- hosts: rabbitmq
  roles:
  - role: rabbitmq
```

## Docs

### Install AMQP tools

Install `amqp-tools`

```console
apt-get install amqp-tools
```

This package provides two main methods

* amqp-consume
* amqp-publish

### Start an AMQP consumer

Start the AMQP consumer.

```console
URL=amqp://admin:admin@127.0.0.1:5672
QUEUE=test
TOPIC=amq.topic
ROUTE=worker1
amqp-consume -u "$URL" -q "$QUEUE" -e "$TOPIC" -r "$ROUTE" -d cat
```

### Publish an AMQP message

```console
URL=amqp://admin:admin@127.0.0.1:5672
QUEUE=test
TOPIC=amq.topic
ROUTE=worker1
amqp-publish -u "$URL" -e "$TOPIC" -r "$ROUTE" -b "Hello AMQP"
```