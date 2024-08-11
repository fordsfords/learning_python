#!/bin/bash
# learn.sh - test the "learn.py" program.

# Example: blah; ASSRT "$? -eq 0"
ASSRT() {
  eval "test $1"

  if [ $? -ne 0 ]; then
    echo "ASSRT ERROR, `date`: `basename ${BASH_SOURCE[1]}`:${BASH_LINENO[0]}, not true: '$1'" >&2
    exit 1
  fi
}  # ASSRT


flake8 learn.py
ASSRT "$? -eq 0"

pylint -sn -r n learn.py
ASSRT "$? -eq 0"

./learn.py
ASSRT "$? -eq 0"
