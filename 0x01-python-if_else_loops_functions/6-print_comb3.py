#!/usr/bin/python3
for f_nums in range(0, 10):
    for s_nums in range(f_nums + 1, 10):
        if f_nums == 8 and s_nums == 9:
            print('89')
        else:
            print('{}{}, '.format(f_nums, s_nums), end='')
