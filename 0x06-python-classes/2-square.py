#!/usr/bin/python3

"""A module that defines a Square class."""


class Square:
    """A class that represents a square."""

    def __init__(self, size=0):
        """Initialize the Square instance.

        Args:
            size (int): Represents the size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """

        # Check if size is an integer and greater than or equal to zero
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        # Assign the size to the private attribute __size
        self.__size = size
