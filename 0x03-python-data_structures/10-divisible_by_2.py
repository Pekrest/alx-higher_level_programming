#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    a function that finds all multiples of 2 in a list.
    """
    lists = []
    for x in range(0, len(my_list)):
        if my_list[x] % 2 == 0:
            lists = lists + [True]
        else:
            lists = lists + [False]
    return lists
