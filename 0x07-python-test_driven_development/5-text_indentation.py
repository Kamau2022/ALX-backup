#!/usr/bin/python3
"""a module that prints a text
"""

def text_indentation(text):
    """a function that prints a text with 2 new lines 
       after each of these characters: ., ? and :
    """
   
    x = text.replace('?', '\n')
    print (x)
