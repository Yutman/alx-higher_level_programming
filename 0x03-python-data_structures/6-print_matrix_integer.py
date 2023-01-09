#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = len(matrix)
    for i in range(a):
        b = len(matrix[i])
        for j in range(b):
            if j < b - 1:
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                print("{:d}".format(matrix[i][j]), end="")
        print("")
