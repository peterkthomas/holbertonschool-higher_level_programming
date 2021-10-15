#!/usr/bin/python3
"""
    File: 2-append_write.py
"""


def append_write(filename="", text=""):
    """writes a string to a utf-8 text file, appended"""
    with open(filename, 'a', encoding='utf-8') as fd:
        return fd.write(text)
