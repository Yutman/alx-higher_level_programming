#!/usr/bin/python3
"""load_from_json_file module."""


import json


def load_from_json_file(filename):
    """
    Create an object from JSON file.

    args:
        filename: the JSON file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.loads(f.read()))
