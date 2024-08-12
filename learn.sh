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


# First let's try a one-liner
echo "123foo456" | python3 -c "import sys, re; [sys.stdout.write(re.sub(r'foo', 'bar', line)) for line in sys.stdin]" >learn.tmp
ASSRT "$? -eq 0"
egrep '123bar456' learn.tmp >/dev/null
ASSRT "$? -eq 0"


# Not one-liner:
echo "123foo456" | python3 -c "
import sys, re
for line in sys.stdin:
    sys.stdout.write(re.sub(r\"foo\", \"bar\", line))" >learn.tmp
egrep '123bar456' learn.tmp >/dev/null
ASSRT "$? -eq 0"


flake8 learn.py
ASSRT "$? -eq 0"

pylint -sn -r n learn.py
ASSRT "$? -eq 0"

./learn.py
ASSRT "$? -eq 0"
