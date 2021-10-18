import numpy as np

def get_input(input_filename):
    input_filepath = "./inputs/" + input_filename
    inpfile = open(input_filepath, 'r')
    n = int(inpfile.readline())
    matA = []
    matb = []
    for j in range(n):
        line = inpfile.readline().split()
        i = [float(inp) for inp in line[:-1]]
        matA.append(i)
        matb.append(float(line[-1]))
    A = np.array(matA, dtype=float)
    b = np.array(matb, dtype=float)
    return A,b
