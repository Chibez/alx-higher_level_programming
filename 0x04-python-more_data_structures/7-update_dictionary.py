#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replace or add key/value in a dictionary.

    Parameters:
    - a_dictionary: The input dictionary.
    - key: The key to update or add.
    - value: The value to assign to the key.

    Returns:
    The modified dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
