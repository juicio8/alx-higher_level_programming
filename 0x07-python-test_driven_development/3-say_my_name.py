#!/usr/bin/python3
""" The say_my_name module"""


def say_my_name(first_name, last_name=""):
    """
    Prints full name in a sentence

    Parameters:
        first_name (str): a first name
        last_name (str): a last name

    Returns:
        sentence (str): My name is + first_name + last_name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
