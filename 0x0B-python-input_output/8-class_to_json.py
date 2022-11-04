#!/usr/bin/python3
"""a module that that describes a json module"""


def class_to_json(obj):
    """a function that returns the dictionary
       description with simple data structure
       (list, dictionary, string, integer and boolean)
       for JSON serialization of an object
    Args:
        obj: an instance of a Class
    """
    if isinstance(obj, type('__class__')):
        return obj
    return obj.__dict__
