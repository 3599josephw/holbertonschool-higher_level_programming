#!/usr/bin/python3
"""Task 5 - Save object to file
"""
import json


def save_to_json_file(my_obj, filename):
    """Save JSON representation to a file
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
