#!/usr/bin/python3

"""a module that describes a class BaseGeometry
"""


class BaseGeometry:
    """a BaseGeometry class"""
    def area(self):
        """a function that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a public instance method that validates value
        Args:
            name: name which is a string
            value: value to be validated
        """
        if not (isinstance(value, (int))):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

