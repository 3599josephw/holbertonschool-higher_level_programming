#!/usr/bin/python3
"""Task 1 - Write to a file
"""


def write_file(filename="", text=""):
    """Writes the given text to a file
    """
    with open(filename, 'w') as f:
        return f.write(text)
