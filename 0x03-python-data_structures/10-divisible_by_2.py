#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    truth = []
    for elem in my_list:
        truth.append(True) if elem % 2 == 0 else truth.append(False)
    return truth
