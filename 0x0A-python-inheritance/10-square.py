#!/usr/bin/python3
"""Task 10 - Square #1
"""


Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    """Creates a Square with area()
    """
    def __init__(self, size):
        Square.integer_validator(self, "size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
