Notes for an old Perl programmer learning Python.

* An assignment statement cannot be used as part of an expression.
* Two statements can be placed on one logical line separateing them with a semicolon,
but it is much frowned upon (and triggers flake8).
* Python "print" includes a final newline.
* You don't declare variables. Assignment sets the type.
  + Presumably means that some errors Perl catches at compile time, Python must find at
    run-time (assuming you can get the bad code to run).

| Python | Perl |
|--------|------|
| None   | undef |
| [dict (dictionary)](https://docs.python.org/3.11/library/stdtypes.html#mapping-types-dict) | hash |

