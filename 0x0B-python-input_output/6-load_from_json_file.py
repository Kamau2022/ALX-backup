#!/usr/bin/python3
"""a module that demonstrates working of a json module"""

import json


def load_from_json_file(filename):
    """ a function that creates an Object from a “JSON file”
    Args:
        filename: a json file
    """
    with open(filename, 'r') as myfile:
        k = json.load(myfile)
        return k
