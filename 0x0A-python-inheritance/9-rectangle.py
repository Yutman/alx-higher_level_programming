#!/usr/bin/python3
"""class Rectangle module."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines a rectangle."""

    def __init__(self, width, height):
        """
        Construct a rectangle instance.

        args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of a rectangle instance."""
        return (self.__width * self.__height)

    def __str__(self):
        """Return string description of a rectangle instance."""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
