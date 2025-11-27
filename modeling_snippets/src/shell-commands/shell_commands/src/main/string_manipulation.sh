#!/usr/bin/env bash
set -euo pipefail

# Replace all occurrences of the word
# ${variable//pattern/replacement} does a global replace of pattern with replacement
s="This is a string"
new_s=${s//string/number}
echo "$new_s"

my_dir="path/to/directory"
new_dir=${my_dir//\//.}
echo "$new_dir"
