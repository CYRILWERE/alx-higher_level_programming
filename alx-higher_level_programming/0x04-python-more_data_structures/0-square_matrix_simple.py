#!/usr/bin/python3
"""
Module for square_matrix_simple function.
"""


def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    Parameters:
    - matrix (list of lists): 2 dimensional array.

    Returns:
    - New matrix (list of lists): Same size as matrix, each value is the square
    of the value of the input. The initial matrix should not be modified.
    """

    new_matrix = []

    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(value ** 2)
        new_matrix.append(new_row)

    return new_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)

