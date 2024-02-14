#!/usr/bin/python3
"""
Module for only_diff_elements function.
"""


def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    Parameters:
    - set_1 (set): The first set.
    - set_2 (set): The second set.

    Returns:
    - A set containing elements present in only one of the sets.
    """

    diff_set = set_1.symmetric_difference(set_2)

    return diff_set


if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))

