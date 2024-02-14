#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = ['.', '?', ':']

    for char in text:
        print(char, end="")
        if char in punctuation_chars:
            print("\n\n", end="")

if __name__ == "__main__":
    pass  # Add any additional code for standalone execution if needed

