########################
# Script documentation #
#!/usr/bin/env bash
#
# A shebang which tells the operating system to run the file
# using the 'bash' binary located by the 'env' program (i.e., "#!/usr/bin/env bash").

#############################
# Strict-mode documentation #
set -euo pipefail
#
# Enables a safer shell-script execution mode by combining three options:
#   -e : exit immediately if any simple command returns a non-zero status.
#   -u : treat unset variables and parameters as an error when performing
#        parameter expansion (throws and exits).
#   -o pipefail : pipefail ensures that failures inside pipelines are not masked by a succeeding final command.
#                 Without it, "cmd1 | cmd2" returns cmd2's exit code even if cmd1 failed.
#############################
