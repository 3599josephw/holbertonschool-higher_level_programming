#!/usr/bin/python3
"""Task 0 - Read file
"""


def read_file(filename=""):
    """Reads a file to standard output
    """
    with open(filename) as f:
        for line in f:
            print(line, end='')
