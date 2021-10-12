#!/usr/bin/python3
"""
    File name : 0-add_integer.py
    Integer addition: This function adds 2 integers
    Prototype: def add_integer(a, b=98)
    Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """
    Return the addition of a and b.
    Floats are coverted to ints before addition.
    Raises:
    TypeError: If either of a or b is a non-int/float.
    """
    if (a is None or not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
