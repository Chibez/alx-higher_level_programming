#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Convert Roman numeral string to an integer.

    Parameters:
    - roman_string: The input Roman numeral string.

    Returns:
    The corresponding integer value.
    """
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    p = 0

    if type(roman_string) is str and roman_string:
        for c in range(len(roman_string) - 1, -1, -1):
            if val[roman_string[c]] >= p:
                res += val[roman_string[c]]
            else:
                res -= val[roman_string[c]]
            p = val[roman_string[c]]
    return res
