#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Calculate the weighted average of a list of tuples.

    Parameters:
    - my_list: The input list of tuples, where each tuple contains
               two values: the weight and the value.

    Returns:
    The weighted average or 0 if the list is empty.
    """
    if my_list:
        return sum(a * b for a, b in my_list) / sum(b for a, b in my_list)
    return 0
