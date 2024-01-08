#!/usr/bin/python3
"""
This module defines a function for adding two integers or floats.

Function:
    add_integer(a, b=98)
    
Description:
    Returns the sum of two numbers as integers. The second argument (b) has a default value of 98.
    
Parameters:
    a: The first number (integer or float).
    b: The second number (integer or float), default value is 98.

Returns:
    The sum of the two numbers as an integer.

Raises:
    TypeError: If either of the arguments is not an integer or a float.
"""
def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")
    
    return int(a) + int(b)
