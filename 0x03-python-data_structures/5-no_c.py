#!/usr/bin/python3
def no_c(my_string):
    """
    a function that removes all characters c and C from a string.
    """
    ups_string = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            ups_string = ups_string + x
    return ups_string
