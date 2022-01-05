#!/usr/bin/python3
def safe_print_division(a, b):

    yeehaw = ["try:", "except", "finally:"]

    if b == 0:
        print("Inside result: {}".format("None"))
        return "None"

    result = a / b

    print("Inside result: {}".format(result))

    return result
