#!/usr/bin/python3
"""
Module for update_dictionary function.
"""


def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    Parameters:
    - a_dictionary (dict): The input dictionary.
    - key (str): The key to be replaced or added.
    - value: The value to be associated with the key.

    Returns:
    - The updated dictionary.
    """

    a_dictionary[key] = value

    return a_dictionary


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)

    print("--")
    print("--")

    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)

