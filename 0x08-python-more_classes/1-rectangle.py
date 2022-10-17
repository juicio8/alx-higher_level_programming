#!/usr/bin/python3
""" 1-rectangle module """


class Rectangle:
    """
    A class to represent a square

    Attributes:
        width (int): width of a rectangle
        height (int): height of a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle class

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter method for private instance attribute width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method for private instance attribute width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter method for private instance attribute height
        Returns:
            (int): height of a rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for private instance attribute height """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
