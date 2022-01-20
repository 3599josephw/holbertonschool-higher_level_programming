#!/usr/bin/python3
"""Task 7 - Integer validator
"""


class BaseGeometry:
    """Doesn't define an area, validates an integer
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
