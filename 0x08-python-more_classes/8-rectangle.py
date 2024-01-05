#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """This class represents a rectangle"""

    number_of_instances = 0  # Class variable to keep track of the number of instances
    print_symbol = "#"  # Class variable to represent the symbol used when printing

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle class.

        Args:
            width (int): Represents the width of the rectangle.
            height (int): Represents the height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than zero.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment the count of instances

    @property
    def width(self):
        """Retrieves the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        """Returns a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if column < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when the object is deleted and decrements instance count"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
