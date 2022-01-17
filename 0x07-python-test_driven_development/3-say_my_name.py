#!/usr/bin/python3
"""Prints two strings passed into the function
"""


def say_my_name(first_name, last_name=""):
    """Both parameters must be strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
