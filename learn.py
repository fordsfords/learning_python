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

    line = 'id="1234" name="Steve\'s Place"'
    mod_line = re.sub(r'id="(\d+)"\s+name="([^"]+)"', r"\2 \g<1>00", line)
    assert mod_line == "Steve's Place 123400"

    print("Bye!")


# This code only runs when the file is executed directly.
if __name__ == "__main__":
    main()
