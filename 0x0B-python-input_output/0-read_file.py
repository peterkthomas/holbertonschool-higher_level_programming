#!/usr/bin/python3
"""
    File: 0-read_file.py
"""


def read_file(filename=""):
    """reads a text file and prints to sdtout"""
    with open(filename, 'r', encoding='utf-8') as fd:
        print(fd.read(), end="")
