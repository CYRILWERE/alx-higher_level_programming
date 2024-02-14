#!/usr/bin/python3
"""
Module for search_replace function.
"""


def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.

    Parameters:
    - my_list (list): The initial list.
    - search: The element to replace in the list.
    - replace: The new element.

    Returns:
    - New list with replaced elements.
    """

    new_list = [replace if x == search else x for x in my_list]

    return new_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    print(new_list)
    print(my_list)

