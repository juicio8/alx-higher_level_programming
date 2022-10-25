#!/usr/bin/python3
""" The append_write module """


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8)
        and returns the number of characters added

        Args:
            filename (str): file name
            text (str): text
        """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
