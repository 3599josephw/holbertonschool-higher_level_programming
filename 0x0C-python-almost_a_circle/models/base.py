#!/usr/bin/python3
"""Task 1 - Base class
"""
import json
import os


class Base:
    """The base class
    """
    __nb_object = 0

    @classmethod
    def clear(cls):
        """Sets the variable to 0 for unittesting"""
        Base.__nb_object = 0

    def __init__(self, id=None):
        """inits the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """Takes a dictionary and returns a list in json format"""
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the attributes of objects into a json file"""
        json_list = []

        if list_objs is not None:
            for i in list_objs:
                json_list.append(i.to_dictionary())

        with open(cls.__name__ + ".json", 'w') as f:
            f.write(Base.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """Converts a json string into a list"""
        if json_string is None:
            return []
        if len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an object based on a given dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads from file"""
        if not os.path.exists(cls.__name__ + ".json"):
            return []

        with open(cls.__name__ + ".json", 'r') as f:
            tmp = Base.from_json_string(f.read())

        newlist = []

        for item in tmp:
            newlist.append(cls.create(**item))

        return newlist
