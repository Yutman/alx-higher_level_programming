#!/usr/bin/python3
"""save_to_json_file module."""


import json


def save_to_json_file(my_obj, filename):
    """
    Write a JSON representation of an object to a text file.

    args:
        my_obj: the object
        filename: the file to write on
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
