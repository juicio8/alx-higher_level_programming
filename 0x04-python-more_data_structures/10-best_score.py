#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_score = float('-inf')
        max_key = ""
        for key in a_dictionary:
            if a_dictionary[key] > max_score:
                max_score = a_dictionary[key]
                max_key = key
        return max_key
    return None
