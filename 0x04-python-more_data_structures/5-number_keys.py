#!/usr/bin/python3
"""
Module for number_keys function.
"""


def number_keys(a_dictionary):
    """
    Returns the number of keys in a dictionary.

    Parameters:
    - a_dictionary (dict): The input dictionary.

    Returns:
    - The number of keys in the dictionary.
    """

    num_keys = len(a_dictionary.keys())

    return num_keys


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))

