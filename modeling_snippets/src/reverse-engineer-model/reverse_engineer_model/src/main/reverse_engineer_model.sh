#!/usr/bin/env bash
set -euo pipefail

token=$1
function install_pkgs {
    if [[  $1 == 1 ]]; then
        echo "Installing required packages..."
        poetry run huggingface-cli login --token $token
    fi
}

cd $(dirname $0)

install_pkgs 1
poetry run python -u -m reverse_engineer_model
