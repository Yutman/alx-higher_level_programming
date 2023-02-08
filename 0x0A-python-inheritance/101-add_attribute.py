#!/usr/bin/python3
"""add_attribute module."""


def add_attribute(inst, name, value):
    """Add attribute to an object."""
    if not hasattr(inst, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(inst, name, value)
