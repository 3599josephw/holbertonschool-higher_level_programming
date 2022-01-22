#!/bin/usr/python3
"""Task 6 - Create object from a JSON file
"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”
    """
    with open(filename) as f:
        return json.loads(f.read())
