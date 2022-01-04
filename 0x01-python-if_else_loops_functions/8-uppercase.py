#!/usr/bin/python3
def uppercase(str):
        new_str = ''
        for i in range(len(str)):
                if (str[i] >= 'a' and str[i] <= 'z'):
                        new_str = new_str + chr(ord(str[i]) - 32)
                else: new_str = new_str + str[i]
        print("{}".format(new_str))
