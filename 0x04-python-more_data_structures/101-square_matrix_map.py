#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda i: i ** 2, row)), matrix))
 """
    Compute the square value of all integers in a matrix using map.

    Parameters:
    - matrix: The input matrix.

    Returns:
    A new matrix where each element is the square of the corresponding element in the input matrix.
    """
