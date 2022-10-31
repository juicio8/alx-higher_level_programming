#!/usr/bin/python3
""" The Rectangle module """
from models.base import Base


class Rectangle(Base):
    """ The Rectangle class
    width (int): width of a rectangle
    height (int): height of a rectangle
    x :
    y :
    id: id of base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializer """

        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ getter for width
        Returns:
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter
        Args:
            value(int): value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise TypeError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter
            Args:
            value(int): value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise TypeError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
