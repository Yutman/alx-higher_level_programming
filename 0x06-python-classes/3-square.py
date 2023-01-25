#!/usr/bin/python3
"""Validates the value of the size attribute of the square object."""


class Square:
    """A class that defines a square object."""

    def __init__(self, size=0):
        """
        Validate the size attribute for the square object.

        args:
            size (int): size of the square object
        """
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Return the area of a square object.

        Returns:
            The area of a square object

        """
        return (self.__size**2)

