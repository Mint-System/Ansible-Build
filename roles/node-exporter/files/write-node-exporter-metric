#!/bin/bash

# Display Help
Help() {
    echo
    echo "write-node-exporter-metric"
    echo "##########################"
    echo
    echo "Description: Write node-exporter metric."
    echo "Syntax: write-node-exporter-metric [-n|-c|-v|help]"
    echo "Example: write-node-exporter-metric -n cron_job -c \"Renew certs for proxy01\" -v 0"
    echo "options:"
    echo "  -n    Reference of custom metric type. Defaults to 'cron_job'"
    echo "  -c    Code for metric value."
    echo "  -v    Value of metric."
    echo "  help  Show write-node-exporter-metric help."
    echo
}

# Show help and exit
if [[ $1 == 'help' ]]; then
    Help
    exit
fi

# Process params
while getopts ":n :c: :v:" opt; do
  case $opt in
    n) TYPE="$OPTARG"
    ;;
    c) CODE="$OPTARG"
    ;;
    v) VALUE="$OPTARG"
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
    Help
    exit;;
  esac
done

# Fallback to environment vars and default values
: ${TYPE:='cron_job'}

[[ -z "$CODE" ]] && { echo "Parameter -c|code is empty" ; exit 1; }
[[ -z "$VALUE" ]] && { echo "Parameter -v|value is empty" ; exit 1; }

if [ "$TYPE" == "cron_job" ]; then
    echo "Write metric node_cron_job_exit_code for code \"$CODE\" with value $VALUE."
    ID=$(echo $CODE | shasum | cut -c1-5)

    cat << EOF >> /var/tmp/node_cron_job_exit_code.$ID.prom.$$
# HELP node_cron_job_exit_code Last exit code of cron job.
# TYPE node_cron_job_exit_code counter
node_cron_job_exit_code{code="$CODE"} $VALUE
EOF
    mv /var/tmp/node_cron_job_exit_code.$ID.prom.$$ /var/tmp/node_cron_job_exit_code.$ID.prom
fi
