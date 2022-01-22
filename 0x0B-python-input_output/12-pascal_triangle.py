#!/usr/bin/python3
"""Task 12 - Pascal's Triangle"""


def pascal_triangle(n):
    biglist = []
    if n <= 0:
        return biglist
    list = [1]
    for i in range(n):
        biglist.append(list)
        newlist = []
        newlist.append(list[0])
        for i in range(len(list) - 1):
            newlist.append(list[i] + list[i + 1])
        newlist.append(list[-1])
        list = newlist
    return biglist
