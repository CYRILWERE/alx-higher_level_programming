#!/usr/bin/python3
"""Defines a MagicClass class."""

import math


class MagicClass:
    """Represents a MagicClass.

    Attributes:
        __radius (float): The radius of the MagicClass.
    """

    def __init__(self, radius=0):
        """Initializes a new instance of the MagicClass class.

        Args:
            radius (float): The radius of the MagicClass. Default is 0.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Calculates and returns the area of the MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates and returns the circumference of the MagicClass."""
        return 2 * math.pi * self.__radius

