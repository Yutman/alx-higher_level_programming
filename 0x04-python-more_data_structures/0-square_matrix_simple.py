#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_cpy = [x[:] for x in matrix]

    for i in range(0, len(matrix_cpy)):
        for j in range(0, len(matrix_cpy[i])):
            matrix_cpy[i][j] = matrix_cpy[i][j] * matrix_cpy[i][j]

    return (matrix_cpy)
