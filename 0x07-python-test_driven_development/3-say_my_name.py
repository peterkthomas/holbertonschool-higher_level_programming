#!/usr/bin/python3
"""
    Say my name: prints My name is <first name> <last name>
    Prototype: def say_my_name(first_name, last_name="")
    You are not allowed to import any modules
"""


def say_my_name(first_name, last_name=""):
    """
    Returns a string with the full name
    first_name and last_name must be strings
    Raises:
        TypeError: first_name must be a string
        TypeError: first_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
