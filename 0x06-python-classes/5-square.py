#!/usr/bin/python3
"""Prints a square."""


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

    def my_print(self):
        """Print square object with character '#' to standard output."""

        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print("")

