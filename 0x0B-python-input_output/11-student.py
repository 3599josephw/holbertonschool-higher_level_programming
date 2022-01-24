#!/usr/bin/python3
"""Task 11 - Student to disk and reload
"""


class Student:
    """Creates a Student that can load attributes from a json file
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

    def reload_from_json(self, json):
        self.__dict__.update(json)
