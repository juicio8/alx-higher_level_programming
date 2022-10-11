#!/usr/bin/python3
""" Defines a clas Square """


class Square:
    """ Definition of Square

    Attributes:
        __size (int): size of a square
    """

    def __init__(self, size=0):
        """ create an instance of square

        args:
            size (int): size of a square"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
