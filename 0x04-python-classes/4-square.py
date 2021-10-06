#!/usr/bin/python3
# 4-square.py
""" Module for Square with docstring at top """


class Square:
    """ Makes a size """
    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    """Area function"""
    def area(self, size=0):
        calc_area = self.__size ** 2
        return calc_area

    """ getter """
    @property
    def size(self):
        """ Returns size property """
        return self.__size

    """ setter """
    @size.setter
    def size(self, value):
        """ Sets size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ prints a # to draw the square """
    def my_print(self):
        if self.__size is 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
