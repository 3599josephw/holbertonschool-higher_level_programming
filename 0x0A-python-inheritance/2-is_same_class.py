#!/usr/bin/python3
"""Task 2 - Exact same object
"""


def is_same_class(obj, a_class):
    """Returns true if the object is exactly an instance of the class
    """
    return True if type(obj) == a_class else False
