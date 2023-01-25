#!/usr/bin/python3
"""Sets and gets a private attribute size."""


class Square:
    """A class that defines a square object."""

    def __init__(self, size=0):
        """
        Construct the size attribute for the square object.

        args:
            size (int): size of the square object
        """
        self.__size = size

    @property
    def size(self):
        """
        Return size of a square object.

        Returns:
            size of a square object


        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size attribute of a square object to a value.

        args:
            value (int): size attribute of the square object
        """
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Return the area of a square object.

        Returns:
            The area of a square object

        """
        return (self.__size**2)

