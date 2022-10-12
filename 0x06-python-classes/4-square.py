#!/usr/bin/python3
""" Defining a class Square"""


class Square:
    """ A class square
    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size):
        """ Initialize an instance of Square
        args:
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
        return self.__size * self.__size

    @property
    def size(self):
        """getter of __size

        Returns:
            The size of a square"""

        return self.__size

    @size.setter
    def size(self, value):
        """ setter of __size

        Args:
            value (int): size of a square """
        if value is not int:
            raise TypeError("size musbe be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
