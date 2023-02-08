#!/usr/bin/python3
"""MyList module."""


class MyList(list):
    """class MyList."""

    def print_sorted(self):
        """Print a sorted list."""
        print(sorted(self))
