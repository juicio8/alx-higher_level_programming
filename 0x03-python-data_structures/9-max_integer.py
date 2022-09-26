#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_item = -inf
        for elem in my_list:
            if elem > max_item:
                max_item = elem
        return max_item
    return None
