#!/usr/bin/python3
"""
    File: rectangle.py
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class definition"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization method"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """__str__ method"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """Height getter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height


    def display(self):
        """prints the rectangle with the # character"""
        for _ in range(self.y):
            print("")

        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """update rectangle"""
        if args and args != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        super().__init__(self.width,
                                         self.height, self.x,
                                         self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
                count += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        super().__init__(self.width, self.height,
                                         self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """dictionary representation of self"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}