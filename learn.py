#!/usr/bin/env python3
"""
Module for me to experiment with Python to learn it.
"""

from collections import Counter
import re
import incmod


# pylint: disable=too-many-locals
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

    # Dict.
    mydict = {'x': 42, 'y': 3.14, 'z': 'zee'}
    assert mydict['x'] == 42
    assert mydict['z'] == 'zee'

    # Default value for undefined dict element.
    mydict1 = {}
    mydict1['a'] = mydict1.get('a', 0) + 1
    assert mydict1['a'] == 1
    # Better solution: Counter
    mycounter = Counter()
    mycounter['a'] += 1
    assert mycounter['a'] == 1

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

    # Lists
    firstl = [1, 2, 3]
    secondl = firstl * 2
    assert secondl == [1, 2, 3, 1, 2, 3]

    thirdl = firstl + [4, 5, 6]
    assert thirdl == [1, 2, 3, 4, 5, 6, ]
    assert 4 in thirdl
    assert 9 not in thirdl

    assert thirdl[2] == 3
    assert thirdl[-1] == 6
    assert thirdl[-2] == 5
    thirdl[-2] = -5
    assert thirdl[-2] == -5

    thirdl.append(7)
    assert thirdl[-1] == 7
    assert thirdl.pop() == 7
    assert thirdl[-1] == 6

    thirdl = firstl + [4, 5, 6]
    assert thirdl == [1, 2, 3, 4, 5, 6, ]

    print('Bye!')


# This code only runs when the file is executed directly.
if __name__ == '__main__':
    main()
