#!/usr/bin/python3
"""Read file module."""


def read_file(filename=""):
    """
    Read file and print content to stdout.

    args:
        filename: file to be read
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()
        print(data, end="")
