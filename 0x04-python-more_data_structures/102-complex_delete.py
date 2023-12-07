#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    Delete key-value pairs from a dictionary where the value matches the specified value.

    Parameters:
    - a_dictionary: The input dictionary.
    - value: The value to be deleted.

    Returns:
    A new dictionary with key-value pairs excluding the ones with the specified value.
    """
    return {k: v for k, v in a_dictionary.items() if v != value}

