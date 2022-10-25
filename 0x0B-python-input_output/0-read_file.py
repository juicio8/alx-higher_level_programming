#!/usr/bin/python3
""" The read-file module """


def read_file(filename=""):
    """ open and reads a file(UTF-8), prints to stdout """
    with open(filename, "r", encoding="UTF-8") as f:
        readfile = f.read
        print(readfile, end="")
