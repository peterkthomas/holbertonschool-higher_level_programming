#!/usr/bin/python3
"""
    File: 9-rectangle.py
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from class 'BaseGeometry'
    """

    def __init__(self, width, height):
        """
        validates width and height are ints"
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Returns the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Prints out a string with area
        """
        return "f[Rectangle] {self.__width__}/{self.__height__}"
