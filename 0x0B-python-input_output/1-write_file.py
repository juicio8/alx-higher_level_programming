#!/usr/bin/python3
""" The write file module """


def write_file(filename="", text=""):
    """  writes a string to a text file (UTF8)
         and returns the number of characters written:

         Args:
            filename (str): name of file
            text (str): text to be written
    """

    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
