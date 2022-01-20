#!/usr/bin/python3
"""Task 8 - Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """Subclass of BaseGeometry that initializes a rectangle
    """
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height