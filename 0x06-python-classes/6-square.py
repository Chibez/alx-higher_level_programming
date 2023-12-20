#!/usr/bin/python3

class Square:
    """A class that represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square instance.

        Args:
            size (int): Represents the size of the square.
            position (tuple): Represents the position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int) or value < 0:
            raise ValueError('size must be a non-negative integer')
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise ValueError('position must be a tuple of two non-negative integers')
        self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return self.size ** 2

    def my_print(self):
        """Print the square using '#' characters and respecting the position."""
        print('\n' * self.position[1] + (' ' * self.position[0] + '#' * self.size + '\n') * self.size)


# Testing the my_print method with different instances
my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

