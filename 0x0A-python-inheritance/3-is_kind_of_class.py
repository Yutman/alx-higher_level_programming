#!/usr/bin/python3
"""Is_kind_of_class module."""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of a class.

    args:
        obj: the object
        a_class: the class
    Returns:
        True if the object is an instance of a class,
        False otherwise

    """
    return (isinstance(obj, a_class))
