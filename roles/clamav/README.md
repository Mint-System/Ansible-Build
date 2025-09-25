<img src="/logos/clamav.png" alt="clamav logo" width="100" height="100">

# ClamAV role

Deploy ClamAV container for antivirus scanning.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/clamav/clamav/
clamav_image: clamav/clamav:1.4.3
clamav_hostname: clamav01
clamav_data_dir: /usr/share/clamav # default: /usr/share/{{ clamav_hostname }}
```

And include it in your playbook.

```yml
- hosts: nextcloud
  roles:
  - role: collabora_code
```

## Docs

### Connext Nexctloud Antivirus for files

Install the app <https://apps.nextcloud.com/apps/files_antivirus> then open *Settings > Security > Antivirus for files*.

* **Mode**: ClamAV-Demon
* **Host**: clamav01
* **Port**: 3310 

Test Antivirus with with <https://secure.eicar.org/eicar.com.txt>. Check the `clamav01` log for a message like:

```
Thu Sep 25 08:37:43 2025 -> instream(10.0.0.6@46498): Win.Test.EICAR_HDB-1 FOUND
```