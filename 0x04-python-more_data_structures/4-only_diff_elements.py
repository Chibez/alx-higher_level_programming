#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Find the elements that are unique to each set (symmetric difference).

    Parameters:
    - set_1: The first set.
    - set_2: The second set.

    Returns:
    A new set containing the elements that are unique to each set as needed.

    """
    return set_1 ^ set_2

