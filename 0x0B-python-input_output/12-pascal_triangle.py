#!/usr/bin/python3
"""
    File: 12-pascal_triangle.py
"""


def pascal_triangle(n):
    """pascal_triangle"""
    if n <= 0:
        return ""

    tri = [[1]]
    for current in range(1, n):
        row = [1]
        prev = tri[current - 1]
        for item in range(1, current):
            row.append(prev[item] + prev[item - 1])
        row.append(1)
        tri.append(row)
    return (tri)
