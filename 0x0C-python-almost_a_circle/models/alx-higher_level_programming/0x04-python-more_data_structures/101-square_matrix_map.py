#!/usr/bin/python3
"""
Module for square_matrix_map function.
"""


def square_matrix_map(matrix=[]):
    """
    Computes the square value of all integers of a matrix using map.

    Parameters:
    - matrix (list of lists): The 2-dimensional input matrix.

    Returns:
    - A new matrix with values squared.
    """

    return list(map(lambda row: list(map(lambda x: x**2, row)), matrix))


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_map(matrix)
    print(new_matrix)
    print(matrix)

