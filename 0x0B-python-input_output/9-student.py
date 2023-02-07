#!/usr/bin/python3
"""Student class module."""

class Student:
    """A class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Contruct an instance of the class Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve dictionary representation of a Student instance."""
        return (self.__dict__)
