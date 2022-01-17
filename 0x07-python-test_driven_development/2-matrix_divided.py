#!/usr/bin/python3
"""Divides all the integers in a matrix by the integer given.
All values in the matrix passed in must be integers.
"""


def matrix_divided(matrix, div):
    """First loop checks all indexes to make sure they're integers.
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        tmp = len(matrix[0])
        if len(row) is not tmp:
            raise TypeError("Each row of the matrix must have the same size")
        if tmp == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[0 for a in range(len(matrix[0]))] for b in range(len(matrix))]

    for row in range(len(matrix)):
        for item in range(len(matrix[0])):
            new_matrix[row][item] = round(matrix[row][item] / div, 2)

    return new_matrix
