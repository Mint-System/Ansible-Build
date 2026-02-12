Read the AGENTS.md and README.md to get an understanding of the project.

```zsh
#compdef task

# Function to complete Docker container names
_docker_container_complete() {
    local -a containers
    containers=($(docker ps --all --format="{{.Names}}"))
    _describe 'Docker containers' containers
}

# Register completion for all docker-odoo-* scripts
local -a scripts
scripts=(${(f)"$(compgen -c | grep -E '^docker-odoo-')"})
if (( ${#scripts[@]} > 0 )); then
    for script in "${scripts[@]}"; do
        compdef "_docker_container_complete" "$script"
    done
fi
```