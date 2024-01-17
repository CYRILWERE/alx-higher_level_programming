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
@staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        screen.bgcolor("white")

        pen = turtle.Turtle()
        pen.speed(2)

        for rect in list_rectangles:
            pen.color("blue")
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            for _ in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)

        for square in list_squares:
            pen.color("red")
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

        turtle.done()

if __name__ == "__main__":
    list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

    Base.draw(list_rectangles, list_squares)
