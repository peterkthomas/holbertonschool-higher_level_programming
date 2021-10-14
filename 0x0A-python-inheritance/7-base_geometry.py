#!/usr/bin/python3
"""
    File: 7-base_geometry.py
"""


class BaseGeometry(object):
    """Class definition for base geometry"""
    def area(self):
        """area method returns the area of the object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value passed"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
