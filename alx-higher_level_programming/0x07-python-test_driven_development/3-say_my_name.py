#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints a message with the given first and last names.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name (default is "").

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name).strip())

if __name__ == "__main__":
    pass  # Add any additional code for standalone execution if needed

