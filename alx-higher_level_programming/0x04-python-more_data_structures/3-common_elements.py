#!/usr/bin/python3
"""
Module for common_elements function.
"""


def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.

    Parameters:
    - set_1 (set): The first set.
    - set_2 (set): The second set.

    Returns:
    - A set containing common elements in both sets.
    """

    common_set = set_1.intersection(set_2)

    return common_set


if __name__ == "__main__":
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))

