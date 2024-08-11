#!/bin/bash
# echo.sh - test the "echo.py" program.

# Example: blah; ASSRT "$? -eq 0"
ASSRT() {
  eval "test $1"

  if [ $? -ne 0 ]; then
    echo "ASSRT ERROR, `date`: `basename ${BASH_SOURCE[1]}`:${BASH_LINENO[0]}, not true: '$1'" >&2
    exit 1
  fi
}  # ASSRT


pylint -sn -r n echo.py
ASSRT "$? -eq 0"

# Output is expected.
echo "echo success" | ./echo.py >echo.tmp
ASSRT "$? -eq 0"
egrep 'success' echo.tmp >/dev/null
ASSRT "$? -eq 0"

# No output is expected.
echo " echo fail" | ./echo.py >echo.tmp
ASSRT "$? -eq 0"
egrep 'fail' echo.tmp >/dev/null
ASSRT "$? -ne 0"

echo "success"
exit 0
