#!/usr/bin/python3
"""
    Divide a matrix: Divides all elements of a matrix
    Prototype: def matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    Returns the division of a and b as a float.
    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    return ([[round(item / div, 2) for item in row] for row in matrix])
