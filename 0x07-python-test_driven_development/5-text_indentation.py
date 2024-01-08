#!/usr/bin/python3
"""
This module contains a function that indents texts.
"""

def text_indentation(text):
    """Print a text with 2 new lines after each ".", "?", or ":"

    Args:
        text (str): The string to be printed

    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_spaces = True
    for char in text:
        if char == "\n" or char in ".?:":
            print("\n\n", end="")
            skip_spaces = True
        elif char == " ":
            if not skip_spaces:
                print(char, end="")
            skip_spaces = True
        else:
            print(char, end="")
            skip_spaces = False

# Example usage:
text_indentation("This is a sample text. It demonstrates the text_indentation functio
