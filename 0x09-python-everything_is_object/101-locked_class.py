#!/usr/bin/python3
"""defines a locked class"""


class LockedClass:
    """
    Allows only instatiation of an attribute called first_name
    """

    __slots__ = ["first_name"]
