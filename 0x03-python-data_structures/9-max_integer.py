#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        ntive_inf = float('-inf')
        max_item = ntive_inf
        for elem in my_list:
            if elem > max_item:
                max_item = elem
        return max_item
    return None

print(max_integer([-5, 7, 0, 8]))
