#!/usr/bin/python3
"""A class Rectangle module."""


class Rectangle:
    """A class that defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Create a new instance of a rectangle class.

        args:
            width (int): width of the rectangle instance
            height (int): height of the rectangle instance
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrive a private instance of a width attribute."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Set a private instance of a width attribute.

        args:
            value (int): value to set the width to.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrive a private instance of a height attribute."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Set a private instance of a height attribute.

        args:
            value (int): value to set the height to.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of a rectangle instance."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of a rectangle instance."""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height + self.__width) * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two instances of class Rectangle.

        args:
            rect_1 (instance): first rectangle
            rect_2 (instance): second rectangle
        Return:
            The bigger of the two rectangles

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() > rect_2.area():
            return (rect_1)
        elif rect_1.area() < rect_2.area():
            return (rect_2)
        elif rect_1.area() == rect_2.area():
            return (rect_1)

    @classmethod
    def square(cls, size=0):
        """
        Return a new instance of class rectangle.

        args:
            size (int): width and height attributes
        """
        return (cls(size, size))

    def __str__(self):
        """Return printable representation of a rectangle instance."""
        if self.__height == 0 or self.__width == 0:
            return ("")
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                print(str(self.print_symbol), end="")
            if i != self.__height - 1:
                print("")
        return ("")

    def __repr__(self):
        """Return a string representation of a rectangle instance."""
        return ('Rectangle({}, {})'.format(self.__width, self.__height))

    def __del__(self):
        """Print a message when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

