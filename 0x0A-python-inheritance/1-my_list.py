#!/usr/bin/python3
"""Task 1 - My List
"""


class MyList(list):
    """Prints the sorted list
    """
    def print_sorted(self):
        print(sorted(self))
