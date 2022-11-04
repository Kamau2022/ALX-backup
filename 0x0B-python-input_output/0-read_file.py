#!/usr/bin/python3
"""a module that reads a text file"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename: name of the file to be read
    """

    with open(filename, 'r', encoding='utf-8') as myfile:
        for line in myfile:
            print(line, end='')
