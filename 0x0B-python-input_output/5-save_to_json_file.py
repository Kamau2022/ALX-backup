#!/usr/bin/python3
"""a module to demonstrate json module"""

import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object
       to a text file, using a JSON representation:
    Args:
        my_obj: object file
        filename: text file
   """
    with open(filename, 'w', encoding='utf-8') as myfile:
        json.dump(my_obj, myfile)
