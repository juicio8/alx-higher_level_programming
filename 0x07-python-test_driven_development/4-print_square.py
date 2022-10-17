#!/usr/bin/python3
""" The print_square module"""


def print_square(size):
    """
    Prints a square with the character #

    Parameters:
        size (int) :  the size length of the square

    Returns:
        no returns
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print('#' * size)
