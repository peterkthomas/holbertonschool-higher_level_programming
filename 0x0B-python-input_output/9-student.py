#!/usr/bin/python3
"""
    File: 9-student.py
"""


class Student(object):
    """Student"""
    def __init__(self, first_name, last_name, age):
        """__init__"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation """
        return self.__dict__
