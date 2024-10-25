# BigBlueButton role

Configures an installed BigBlueButton instance.

## Usage

Configure the role.

```yml
# https://docs.bigbluebutton.org/2.3/install.html
bigbluebutton_apt_repo_url: https://ubuntu.bigbluebutton.org/xenial-220/
bigbluebutton_hostname: bbb.example.com
bigbluebutton_api_url: https://bbb.example.com/bigbluebutton/
bigbluebutton_certbot_email: info@example.com
bigbluebutton_coturn_domain: turn.example.com

# https://hub.docker.com/r/bigbluebutton/greenlight
greenlight_image: bigbluebutton/greenlight:v2.14.4
greenlight_hostname: green01
greenlight_description: BBB-GUI # default: Greenlight
greenlight_port: 127.0.0.1:4000  # default: 127.0.0.1:5000
greenlight_secret_key_base: "{{ vault_greenlight_secret_key_base }}"
greenlight_safe_hosts: bbb.example.com,meet.example.com # default: "{{ bigbluebutton_hostname }}"

greenlight_db_adapter: postgresql
greenlight_db_host: postgres01
greenlight_db_port: "1234" # default: "5432"
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

greenlight_default_registration: closed # default: open
greenlight_allow_greenlight_accounts: "false" # default: "true"
greenlight_room_features: mute-on-join # default: mute-on-join,require-moderator-approval,anyone-can-start,all-join-moderator
greenlight_allow_mail_notifications: "false" # default: "true"
greenlight_admin_email: admin@example.com
greenlight_admin_password: "{{ vault_greenlight_admin_password }}"
```

And include it in your playbook.

```yml
- hosts: bigbluebutton
  roles:
  - role: bigbluebutton
```

The following tags are available:

* ubuntu1804
* letsencrypt
* html5
* https
* greenlight
* coturn
