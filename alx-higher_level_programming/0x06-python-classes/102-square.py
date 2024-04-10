#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represents a square.

    Attributes:
        __size (float or int): The size of the square.
    """

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.

        Args:
            size (float or int): The size of the square. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculates and returns the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Overrides the default equality operator."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Overrides the default inequality operator."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Overrides the default less-than operator."""
        return self.area() < other.area()

    def __le__(self, other):
        """Overrides the default less-than or equal to operator."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Overrides the default greater-than operator."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Overrides the default greater-than or equal to operator."""
        return self.area() >= other.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")

