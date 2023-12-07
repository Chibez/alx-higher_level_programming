#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    Multiply each element in the list by the specified number using map.

    Parameters:
    - my_list: The input list.
    - number: The multiplier.

    Returns:
    A list with each element multiplied by the specified number.
    """
    return list(map(lambda i: i * number, my_list))
