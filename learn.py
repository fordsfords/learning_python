#!/usr/bin/env python3
"""
Module for me to experiment with Python to learn it.
"""

from collections import Counter
import re
import incmod


# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
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

    # Exception
    inc_result = -1
    inc_msg = ""
    try:
        inc_result = incmod.inc(42)  # This raises ValueError
    except ValueError as inc_except:
        inc_result = -2
        inc_msg = str(inc_except)
    assert inc_result == -2
    assert re.search(r'what more do you want', inc_msg)

    # Simple regular expression substitution.
    # Use \g<1> instead of \1 to get append of 00.
    line = 'id="1234" name="Steve\'s Place"'
    mod_line = re.sub(r'id="(\d+)"\s+name="([^"]+)"', r"\2 \g<1>00", line)
    assert mod_line == "Steve's Place 123400"

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

    # Unpacking
    first, second, third = [1, 2, 3]
    assert (first == 1) and (second == 2) and (third == 3)
    first, *secondlist, third = [1, 2, 3]
    assert (first == 1) and (secondlist == [2, ]) and (third == 3)

    # Addition
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

    # Assigning a list only copies the reference.
    fourthl = thirdl
    assert fourthl is thirdl
    thirdl.append(99)
    assert fourthl[-1] == 99

    # Next level copy
    fifthl = list()
    fifthl[:] = thirdl
    # They are equal but not the same
    assert fifthl is not fourthl
    assert fifthl == fourthl
    fifthl.append(90)
    assert fourthl[-1] == 99
    assert fifthl[-1] == 90
    assert fifthl != fourthl

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

    # Assigning a dict only copies the reference.
    mydict2 = mydict1
    assert mydict2 is mydict1
    assert mydict2 == mydict1
    mydict1['b'] = 2
    assert mydict2['b'] == 2

    # Next level copy
    mydict3 = mydict1.copy()
    assert mydict3 is not mydict1
    assert mydict3 == mydict1
    mydict1['c'] = 3
    assert 'c' not in mydict3

    # Keys() returns an iterator, but can usually be treated as a list?
    # Not sure what all changes an interator into a list.
    d_keys = mydict1.keys()
    assert len(d_keys) == 3

    # Control flow
    err = 0
    if 'b' not in d_keys:
        err = 1
    elif 'c' not in d_keys:
        err = 2
    else:
        err = -1
    assert err == -1

    # range returns an interator that apparently can be used like a list?
    r_list = range(5)
    assert len(r_list) == 5
    assert r_list[-1] == 4

    loop_tot = 0
    for loop_i in range(5):
        loop_tot += loop_i
    assert loop_tot == 10

    # List comprehension: construct a list as a series of values returned
    # by an expression when run by an iterator. The # point of the
    # experssion might just be its side effects.
    listc1 = [index*index for index in range(5)]
    assert len(listc1) == 5
    assert listc1[0] == 0
    assert listc1[1] == 1
    assert listc1[2] == 4
    assert listc1[-1] == 16

    listc2 = [index*index for index in range(5) if index % 2 == 1]
    assert len(listc2) == 2
    assert listc2[0] == 1
    assert listc2[1] == 9
    assert listc2[-1] == 9

    print('Bye!')


# This code only runs when the file is executed directly.
if __name__ == '__main__':
    main()
