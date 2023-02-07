#!/usr/bin/python3
"""class_to_json module."""


def class_to_json(obj):
    """
    Return the dictionary description for JSON serialization of an object.

    args:
        obj: instance of a class
    """
    return (obj.__dict__)
