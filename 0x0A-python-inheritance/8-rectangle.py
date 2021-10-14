#!/usr/bin/python3
"""
    File: 8-rectangle.py
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
