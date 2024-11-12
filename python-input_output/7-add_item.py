#!/usr/bin/python3
"""
a script that adds all arguments to a Python list,
and then save them to a file.
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
