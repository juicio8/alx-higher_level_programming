#!/usr/bin/python3
""" The save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation:

        Args:
            my_obj (obj): the object
            filename (str): file

    """

    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
