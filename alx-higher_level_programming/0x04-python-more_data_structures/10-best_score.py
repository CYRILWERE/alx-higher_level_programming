#!/usr/bin/python3
"""
Module for best_score function.
"""


def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.

    Parameters:
    - a_dictionary (dict): The input dictionary.

    Returns:
    - The key with the biggest integer value.
      If no score found, returns None.
    """

    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
    else:
        return None


if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))

