#!/usr/bin/python3
""" The base.py module """

class Base:
    """ Attributes:
        __nb_objects (int)
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """ initialize
        Args:
            id (int): 
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
