# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Removed

- Removed `snap_packages` from `packages` role.

### Added

- Do a port knocking in `certbot_check.yml` task.
- Command `run` to execute Ansible commands.

### Changed

- BREAKING!: Renamed variables with `_proxy_basic_auth_` to `_basic_auth_`.
- Renamed `clean` to `cleanup`.
- Updated bash scripts to follow coding conventions from AGENTS.md.
- Merged `odoo_scripts` into `odoo` role.
- Set Python version to `3.10`.
- Remove version check in `requirements.txt`.
- Renamed `ssl` to `tls`
- Optimized backup scripts to delete destination files before creating new dumps to save disk space.
- Fixed `test-localhost` task to correctly display logs for all containers instead of only failed ones.
