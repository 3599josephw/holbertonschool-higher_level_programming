#!/usr/bin/python3
"""Task 2 - Append to a file
"""


def append_write(filename="", text=""):
    """Appends text to a file
    """
    with open(filename, 'a') as f:
        return f.write(text)
