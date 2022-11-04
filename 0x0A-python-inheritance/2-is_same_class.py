#!/usr/bin/python3

"""a module to check if an object is
   exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """ a function that returns True if the object is exactly
    an instance of the specified class ; otherwise False.
    Args:
        obj: the object
        a_class: the class
    Returns: True or False
    """
    k = type(obj) is a_class
    return k
