from math import sqrt
import numpy as np


def cholesky(A):
    n = A.shape[0]
    L = np.zeros((n,n))
    L = L.astype('float32')
    for i in range(n):
        for k in range(i + 1):
            tmp = sum(L[i][j] * L[k][j] for j in range(k))
            if i == k:
                L[i][k] = sqrt(A[i][i] - tmp)
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp))
    U = np.transpose(L)
    # print(L, U)
    return L, U

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




def cd(A, b):
    L, U = cholesky(A)
    y = back_substitution_lower(L, b)
    x = back_substitution_upper(U, y)
    return x, L


#
# A = np.array([[4.0, 2.0, 0.0], [2.0, 4.0, 1.0], [0.0, 1.0, 5.0]])
# A = A.astype('float32')
#
# b = np.array([10, 11.5, 5])
# b = b.astype('float32')
#
#
# cd_solve(A, b)
#
