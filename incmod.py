"""
incmod.py - Simple module.
"""

from typing import Union


def inc(value: Union[int, float]) -> Union[int, float]:
    """
    Demo function.
    """

    return value + 1


def selftest():
    """
    Unit tests. Called when the module is run as a standalone program.
    """

    assert inc(5) == 6


if __name__ == "__main__":
    # This block allows the module to be run standalone for testing
    selftest()
