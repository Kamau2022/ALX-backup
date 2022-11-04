#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """a function that prints integers only
    Args:
        mylist: a list of elements
        x: number of elements to be printed
    Return:
           number of elements printed
    """

    p = 0
    a = my_list
    for i in a:
        if i.isdigit():
            try:
                print("{:d}".format(a[i]), end='')
                p = p + 1
            except TypeError:
                break
            except NameError:
                break
    print()
    return p
        
