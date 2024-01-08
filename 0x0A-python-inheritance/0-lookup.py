#!/usr/bin/python3
"""
    This module defines a function 'lookup' that returns the list of
    available attributes and methods of an object using the 'dir()' function.
"""
def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return dir(obj)

