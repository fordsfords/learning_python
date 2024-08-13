#!/bin/sh
# msg_id_histo.sh

# Example: blah; ASSRT "$? -eq 0"
ASSRT() {
  eval "test $1"

  if [ $? -ne 0 ]; then
    echo "ASSRT ERROR, `date`: `basename ${BASH_SOURCE[1]}`:${BASH_LINENO[0]}, not true: '$1'" >&2
    exit 1
  fi
}  # ASSRT


echo flake8 msg_id_histo.py
flake8 msg_id_histo.py
ASSRT "$? -eq 0"

echo pylint -sn -r n msg_id_histo.py
pylint -sn -r n msg_id_histo.py
ASSRT "$? -eq 0"

echo mypy --check-untyped-defs msg_id_histo.py
mypy --check-untyped-defs --no-error-summary msg_id_histo.py
ASSRT "$? -eq 0"


echo ./msg_id_histo.py test_dro.log
./msg_id_histo.py test_dro.log >test_dro.pyout
ASSRT "$? -eq 0"

echo ./msg_id_histo.py test_store.log
./msg_id_histo.py test_store.log >test_store.pyout
ASSRT "$? -eq 0"
