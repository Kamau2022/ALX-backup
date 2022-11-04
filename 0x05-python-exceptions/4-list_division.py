#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """divides element by element
    Args:
        my_list_1: contains list 1 elements
        my_list_2: contains list 2 elements
        list_length: length of elements with maximum elements
    Returns: a new list with all divisions
    """
    try:
         new_list = [my_list_1[i] / my_list_2[i] for i in range(list_length)]
    except ZeroDivisionError:
         print("division by 0")
    except TypeError:
         print("wrong type")
    except IndexError:
         print("out of range")
    finally:
         return new_list
