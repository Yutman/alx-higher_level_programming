#!/usr/bin/python3
"""form_json_string module."""

import json


def from_json_string(my_str):
    """
    Return an object repsented by a JSON string.

    args:
        my_str: the JSON string
    """
    return (json.loads(my_str))


