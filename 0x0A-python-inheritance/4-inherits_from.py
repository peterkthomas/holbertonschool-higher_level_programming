#!/usr/bin/python3
"""
    File: 4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """
        Returns True if the object is an instance of a class
        that inherited from the specified class
    """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
