#!/usr/bin/python3
def no_c(my_string):

    new_str = ''

    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            pass
        else:
            new_str = new_str + my_string[i]

    return new_str
