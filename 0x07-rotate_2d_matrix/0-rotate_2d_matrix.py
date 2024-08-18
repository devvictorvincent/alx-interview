#!/usr/bin/python3
"""
0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    rows = len(matrix)

    # Lets Transpose the matrix
    for i in range(rows):
        for j in range(i, rows):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Lets Reverse each row of the matrix
    for i in range(rows):
        matrix[i].reverse()
