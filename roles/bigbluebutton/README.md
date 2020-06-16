# Ansible BigBlueButton role

Installs BigBlueButton with https and greenlight.

## Usage

Configure the role.

**vars.yml**

```yml
bigbluebutton_apt_repo_url: https://ubuntu.bigbluebutton.org/xenial-220/
bigbluebutton_hostname: bbb.example.com
bigbluebutton_api_url: http://bbb.example.com/bigbluebutton/
bigbluebutton_external_ip: 116.203.41.151
bigbluebutton_certbot_email: info@example.com

# https://hub.docker.com/r/bigbluebutton/greenlight
greenlight_image: bigbluebutton/greenlight:release-2.6.4
greenlight_hostname: green01
greenlight_secret_key_base: "{{ vault_greenlight_secret_key_base }}"
greenlight_safe_hosts: bbb.example.com
greenlight_db_adapter: postgresql
greenlight_db_host: postgres01
greenlight_db_port: "5432"
greenlight_db_name: greenlight
greenlight_db_username: greenlight
greenlight_db_password: "{{ vault_greenlight_db_password }}"
greenlight_smtp_server: mail.example.com
greenlight_smtp_auth: login
greenlight_smtp_port: "587"
greenlight_smtp_domain: example.com
greenlight_smtp_sender: noreply@example.com
greenlight_smtp_username: bot@example.com
greenlight_smtp_password: "{{ vault_greenlight_smtp_password }}"
greenlight_default_registration: open
greenlight_allow_greenlight_accounts: "true"
greenlight_room_features: mute-on-join,require-moderator-approval,anyone-can-start,all-join-moderator
greenlight_allow_mail_notifications: "true"
greenlight_admin_email: admin@example.com
greenlight_admin_password: "{{ vault_greenlight_admin_password }}"
```

And include it in your playbook.

```yml
- hosts: bigbluebutton
  roles:
  - role: bigbluebutton
    tags:
    - biglbuebutton
    - biglbuebutton-core
    - biglbuebutton-letsencrypt
    - biglbuebutton-https
    - biglbuebutton-greenlight
```

The following tags are available:

* biglbuebutton
* biglbuebutton-core
* biglbuebutton-letsencrypt
* biglbuebutton-https
* biglbuebutton-greenlight