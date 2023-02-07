#!/usr/bin/python3
"""write_file module."""


def write_file(filename="", text=""):
    """
    Write to a file.

    args:
        filename: the file
        text: the text to be written
    Returns:
        no. of characters written

    """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
