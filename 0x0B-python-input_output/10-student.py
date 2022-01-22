#!/usr/bin/python3
"""Task 10 - Student to JSON with filter
"""


class Student:
    """Creates a Student with JSON filter
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dict = vars(self)
        if type(attrs) != list:
            return dict
        for item in attrs:
            if type(item) != str:
                return dict

        new_dict = {}
        for key, value in dict.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict
