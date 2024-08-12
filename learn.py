#!/usr/bin/env python3
"""
Module for me to experiment with Python to learn it.
"""

import re


def inc(value):
    """
    Demo function.
    """

    return value + 1


def main():
    """
    Unit tests (only executed when module is run directly).
    """

    assert inc(4) == 5

    assert inc(  # Don't need backslash for bracketed continuation lines.
        4
    ) == 5

    # Simple regular expression substitution.
    # Use \g<1> instead of \1 to get append of 00.
    line = 'id="1234" name="Steve\'s Place"'
    mod_line = re.sub(r'id="(\d+)"\s+name="([^"]+)"', r"\2 \g<1>00", line)
    assert mod_line == "Steve's Place 123400"

    # Unpacking
    first, second, third = [1, 2, 3]
    assert (first == 1) and (second == 2) and (third == 3)
    first, *second, third = [1, 2, 3]
    assert (first == 1) and (second == [2, ]) and (third == 3)

    # Dict init.
    mydict = {'x': 42, 'y': 3.14, 'z': 'zee'}
    assert mydict['z'] == 'zee'

    # Ternary.
    first = inc(1)
    second = 'two' if first == 2 else 'not two'
    assert second == 'two'

    # Division
    first = 3.0
    second = 2.0
    third = first / second
    assert third == 1.5
    third = first // second
    assert third == 1.0

    print('Bye!')


# This code only runs when the file is executed directly.
if __name__ == '__main__':
    main()
