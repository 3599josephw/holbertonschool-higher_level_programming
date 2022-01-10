#!/usr/bin/python3
def roman_to_int(roman_string):

    my_dict = {'I': 1, 'V': 5, 'X': 10, 'IX': 9, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'D': 500, 'CM': 900, 'M': 1000}

    result = 0

    if roman_string in my_dict:
        result = my_dict[roman_string]
        return result

    for i in roman_string:
        result += my_dict[i]

    return result
