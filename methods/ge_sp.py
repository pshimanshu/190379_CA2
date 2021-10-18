import numpy as np


def forward_elimination(A, b, row_id, itr):
    row_id -= 1
    itr -= 1
    n = A.shape[0]
    for row in range(0, n):
        if row == row_id:
            continue
        factor = A[row, itr] / A[row_id, itr]
        A[row, itr:] -= factor * A[row_id, itr:]
        b[row] -= factor * b[row_id]
    # print('A = \n%s and \nb = %s' % (A, b))
    return A, b


def forward(A, b):
    n = A.shape[0]
    order = []
    left = list(range(n))
    s = np.array([max(abs(row)) for row in A])
    for itr in range(1, n + 1):
        # print("itr: ", "----", itr)
        curr = [abs(A[row][itr - 1] / s[row]) for row in left]
        row_id = left[int(np.argmax(curr))]
        order.append(row_id + 1)
        left.remove(row_id)
        A, b = forward_elimination(A, b, row_id + 1, itr)
    return A, b, order


def back_substitution(A, b, order):
    n = A.shape[0]
    x = np.zeros(n)
    i = 0
    for row in order:
        row -= 1
        x[i] = b[row] / A[row, i]
        i += 1
    # print('A = \n%s and \nb = %s and \nx = %s' % (A,b,x))
    return x


def ge_sp(A, b):
    A1, b1, order = forward(A, b)
    x = back_substitution(A1, b1, order)
    return x
#
#
# A = np.array([[3, -13, 9, 3], [-6, 4, 1, -18], [6, -2, 2, 4], [12, -8, 6, 10]])
# #A = np.array([[4.0, 2.0, 0.0], [2.0, 4.0, 1.0], [0.0, 1.0, 5.0] ])
# A = A.astype('float32')
#
# b = np.array([-19, -34, 16, 26])
# #b = np.array([10,11.5,5])
# b = b.astype('float32')
#
# ge_sp(A, b)
