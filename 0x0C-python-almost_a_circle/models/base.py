#!/usr/bin/python3
"""Task 1 - Base class
"""
import json
import os


class Base:
    """The base class
    """
    __nb_object = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    # Takes a dictionary and returns a list in json format
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    # Saves the attributes of objects into a json file
    @classmethod
    def save_to_file(cls, list_objs):
        json_list = []

        if list_objs is not None:
            for i in list_objs:
                json_list.append(i.to_dictionary())

        with open(cls.__name__ + ".json", 'w') as f:
            f.write(Base.to_json_string(json_list))

    # Converts a json string into a list
    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string)

    # Creates an object based on a given dictionary
    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):

        if not os.path.exists(cls.__name__ + ".json"):
            return []

        with open(cls.__name__ + ".json", 'r') as f:
            tmp = Base.from_json_string(f.read())

        newlist = []

        for item in tmp:
            newlist.append(cls.create(**item))

        return newlist
