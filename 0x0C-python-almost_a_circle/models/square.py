#!/usr/bin/python3
"""
    File: Square.py
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ method"""
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                                                 self.width)
