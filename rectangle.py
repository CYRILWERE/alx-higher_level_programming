#!/usr/bin/python3
"""Rectangle module"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class, inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for Rectangle class"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute"""
        self.validate_positive_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute"""
        self.validate_positive_integer("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute"""
        self.validate_non_negative_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute"""
        self.validate_non_negative_integer("y", value)
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle instance with the character #"""
        for _ in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """Override __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """Update attributes using no-keyword and keyword arguments"""
        attributes = ["id", "width", "height", "x", "y"]
        for i, value in enumerate(args):
            setattr(self, attributes[i], value)

        if args:
            return

        for key, value in kwargs.items():
            setattr(self, key, value)

    def validate_positive_integer(self, attribute_name, value):
        """Validate if the value is a positive integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attribute_name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(attribute_name))

    def validate_non_negative_integer(self, attribute_name, value):
        """Validate if the value is a non-negative integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attribute_name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute_name))

if __name__ == "__main__":
    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())

    print("---")

    r4 = Rectangle(4, 6)
    r4.display()

    print("---")

    r5 = Rectangle(2, 2)
    r5.display()

    print("---")

    r6 = Rectangle(4, 6, 2, 1, 12)
    print(r6)

    r7 = Rectangle(5, 5, 1)
    print(r7)

    print("---")

    r8 = Rectangle(2, 3, 2, 2)
    r8.display()

    print("---")

    r9 = Rectangle(3, 2, 1, 0)
    r9.display()

    print("---")

    r10 = Rectangle(10, 10, 10, 10)
    print(r10)

    r10.update(89)
    print(r10)

    r10.update(89, 2)
    print(r10)

    r10.update(89, 2, 3)
    print(r10)

    r10.update(89, 2, 3, 4)
    print(r10)

    r10.update(89, 2, 3, 4, 5)
    print(r10)

    print("---")

    r11 = Rectangle(10, 10, 10, 10)
    print(r11)

    r11.update(height=1)
    print(r11)

    r11.update(width=1, x=2)
    print(r11)

    r11.update(y=1, width=2, x=3, id=89)
    print(r11)

    r11.update(x=1, height=2, y=3, width=4)
    print(r11)

