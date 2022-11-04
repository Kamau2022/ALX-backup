#!/usr/bin/python3
"""a module that writes to a file"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)
    Args:
        filename: name of the file to write to
        text: written text
   Returns: number of characters written
    """

    with open(filename, 'w', encoding='utf-8') as myfile:
        k = myfile.write(text)
        return k
