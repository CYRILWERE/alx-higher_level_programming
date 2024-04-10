#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file.
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    # Load existing data from the file
    my_list = load_from_json_file(filename)
except (FileNotFoundError, ValueError):
    # Create an empty list if the file doesn't exist or is not valid JSON
    my_list = []

# Add new arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)

