#!/usr/bin/python3
"""Base module"""

import json

class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return list representation of json_string"""

        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON string representation of list_objs to a file"""

        file_name = cls.__name__ + ".json"

        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(file_name, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """Return list of instances from JSON file"""

        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, mode="r", encoding="utf-8") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

