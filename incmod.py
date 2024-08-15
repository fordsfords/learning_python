"""
incmod.py - Simple module.
"""


def inc(value, inc_by=1):
    """
    Demo function.
    """

    if value == 42:
        raise ValueError("You're already at 42, what more do you want?")

    return value + inc_by


def selftest():
    """
    Unit tests. Called when the module is run as a standalone program.
    """

    assert inc(5) == 6


if __name__ == "__main__":
    # This block allows the module to be run standalone for testing
    selftest()
