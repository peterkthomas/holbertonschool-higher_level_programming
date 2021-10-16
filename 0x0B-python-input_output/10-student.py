#!/usr/bin/python3
"""
    File: 10-student.py
"""


class Student(object):
    """Student"""
    def __init__(self, first_name, last_name, age):
        """__init__"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation """
        if attrs is None:
            return self.__dict__
        diction = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                diction[key] = value
        return diction
