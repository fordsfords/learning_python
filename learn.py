#!/usr/bin/env python3
"""
Module for me to experiment with Python to learn it.
"""

import re
import incmod


def main():
    """
    Unit tests (only executed when module is run directly).
    """

    # Simple module
    assert incmod.inc(4) == 5

    # Bracketed continuation
    assert incmod.inc(
        4-1
    ) == 5-1

    # Simple regular expression substitution.
    # Use \g<1> instead of \1 to get append of 00.
    line = 'id="1234" name="Steve\'s Place"'
    mod_line = re.sub(r'id="(\d+)"\s+name="([^"]+)"', r"\2 \g<1>00", line)
    assert mod_line == "Steve's Place 123400"

    # Unpacking
    first, second, third = [1, 2, 3]
    assert (first == 1) and (second == 2) and (third == 3)
    first, *secondlist, third = [1, 2, 3]
    assert (first == 1) and (secondlist == [2, ]) and (third == 3)

    # Dict init.
    mydict = {'x': 42, 'y': 3.14, 'z': 'zee'}
    assert mydict['z'] == 'zee'

    # Ternary.
    incmod_res = incmod.inc(1)
    secondstr = 'two' if incmod_res == 2 else 'not two'
    assert secondstr == 'two'

    # Division
    firstfp = 3.0
    secondfp = 2.0
    thirdfp = firstfp / secondfp
    assert thirdfp == 1.5
    thirdfp = firstfp // secondfp
    assert thirdfp == 1.0

    print('Bye!')


# This code only runs when the file is executed directly.
if __name__ == '__main__':
    main()
