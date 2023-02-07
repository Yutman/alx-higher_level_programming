#!/usr/bin/python3
"""append_write module."""


def append_write(filename="", text=""):
    """
    Append text to a file.

    args:
        filename: the file
        text: the text to append
    Returns:
        no. of chaacters appended

    """
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
