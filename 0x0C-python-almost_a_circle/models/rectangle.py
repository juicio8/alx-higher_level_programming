#!/usr/bin/python3
""" The Rectangle module """


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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        self.__height = value
