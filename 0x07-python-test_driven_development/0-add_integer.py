#!/usr/bin/python3
"""Makes the code executable."""


def add_integer(a, b=98):
    """Add integers.

    Raise TypeError if input is not a float or an int
    """

    if (not isisntance(a, int) or (a, float)):
        raise TypeError("a must be an integer")
    elif (not isisntance(b, int) or (b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
