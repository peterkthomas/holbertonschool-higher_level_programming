#!/usr/bin/python3
"""
    File: 2-is_same_class.py
"""


def is_same_class(obj, a_class):
    """Check if an object is an type of class"""
    if type(obj) == a_class:
        return True
    return False
