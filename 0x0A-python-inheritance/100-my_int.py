#!/usr/bin/python3
"""MyInt module."""


class MyInt(int):
    """A class that inherits from int class."""

    def __eq__(self, n):
        """Equality is opposite."""
        return not super().__eq__(n)

    def __ne__(self, n):
        """Inequality is opposite."""
        return not super().__ne__(n)
