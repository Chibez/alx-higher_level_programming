#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Delete a key from the dictionary, if it exists.

    Parameters key and input:
    - a_dictionary: The input dictionary.
    - key: The key to delete (default is an empty string).

    Returns Dictionary:
    The modified dictionary.
    """
    a_dictionary.pop(key, None)
    return a_dictionary
