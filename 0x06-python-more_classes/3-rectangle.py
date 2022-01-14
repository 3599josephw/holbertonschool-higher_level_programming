#!/usr/bin/python3
"""Creating a rectangle with private properties - repr and eval"""


class Rectangle:
    """The class for a rectangle with private properties"""
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise TypeError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise TypeError("height must be >= 0")

        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        return ("#"*self.__width+"\n")*(self.__height-1)+("#"*self.__width)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
