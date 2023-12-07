#!/usr/bin/python3
def square_matrix_simple(matrix=None):

    if matrix is None:
        matrix = []

    result_matrix = [[y ** 2 for y in x] for x in matrix]

    return (result_matrix)
