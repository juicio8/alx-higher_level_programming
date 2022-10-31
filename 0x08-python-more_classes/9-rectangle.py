#!/usr/bin/python3
""" module 9-rectangle """


class Rectangle:
    """
    A class to represent a square
    Attributes:
        width (int): width of a rectangle
        height (int): height of a rectangle
        number_of_instances (int): no of times an instance is created
        print_symbol (str): symbol to print
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle class
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns an area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Returns printable string representation of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return ((symbol * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area
        Args:
            rect_1 (Rectangle): first rectangle
            rect_2 (Rectangle): second rectangle
        Raises:
            TypeError: must be an instance of Rectangle
        Returns: greater rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_1.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

        @classmethod
        def square(cls, size=0):
            "returns a new Rectangle instance with width == height == size"
            return cls(size, size)
