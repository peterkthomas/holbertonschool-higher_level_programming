#!/usr/bin/python3
"""
    File: 1-my_list.py
"""


class MyList(list):
    """Does orted printing"""

    def print_sorted(self):
        """Printis out a sorted list in aascending order"""
        print(sorted(self))
