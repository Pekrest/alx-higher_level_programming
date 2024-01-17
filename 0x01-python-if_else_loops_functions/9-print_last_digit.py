#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        l_nums = number % -(10)
        print(-(l_nums), end='')
    else:
        l_nums = number % 10
        print(l_nums, end='')
    return abs(l_nums)
