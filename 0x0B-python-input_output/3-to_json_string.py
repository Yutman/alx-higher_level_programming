#!/usr/bin/python3
"""to_jason_string module."""


import json


def to_json_string(my_obj):
    """
    Return JSON representation of an object.

    args:
        my_obj: the object
    """
    return (json.dumps(my_obj))
