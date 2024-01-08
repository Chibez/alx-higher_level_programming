#!/usr/bin/python3
"""
This module defines a function for element-wise matrix division.

Function:
    matrix_divided(matrix, div)

Description:
    Divides all elements of a matrix by a given number.

Parameters:
    matrix (list of lists): Matrix with elements of type int or float.
    div (int or float): Number to be used for the division.

Raises:
    TypeError: If the matrix is not a list of lists containing integers or floats,
               or if rows have different sizes.
    TypeError: If div is not an int or float.
    ZeroDivisionError: If div is 0.

Returns:
    list of lists: A new matrix representing the result of the divisions.
"""
def matrix_divided(matrix, div):
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for row in matrix for element in row)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(element / div, 2) for element in row]
        for row in matrix
    ]
