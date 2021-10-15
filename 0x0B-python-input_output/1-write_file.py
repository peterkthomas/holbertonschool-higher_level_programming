#!/usr/bin/python3
"""
    File: 1-write_file.py
"""


def write_file(filename="", text=""):
    """writes a string to a utf-8 text file"""
    with open(filename, 'w', encoding='utf-8') as fd:
        return fd.write(text)
