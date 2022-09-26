#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        if 0 <= idx < len( my_list):
            for item in my_list:
                if my_list.index(item) == idx:
                    my_list.remove(item)
    return my_list
