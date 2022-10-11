#!/usr/bin/python3
""" Defining a class Square"""


class Square:
    """ A class square
    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size):
        """ Initialize an instance of Square
        Args:
            size (int): size of the square"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Method Area
        Returns:
            area of the square"""
        return (self.__size) ** 2
