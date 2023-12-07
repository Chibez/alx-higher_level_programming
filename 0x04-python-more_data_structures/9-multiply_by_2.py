#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Multiply each value in the dictionary by 2.

    Parameters:
    - a_dictionary: The input dictionary.

    Returns:
    A new dictionary with values multiplied by 2.
    """
    return {k: v * 2 for k, v in a_dictionary.items()}
