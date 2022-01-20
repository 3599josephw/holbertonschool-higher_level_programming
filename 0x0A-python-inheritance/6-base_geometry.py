#!/usr/bin/python3
"""Task 6 - Improve Geometry
"""


class BaseGeometry:
    """Doesn't define an area
    """
    def area(self):
        raise Exception("area() is not implemented")
