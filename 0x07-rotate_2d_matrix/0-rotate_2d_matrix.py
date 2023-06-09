#!/usr/bin/python3
"""
2D Matrix rotation module
"""


def rotate_2d_matrix(matrix):
    """
    A function that rotates 2D matric
    """
    matrix_len = len(matrix)

    # Iterating through the rows and cols and swapping them
    for r in range(matrix_len):
        for c in range(r, matrix_len):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    for r in range(matrix_len):
        matrix[r] = matrix[r][::-1]
        # ','.join(map(str, r))
