#!/usr/bin/python3

"""a module on inheritance"""


def lookup(obj):
    """a function that returns the list of available
    attributes and methods of an object
    """
    list = dir(obj)
    return list
