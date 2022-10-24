#!/usr/bin/python3
""" Geometry module """


class BaseGeometry:
    """ BaseGeometry class"""

    def area(self):
        """ public instance method """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates that value is an integer greater than 0 """

        if type(value) is not int:
            raise TypeError("{name} must be an integer")
        if value <= 0:
            raise ValueError("{name} must be greater than")
