#!/bin/bash
# bld.sh

# Example: blah; ASSRT "$? -eq 0"
ASSRT() {
  eval "test $1"

  if [ $? -ne 0 ]; then
    echo "ASSRT ERROR, `date`: `basename ${BASH_SOURCE[1]}`:${BASH_LINENO[0]}, not true: '$1'" >&2
    exit 1
  fi
}  # ASSRT

for F in *.md; do :
  if egrep "<!-- mdtoc-start -->" $F >/dev/null; then :
    # Update doc table of contents (see https://github.com/fordsfords/mdtoc).
    if which mdtoc.pl >/dev/null 2>&1; then LANG=C mdtoc.pl -b "" $F;
    elif [ -x ../mdtoc/mdtoc.pl ]; then LANG=C ../mdtoc/mdtoc.pl -b "" $F;
    else echo "FYI: mdtoc.pl not found; Skipping doc build"; echo ""; fi
  fi
done


echo ruff check -q learn.py incmod.py
ruff check -q learn.py incmod.py

echo flake8 learn.py incmod.py
flake8 learn.py incmod.py
ASSRT "$? -eq 0"

echo pylint -sn -r n learn.py incmod.py
pylint -sn -r n learn.py incmod.py
ASSRT "$? -eq 0"

### echo mypy --check-untyped-defs learn.py incmod.py
### mypy --check-untyped-defs --no-error-summary learn.py incmod.py
echo mypy learn.py incmod.py
mypy --no-error-summary learn.py incmod.py
ASSRT "$? -eq 0"


echo "Build OK"
