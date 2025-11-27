#! /usr/bin/env bash
set -euo pipefail

cd $(dirname "$0")

poetry run python -u -m how_to_ddp
