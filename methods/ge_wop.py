import numpy as np


def forward_elimination(A, b):
    n = A.shape[0]
    for row in range(0, n - 1):
        for i in range(row + 1, n):
            factor = A[i, row] / A[row, row]
            A[i, row:] -= factor * A[row, row:]
            b[i] -= factor * b[row]
        # print('A = \n%s and \nb = %s' % (A,b))
    return A, b


def back_substitution(A, b):
    n = A.shape[0]
    x = np.zeros(n)
    x[n - 1] = b[n - 1] / A[n - 1, n - 1]
    for row in range(n - 2, -1, -1):
        sums = b[row] - np.sum(np.multiply(A[row, row + 1:], x[row + 1:]))
        x[row] = sums / A[row, row]
        # print('A = \n%s and \nb = %s and \nx = %s' % (A,b,x))
    return x


def ge_wop(A, b):
    n = A.shape[0]
    if any(np.diag(A) == 0):
        return None
    A, b = forward_elimination(A, b)
    x = back_substitution(A, b)
    # print(x)
    return x
