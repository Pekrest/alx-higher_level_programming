#!/usr/bin/python3
for nums in range(ord('z'), ord('a') - 1, -1):
    if nums % 2 == 0:
        diff = 0
    else:
        diff = 32
    print('{}'.format(chr(nums - diff)), end='')
