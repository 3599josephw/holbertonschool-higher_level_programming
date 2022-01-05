#!/usr/bin/python3

def safe_print_division(a, b):

    exista = "a" in locals()
    existb = "b" in locals()

    if exista == "False" or existb == "False" or a == 0 or b == 0:
        print("Inside result: {}".format("None"))
        return "None"

    result = a / b

    print("Inside result: {}".format(result))

    return result
