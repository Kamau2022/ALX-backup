#!/usr/bin/python3

"""This module demonstrates working of json module"""
import json


def from_json_string(my_str):
    """ a function that returns an object
       (Python data structure) represented by a JSON string:
    """
    k = json.loads(my_str)
    return k
