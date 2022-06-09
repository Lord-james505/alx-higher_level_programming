#!/usr/bin/python3


def best_score(a_dictionary):
    """
    a function that returns a key with the biggest integer value
    """
    highest = 0
    win = None
    if type(a_dictionary) is dict:
        for key, value in a_dictionary.items():
            if value > highest:
                highest = value
                win = key
    return win
