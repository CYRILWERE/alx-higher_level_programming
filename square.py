#!/usr/bin/python3
"""Square module"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        self.validate_positive_integer("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes using no-keyword and keyword arguments"""

        attributes = ["id", "size", "x", "y"]

        for i, value in enumerate(args):
            setattr(self, attributes[i], value)

        if args:
            return

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

if __name__ == "__main__":
    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()

