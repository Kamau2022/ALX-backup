#!/usr/bin/python3
"""a class student module"""


class Student:
    """a class Student that defines a student by:
       first_name, last_name and age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """a function that retrieves a
           dictionary representation of a Student instance
        Args:
            attrs: attributes
        """
        if (isinstance(attrs, list)):
            return attrs
        else:
            return self.__dict__
