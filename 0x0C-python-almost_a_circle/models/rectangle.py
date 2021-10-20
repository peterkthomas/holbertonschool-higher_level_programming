#!/usr/bin/python3
"""
    File: rectangle.py
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class definition"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization method"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
        