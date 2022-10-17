#!/usr/bin/python3
""" add_integer module """


def add_integer(a, b=98):
    """ add_integer : a function to add two integers

        Args:
            a (int/float): the first integer
            b (int/float): the second integer

        Raises:
            TypeError: when passing non integer argument

        Returns:
            (int) : sum of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
