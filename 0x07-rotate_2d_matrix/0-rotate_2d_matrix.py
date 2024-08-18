#!/usr/bin/python3
"""
0x07 - Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed_matrix = [[0] * rows for _ in range(cols)]


    for i in range (rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    for row in transposed_matrix:
        row.reverse()

    return transposed_matrix
