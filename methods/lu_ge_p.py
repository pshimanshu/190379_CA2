import numpy as np

def decompose(A):
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=np.double)
    P = np.eye(n, dtype=np.double)
    for i in range(n):
        for k in range(i, n):
            if ~np.isclose(U[i, i], 0.0):
                break
            U[[k, k + 1]] = U[[k + 1, k]]
            P[[k, k + 1]] = P[[k + 1, k]]
        factor = U[i + 1:, i] / U[i, i]
        L[i + 1:, i] = factor
        U[i + 1:] -= factor[:, np.newaxis] * U[i]
    # print(L)
    # print(U)
    return P, L, U


def back_substitution_lower(L, b):
    n = L.shape[0]
    y = np.zeros(n)
    y[0] = b[0]/L[0, 0]
    for row in range(1, n):
        sums = b[row] - np.sum(np.multiply(L[row, :row], y[:row]))
        y[row] = sums / L[row, row]
    # print(y)
    return y

def back_substitution_upper(U, y):
    n = U.shape[0]
    x = np.zeros(n)
    x[n - 1] = y[n - 1] / U[n - 1, n - 1]
    for row in range(n - 2, -1, -1):
        sums = y[row] - np.sum(np.multiply(U[row, row + 1:], x[row + 1:]))
        x[row] = sums / U[row, row]
        # print('U = \n%s and \ny = %s and \nx = %s' % (U,y,x))
    # print(x)
    return x



def lu_ge_p(A, b):
    P, L, U = decompose(A)
    y = back_substitution_lower(L, b)
    x = back_substitution_upper(U, y)
    return x, P, L, U


A = np.array([[4.0, 2.0, 0.0], [2.0, 4.0, 1.0], [0.0, 1.0, 5.0]])
# A = np.array([[7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6]])
A = A.astype('float32')


b = np.array([10, 11.5, 5])
b = b.astype('float32')

lu_ge_p(A, b)
