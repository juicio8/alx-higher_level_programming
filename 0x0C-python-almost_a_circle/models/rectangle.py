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
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif width <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if x < 0:
            raise ValueError("x must be >= 0")
        elif type(x) is not int:
            raise TypeError("x must be an integer")
        else:
            self.__x = x

        if y < 0:
            raise ValueError("y must be >= 0")
        elif type(y) is not int:
            raise TypeError("y must be an integer")
        else:
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
        if value < 0:
            raise TypeError("width must be >= 0")
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

    def area(self):
        """return area of a rectangle"""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the Rectangle instance with the character # """
        symbol = '#'
        for i in range(self.__height):
            print(self.__width * symbol)

    def __str__(self):
        """ overiding str method """"
       return (f'[Rectangle]({self.id}) {self.__x} / {self.__y} -
                {self.__width} / {self.__height}') 
