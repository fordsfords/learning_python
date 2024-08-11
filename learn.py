#!/usr/bin/env python3
"""
Module for me to experiment with Python to learn it.
"""


def inc(value):
    """
    Demo function.
    """

    return value + 1


if __name__ == "__main__":
    # This code only runs when the file is executed directly.

    assert inc(4) == 5

    assert inc(  # Don't need backslash for bracketed continuation lines.
        4
    ) == 5

    print("Bye!")
