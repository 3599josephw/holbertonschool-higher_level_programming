#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    N = len(matrix)
    M = len(matrix[0])

    sqr = [[0 for a in range(M)] for b in range(N)]

    for row in range(N):
        for i in range(M):
            sqr[row][i] = matrix[row][i]**2

    return sqr
