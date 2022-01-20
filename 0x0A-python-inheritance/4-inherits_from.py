#!/usr/bin/python3
"""Task 4 - only sub class of
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class
    """
    return True if isinstance(obj, a_class)  and type(obj) != a_class else False
