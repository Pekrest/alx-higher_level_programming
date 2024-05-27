#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    a function that prints a matrix of integers.
    """
    for row in matrix:
        for x in range(len(row)):
            if x != 0:
                print(" ", end="")
            print("{:d}".format(row[x]), end="")
        print()
