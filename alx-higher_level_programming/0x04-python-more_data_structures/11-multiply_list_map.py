#!/usr/bin/python3
"""
Module for multiply_list_map function.
"""


def multiply_list_map(my_list=[], number=0):
    """
    Returns a new list with all values multiplied by a number using map.

    Parameters:
    - my_list (list): The input list.
    - number: The number to multiply each value in the list.

    Returns:
    - A new list with values multiplied by the specified number.
    """

    return list(map(lambda x: x * number, my_list))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 6]
    new_list = multiply_list_map(my_list, 4)
    print(new_list)
    print(my_list)

