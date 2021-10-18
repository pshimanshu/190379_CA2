import numpy as np


def pivot(A, row, ps):
    max_elem = -1e100
    max_row = -1
    n = A.shape[0]
    for r in range(row, n):
        if abs(A[r, row]) > max_elem:
            max_elem = abs(A[r, row])
            max_row = r
    A[[row, max_row]] = A[[max_row, row]]
    ps.append(max_row)
    return A, ps


def forward_elimination(A, b, ps):
    n = A.shape[0]
    for row in range(n):
        A, ps = pivot(A, row, ps)
        for i in range(row + 1, n):
            factor = A[i, row] / A[row, row]
            A[i, :] -= factor * A[row, :]
            b[i] -= factor * b[row]
    return A, b, ps


def back_substitution(A, b):
    n = A.shape[0]
    x = np.zeros(n)
    for row in range(n - 1, -1, -1):
        sums = b[row] - np.sum(np.multiply(A[row, row:], x[row:]))
        x[row] = sums / A[row, row]
    return x


def find_permutation(A, ps):
    n = A.shape[0]
    P = np.zeros((A.shape))
    for i in range(n):
        P[i, ps[i]] = 1
    # print(P)
    return P


def ge_p(A, b):
    ps = []

    A1, b1, ps = forward_elimination(A, b, ps)
    print("----PS::  ", ps, "----------")
    P = find_permutation(A, ps)

    x = back_substitution(A1, b1)
    return x, P
