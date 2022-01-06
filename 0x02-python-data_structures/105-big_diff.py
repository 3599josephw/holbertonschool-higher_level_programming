#!/usr/bin/python3
def big_diff(my_list=[]):

    if len(my_list) <= 1:
        return 0

    largest = my_list[0]
    smallest = my_list[0]

    for i in my_list:
        if i > largest:
            largest = i
        elif i < smallest:
            smallest = i

    diff = largest - smallest

    return diff
