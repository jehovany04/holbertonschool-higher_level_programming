#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return

    if len(matrix) < 1:
        print()
        return

    for v in matrix:
        print(' '.join(map(str, v)))
        print(0 * "{:d}".format(0), end='')
