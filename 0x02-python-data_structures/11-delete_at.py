#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    if not my_list:
        return None

    my_list.remove(idx + 1)

    return my_list
