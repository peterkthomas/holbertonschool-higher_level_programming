#!/usr/bin/python3
# 3-is_kind_of_class.py
# Carlos Barros <1543@holbertonschool.com>
"""
    File: 3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """Determing if an object is an instance of a class"""
    if isinstance(obj, a_class):
        return True
    return False
