#!/usr/bin/python3
""" The 1-ny_list module """


class MyList(list):
    """ a clss inheriting from list """
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
