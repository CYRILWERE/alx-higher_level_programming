#!/usr/bin/python3
"""
Module for uniq_add function.
"""


def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).

    Parameters:
    - my_list (list): The input list.

    Returns:
    - The sum of all unique integers.
    """

    unique_set = set(my_list)
    sum_unique = sum(unique_set)

    return sum_unique


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))

