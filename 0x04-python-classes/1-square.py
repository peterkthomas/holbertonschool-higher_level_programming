#!/usr/bin/python3
# 1-square.py
""" Module for Square with docstring at top """


class Square:
    """ Makes a size """
    def __init__(self, size):
        self.__size = size

        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) is not int:
            raise TypeError("size must be an integer")
