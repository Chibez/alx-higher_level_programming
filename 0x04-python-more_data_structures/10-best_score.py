#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Find the key with the maximum value in the dictionary.

    Parameters:
    - a_dictionary: The input dictionary.

    Returns:
    The key with the maximum value or None if the dictionary is empty.
    """
    return max(a_dictionary, key=a_dictionary.get) if a_dictionary else None
