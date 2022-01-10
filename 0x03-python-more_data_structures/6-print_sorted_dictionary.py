#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    sort_dict = dict(sorted(a_dictionary.items()))
    for i in sort_dict:
        print("{}: {}".format(i, sort_dict[i]))
