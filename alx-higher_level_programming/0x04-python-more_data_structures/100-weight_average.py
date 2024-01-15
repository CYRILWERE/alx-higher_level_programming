#!/usr/bin/python3
"""
Module for weight_average function.
"""


def weight_average(my_list=[]):
    """
    Returns the weighted average of all integers tuple (<score>, <weight>).

    Parameters:
    - my_list (list): The list of tuples containing score and weight.

    Returns:
    - The weighted average.
    """

    if not my_list:
        return 0

    total_score = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)

    if total_weight == 0:
        return 0

    return total_score / total_weight


if __name__ == "__main__":
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))

