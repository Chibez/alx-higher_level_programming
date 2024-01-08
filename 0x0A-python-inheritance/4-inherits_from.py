#!/usr/bin/python3
"""
    This module defines a function 'inherits_from' that checks if an object
    is an instance of a class that inherited (directly or indirectly) from
    the specified class.
"""


def inherits_from(obj, a_class):
    """Return True if 'obj' is an instance of a class inherited
    from 'a_class'; otherwise, return False.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
