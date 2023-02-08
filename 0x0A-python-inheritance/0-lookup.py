#!/usr/bin/python3
"""Function lookup module."""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    args:
        obj: an object
    """
    return (dir(obj))
