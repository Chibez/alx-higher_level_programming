#!/usr/bin/python3
"""Inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle using the BaseGeometry class."""

    def __init__(self, width, height):
        """Initialize a new Rectangle."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

