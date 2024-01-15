#!/usr/bin/python3
"""
Module for returning the dictionary description with simple data structure
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representing the JSON-serializable attributes of the object.
    """
    return obj.__dict__


if __name__ == "__main__":
    pass  # You can add test cases here if needed

