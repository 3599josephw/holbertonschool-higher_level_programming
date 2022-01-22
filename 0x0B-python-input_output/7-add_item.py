#!/usr/bin/python3
"""Task 7 - Load, add, save
"""
from os.path import exists
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    my_list = load_from_json_file('add_item.json')
except(TypeError, FileNotFoundError):
    my_list = []

for item in range(1, len(sys.argv)):
    my_list.append(sys.argv[item])

save_to_json_file(my_list, 'add_item.json')
