#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for a in range(len(matrix)):
        for i in range(len(matrix[a])):
            if i == len(matrix[a]) - 1:
                print("{:d}".format(matrix[a][i]), end="")
            else:
                print("{:d}".format(matrix[a][i]), end=" ")
        print("")
