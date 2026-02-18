---
title: Format all versioned bash scripts
---

This documents provides instructions for an LLM agent.

Read the AGENTS.md.

Format all versioned bash scripts. Versioned means that they either have a `version=` or `script=` statement:

- Move fallback vars before while loop
- Bump the minor version
- Remove comments
- If missing add `version=1.0.1` statement after `script=`

Here is an example: /home/janikvonrotz/Ansible-Build/roles/docker_volume/files/docker-volume-import

Before formatting the content is:

```
#!/usr/bin/env bash
set -e

# Get script name
script=$(basename "$0")
version="1.0.0"

# Display Help
help() {
    echo
    echo "$script"
    echo
    echo 'Description: Import Docker volume content.'
    echo "Syntax: $script [-v|-p|-o|-V|help]"
    echo 'Example: $script -v odoo01 -p /filestore/odoo -f /var/tmp/odoo01.tar'
    echo 'options:'
    echo '  -v    Name of Docker volume.'
    echo "  -p    Path in volume. Defaults to '/'"
    echo '  -f    Path to tar file.'
    echo '  -r    Replace content in path.'
    echo "  -V    Show $script version."
    echo "  help  Show $script manual."
    echo
}

# Show help and exit
if [[ "$1" == 'help' ]]; then
    help
    exit
fi

# Initialise option flags
replace=False

# Process params
while getopts ":v: :p: :f: :r :V" opt; do
    case $opt in
        v) volume="$OPTARG"
        ;;
        p) path="$OPTARG"
        ;;
        f) file="$OPTARG"
        ;;
        r) replace=True
        ;;
        V) echo "$script version $version"
        exit 0
        ;;
        \?) echo "Invalid option -$OPTARG" >&2
        help
        exit 1;;
    esac
done

# Fallback to environment vars and default values
: "${path:=/}"

# Verify variables
[[ -z "$volume" ]] && [[ -z "$all" ]] && { echo 'Parameter -v|volume' ; exit 1; }

# Process vars
filename=$(basename "$file")
filepath=$(dirname "$file")

if [[ $replace = True ]]; then
    echo "Clear $path folder in $volume volume..."
    docker run --rm \
      -v "$volume:/target" \
      alpine rm -rf /target$path
fi

# Run export 
echo "Import content of $volume volume to $path path..."
docker run --rm \
  -v "$volume:/target" \
  -v "${filepath}:/source" \
  alpine /bin/ash -c "
    mkdir -p /target$path
    cd /target$path
    tar xf /source/$filename --strip-components=1"

# Notify if import has finished
echo "Docker volume import has finished."
```

And after formatting the content is:

```
#!/usr/bin/env bash
set -e

script=$(basename "$0")
version="1.0.1"

help() {
    echo
    echo "$script"
    echo
    echo 'Description: Import Docker volume content.'
    echo "Syntax: $script [-v|-p|-o|-V|help]"
    echo 'Example: $script -v odoo01 -p /filestore/odoo -f /var/tmp/odoo01.tar'
    echo 'options:'
    echo '  -v    Name of Docker volume.'
    echo "  -p    Path in volume. Defaults to '/'"
    echo '  -f    Path to tar file.'
    echo '  -r    Replace content in path.'
    echo "  -V    Show $script version."
    echo "  help  Show $script manual."
    echo
}

if [[ "$1" == 'help' ]]; then
    help
    exit
fi

replace=False
path=/

while getopts ":v: :p: :f: :r :V" opt; do
    case $opt in
        v) volume="$OPTARG"
        ;;
        p) path="$OPTARG"
        ;;
        f) file="$OPTARG"
        ;;
        r) replace=True
        ;;
        V) echo "$script version $version"
        exit 0
        ;;
        \?) echo "Invalid option -$OPTARG" >&2
        help
        exit 1;;
    esac
done

[[ -z "$volume" ]] && [[ -z "$all" ]] && { echo 'Parameter -v|volume' ; exit 1; }

filename=$(basename "$file")
filepath=$(dirname "$file")

if [[ $replace = True ]]; then
    echo "Clear $path folder in $volume volume..."
    docker run --rm \
      -v "$volume:/target" \
      alpine rm -rf /target$path
fi

echo "Import content of $volume volume to $path path..."
docker run --rm \
  -v "$volume:/target" \
  -v "${filepath}:/source" \
  alpine /bin/ash -c "
    mkdir -p /target$path
    cd /target$path
    tar xf /source/$filename --strip-components=1"

echo "Docker volume import has finished."
```