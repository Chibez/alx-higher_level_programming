#!/usr/bin/python3

"""Defines a square class"""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """Initializes a new square.

        Args:
            size (int): The size of the square.

        Returns:
            None
        """
        # Using double underscores to make __size a private attribute
        self.__size = size
