#!/usr/bin/python3
"""inherits_form module."""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited from a class.

    args:
        obj: the object
        a_class: the class
    Returns:
        True if the object is an instance
        of a class that inherited from a class
        False otherwise

    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
