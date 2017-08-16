#!/usr/bin/env python

import sys

def sigma(sequence, i, j):
    result = 0
    for k in range(i-1,j):
        result += sequence[k]
    return result


def mean(sequence):
    return (1 / len(sequence)) * sigma(sequence, 1, len(sequence))


def transpose(A):
    A_t = []
    for i in range(len(A[0])):
        A_t_row_i = []
        for j in range(len(A)):
            A_t_row_i.append(A[j][i])
        A_t.append(A_t_row_i)
    return A_t


def matrix_sum(A, B):
    if len(A) != len(B):
        return "Not Defined!!"
    elif len(A[0]) != len(B[0]):
        return "Not Defined!!"
    result = []
    for i in range(len(A)):
        result_row_i = []
        for j in range(len(A[0])):
            component_ij = A[i][j] + B[i][j]
            result_row_i.append(component_ij)
        result.append(result_row_i)
    return result


def upper_triangular_matrix(A):
    if len(A) != len(A[0]):
        return "Not Defined!!"
    result = []
    for i in range(len(A)):
        result_row_i = []
        for j in range(len(A[0])):
            if i <= j:
                result_row_i.append(A[i][j])
            else:
                result_row_i.append(0)
        result.append(result_row_i)
    return result


def lower_triangular_matrix(A):
    if len(A) != len(A[0]):
        return "Not Defined!!"
    result = []
    for i in range(len(A)):
        result_row_i = []
        for j in range(len(A[0])):
            if i >= j:
                result_row_i.append(A[i][j])
            else:
                result_row_i.append(0)
        result.append(result_row_i)
    return result


def matrix_product(A, B):
    if len(A[0]) != len(B):
        return "Not Defined!!"
    result = []
    for i in range(len(A)):
        result_row_i = []
        for j in range(len(B[0])):
            component_ij = 0
            for k in range(len(A[0])):
                component_ij += A[i][k] * B[k][j]
            result_row_i.append(component_ij)
        result.append(result_row_i)
    return result


def inner_product(u, v):
    if len(u) != len(v):
        return "Not Defined!!"

    result = 0
    for i in range(len(u)):
        result += u[i] * v[i]
    return result


def powerset(iterable):
    result = []
    n = len(iterable)
    counter = 2**n
    for i in range(counter):
        element_i = []
        bin_i = bin(i)[2:].zfill(n)
        mapping_index = list(bin_i)
        element_i = [iterable[j] for j in range(len(mapping_index)) if int(mapping_index[j]) == 1]
        result.append(element_i)
    return result


def vector_product(u, v):
    if len(u) != len(v): return "Not Defined!!"
    elif len(u) != 3: return "Not Defined!!"

    component_1 = u[1] * v[2] - u[2] * v[1]
    component_2 = u[2] * v[0] - u[0] * v[2]
    component_3 = u[0] * v[1] - u[1] * v[0]
    result = [component_1, component_2, component_3]
    return result

