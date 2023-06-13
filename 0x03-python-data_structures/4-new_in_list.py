#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """
    A function that replaces an element in a list at 
    a specific position without modifying the original list
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    new_list = [x for x in my_list]
    new_list[idx] = element
    return new_list
