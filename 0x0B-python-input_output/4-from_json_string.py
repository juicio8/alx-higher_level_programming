#!/usr/bin/python3
""" The to_json_string module """
import json


def to_json_string(my_str):
    """  returns an object (Python data structure)
         represented by a JSON string:
        Args:
            my_str (str): object to be stringified
    """
    return json.loads(my_str)
