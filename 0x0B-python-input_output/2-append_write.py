#!/usr/bin/python3
"""a module that appends to a file"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file
    Args:
        filename: name of the file to append to
        text: appended text
   Returns: number of characters added
    """

    with open(filename, 'a', encoding='utf-8') as myfile:
        k = myfile.write(text)
        return k
