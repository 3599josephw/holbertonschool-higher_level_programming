#!/usr/bin/python3
"""Adding two integers. Typecasts floats as integers.
Raises TypeError if either parameter is not an int or a float.
"""


def add_integer(a, b=98):
    """Adds 'a' + 'b'
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
