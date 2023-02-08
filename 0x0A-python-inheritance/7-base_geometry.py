#!/usr/bin/python3
"""BaseGeometry module."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise an Exception."""
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """Validate value."""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
