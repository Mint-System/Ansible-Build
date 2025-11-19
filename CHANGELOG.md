# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Do a port knocking in `certbot_check.yml` task.

### Changed

- Renamed `clean` to `cleanup`.
- Updated bash scripts to follow coding conventions from AGENTS.md
  - Removed 'function' keyword from all bash functions
  - Added 'local' declarations for variables inside functions
  - Converted uppercase local variables to lowercase
  - Updated conditional syntax from [ ] to [[ ]] where needed
  - Improved quoting with single quotes for literal strings
  - Updated more bash scripts including ansible-vault-get, get-public-ip, docker-mysql-list, and docker-mysql-drop
  - Changed shebang from #!/bin/bash to #!/usr/bin/env bash for portability
