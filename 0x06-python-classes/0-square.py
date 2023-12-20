#!/usr/bin/python3

# Import the Square class from the 0-square module
Square = __import__('0-square').Square

# Create an instance of the Square class
my_square = Square()

# Print the type of my_square (should be <class '0-square.Square'>)
print(type(my_square))

# Print the dictionary representation of my_square
print(my_square.__dict__)
