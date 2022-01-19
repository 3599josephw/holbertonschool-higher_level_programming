#!/usr/bin/python3
"""Adds in a newline character after every '.' '?' and ':'
"""


def text_indentation(text):
    """Takes a string and adds newlines in
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    sep = [".", "?", ":"]
    new_str = ""

    for i in range(len(text)):
        if text[i] in sep:
            new_str = new_str + text[i]
            new_str = new_str + "\n\n"
        else:
            if (text[i - 1] in sep and text[i] == " ") or (text[i - 1] == " " and text[i] == " "):
                pass
            else:
                new_str = new_str + text[i]

    print(new_str, end="")
