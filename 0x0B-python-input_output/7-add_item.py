#!/usr/bin/python3
"""
This module adds all arguments to a Python list and then
saves them to a file.
"""
import sys
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

try:
    my_list = load("add_item.json")
except(TypeError, FileNotFoundError):
    my_list = []

for x in sys.argv[1:]:
    my_list.append(x)

save(my_list, "add_item.json")