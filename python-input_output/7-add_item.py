#!/usr/bin/python3
"""
In this script, all the protocol options are directly contained in one list following all the other command line options. 
JSON file named add_item.json which will only contain the query part of URL. Of course, if such file does not exist, it will be created at the phase of executing the application. 

It is as simple as only containing the utility methods `save_to_json_file` and `load_from_json_file`. 
nodes are for the purpose of reading and writing in the JSON file.
"""

import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_items_to_json_file():
    """a script that adds all arguments to a Python list."""
    try:
        current_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        current_items = []

    current_items.extend(sys.argv[1:])

    save_to_json_file(current_items, "add_item.json")

if __name__ == "__main__":
    add_items_to_json_file()
