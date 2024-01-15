#!/usr/bin/python3
"""
Module for defining a Student class.
"""

class Student:
    """
    Class that defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to retrieve. Default is None.

        Returns:
            dict: A dictionary representing the Student instance with selected attributes.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from a dictionary.

        Args:
            json (dict): A dictionary where keys are attribute names and values are attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)


if __name__ == "__main__":
    pass  # You can add test cases here if needed

