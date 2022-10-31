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
