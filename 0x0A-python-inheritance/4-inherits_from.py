#!/usr/bin/python3

"""a module that checks if the object is an instance of a class
"""


def inherits_from(obj, a_class):
    """ a function that returns True if the object is
        an instance of a class that inherited (directly or indirectly)
        from the specified class ; otherwise False.
    Args:
        obj: an object
        a_class: a class
    Return:
           True or False
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    return False
