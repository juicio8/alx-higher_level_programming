#!/usr/bin/python3
""" The load_from_json_file """
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file”:

        Args:
            filename (str): the file name

    """
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
