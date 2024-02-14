#!/usr/bin/python3
"""
Module for roman_to_int function.
"""


def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Parameters:
    - roman_string (str): The input Roman numeral string.

    Returns:
    - An integer representing the converted value.
    - If the roman_string is not a string or None, returns 0.
    """

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}

    result = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = roman_dict[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result


if __name__ == "__main__":
    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

