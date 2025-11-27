#!/usr/bin/env bash
set -euo pipefail


# For locating files relative to the script location (the result may be relative).
dirname=$(dirname "$0")

# For getting the script's filename (with extension).
basename=$(basename "$0")
