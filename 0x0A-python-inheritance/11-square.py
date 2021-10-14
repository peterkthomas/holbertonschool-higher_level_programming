#!/usr/bin/python3
"""
    File: 10-square.py
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square inherits from Rectangle"""
    def __init__(self, size):
        """Makes a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Prints a string of the square"""
        return f"[Square] {self.__size}/{self.__size}"
