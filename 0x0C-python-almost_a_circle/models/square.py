#!/usr/bin/python3
""" The Square module"""
from models.rectangle import *
from models.base import *


class Square(Rectangle):
    """ the Square class
        Args:
            size (int) : size of a square
            x (int)
            y(int)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing"""
        super().__init__(size, size, x, y, id=None)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(
                self.id,
                self.x,
                self.y,
                self.width)
