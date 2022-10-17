#!/usr/bin/python3
""" The matrix-divided module"""

def matrix_divided(matrix, div):
    """
    Returns a new matrix, matrix divided by div

    Parameters:
        matrix (list): a list with a list, integer or float
        div (int/float): an integer or float

    Returns:
        list (list): a new matrix
    """

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

