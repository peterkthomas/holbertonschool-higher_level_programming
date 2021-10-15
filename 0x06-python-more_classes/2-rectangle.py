#!/usr/bin/python3
"""
    File: 1-rectangle.py
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

    def area(self):
        """return area"""
        return self.__width * self.__height

    def perimeter(self):
        """return perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """return string reprsentation"""
        if self.__height != 0 and self.__width != 0:
            return ("\n".join("#"*self.__width for i in range(self.__height)))
        else:
            return ""
