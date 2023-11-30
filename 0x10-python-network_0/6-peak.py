#!/usr/bin/python3
""" A function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    size = len(list_of_integers)
    i = size
    j = size // 2

    if size == 0:
        return None

    while True:
        i = i // 2
        if (j < size - 1 and
                list_of_integers[j] < list_of_integers[j + 1]):
            if i // 2 == 0:
                i = 2
            j = j + i // 2
        elif i > 0 and list_of_integers[j] < list_of_integers[j - 1]:
            if i // 2 == 0:
                i = 2
            j = j - i // 2
        else:
            return list_of_integers[j]
