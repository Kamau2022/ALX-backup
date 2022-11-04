#!/usr/bin/python3

"""This module demonstrates working of json module"""
import json


def to_json_string(my_obj):
    """ a function that returns an object (Python data structure)
    represented by a JSON string
    """
    k = json.dumps(my_obj)
    return k
