#!/usr/bin/python3
"""Is_same_class module."""


def is_same_class(obj, a_class):
    """
    Check of an object is an instance of a class.

    args:
        obj: the object
        a_class: the class
    Returns:
        True if the object is an instance of a class,
        False otherwise

    """
    return (type(obj) is a_class)
