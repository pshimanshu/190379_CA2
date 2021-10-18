import numpy as np

def decompose(A, b):
    n = A.shape[0]
    L = np.zeros((n, n))
    L = L.astype('float32')
    for i in range(n):
        L[i, i] = 1
    for i in range(n - 1):
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            L[j, i] = factor
            A[j, :] -= factor * A[i, :]
            b[j] -= factor * b[i]
    U = A
    return L, U, b

def back_substitution(A, b):
    n = A.shape[0]
    x = np.zeros(n)
    x[n - 1] = b[n - 1] / A[n - 1, n - 1]
    for row in range(n - 2, -1, -1):
        sums = b[row] - np.sum(np.multiply(A[row, row + 1:], x[row + 1:]))
        x[row] = sums / A[row, row]
        # print('A = \n%s and \nb = %s and \nx = %s' % (A,b,x))
    return x

def lu_ge_wop(A, b):
    L, U, b = decompose(A, b)
    x = back_substitution(U, b)
    # print(x)
    return x, L, U

#
# A = np.array([[4.0, 2.0, 0.0], [2.0, 4.0, 1.0], [0.0, 1.0, 5.0]])
# # A = np.array([[1, -1, 2], [4, 0, 1], [-3, 1, -3]])
# A = A.astype('float32')
#
#
# b = np.array([10, 11.5, 5])
# b = b.astype('float32')
#
#
# lu_ge_wop(A, b)
