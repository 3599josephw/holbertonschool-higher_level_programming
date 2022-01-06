#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        x = " ".join(map(str, row))
        print("{}".format(x))
