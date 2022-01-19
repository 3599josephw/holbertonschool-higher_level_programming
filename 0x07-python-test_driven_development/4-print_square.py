#!/usr/bin/python3
"""Prints out a square of # equal to the size of the integer passed in
"""


def print_square(size):
    """Prints the square out.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
            if j is size - 1:
                print("")
