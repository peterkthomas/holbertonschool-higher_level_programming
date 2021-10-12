#!/usr/bin/python3
"""
    Print square: function that prints a square with the character #
    Prototype: def print_square(size)
"""


def print_square(size):
    """
    function that prints a square with the character #
    size: numbers the character # to print
    Raises:
        TypeError: size must be an integer
        TypeError: size must be >= 0
    """

    if (not isinstance(size, int) or isinstance(size, float) and size < 0):
            raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        else:
            print("")
