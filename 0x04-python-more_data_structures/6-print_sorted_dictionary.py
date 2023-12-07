#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Print the keys and value of a dictionary in sorted order.

    Parameters:
    - a_dictionary: The input dictionary.
    """
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
