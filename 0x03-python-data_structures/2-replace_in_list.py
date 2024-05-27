#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    a function that replaces an element of a list at a specific
    position (like in C).
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    for x in range(len(my_list)):
        if x == idx:
            my_list[x] = element
            return my_list
