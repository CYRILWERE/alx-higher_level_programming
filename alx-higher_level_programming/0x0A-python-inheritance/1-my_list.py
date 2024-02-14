#!/usr/bin/python3
"""
Module for MyList class
"""


class MyList(list):
    """
    A class that inherits from list and adds a print_sorted method
    """

    def print_sorted(self):
        """
        Prints the list in sorted order (ascending)
        """
        print(sorted(self))

