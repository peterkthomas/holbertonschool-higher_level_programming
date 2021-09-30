#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in mtx:
        i = 0
        for j in row:
            len_mtx = len(row)
            i += 1
            print("{:d}".format(j), end="")
            if i != len_mtx:
                print(" ", end="")
        print("")
