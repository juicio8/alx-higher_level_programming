#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = -inf
        for elem in my_list:
            if elem > max:
                max = elem
        return max
    return None
