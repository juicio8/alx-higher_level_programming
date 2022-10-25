#!/usr/bin/python3
""" The to_json_string module """


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string):

        Args:
            my_obj (object): object to be stringified
    """
    return json.dumps(my_obj)
