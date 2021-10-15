#!/usr/bin/python3
"""
    File: 0-rectangle.py
"""


class Rectangle(object):
    """rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialize rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for  width."""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter forheight."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
