import numpy as np

from inputters.get_input import get_input

from outputters.output_path import output_path
from outputters.out_ge_wop import out_ge_wop
from outputters.out_ge_p import out_ge_p
from outputters.out_ge_sp import out_ge_sp
from outputters.out_lu_ge_wop import out_lu_ge_wop
from outputters.out_cd import out_cd
from outputters.out_lu_cm_wop import out_lu_cm_wop
from outputters.out_lu_ge_p import out_lu_ge_p

from methods.ge_wop import ge_wop
from methods.ge_p import ge_p
from methods.ge_sp import ge_sp
from methods.lu_ge_wop import lu_ge_wop
from methods.cd  import cd
from methods.lu_cm_wop import lu_cm_wop
from methods.lu_ge_p import lu_ge_p



input_filename = input('Enter the name of the input file, present inside the "inputs" folder: ')
# input_filename = "test1"
A, b = get_input(input_filename)

methods = {
    1: "Gauss Elimination without Pivoting",
    2: "Gauss Elimination with Pivoting",
    3: "Gauss Elimination with Scaling & Pivoting",
    4: "LU Decomposition using Gauss Elimination without Pivoting",
    5: "LU Decomposition using Gauss Elimination with Pivoting",
    6: "LU Decomposition using Crout Method without Pivoting",
    7: "Cholesky Decomposition",
    8: "Exit"
}

while True:
    # decimal = int(input("Enter the number of decimal places till which the answer is to be printed: "))
    decimal = 4
    method_text = "Select the method of computation of solving a system of linear equations, Ax=b: \n"
    for k, v in methods.items():
        method_text += "\t " + str(k) + ". " + v + "\n"
    method_text += "---" * 45 + "\n"
    method = int(input(method_text))
    # method = 1
    if method == 1:
        x = ge_wop(A, b)
        if x is None:
            print("Division by zero will occur, currently without pivoting, this is not acceptable.")
        else:
            x = np.around(x, decimal)
            print(
                "Solution to the system of linear equations, Ax=b, using %s, where \nA = %s and \nb = %s is \nx = %s" % (
                methods[method], A, b, x))
            output_filepath = output_path(method, input_filename)
            out_ge_wop(x, methods[method], output_filepath)
        print("---" * 45)
    elif method == 2:
        x, P = ge_p(A, b)
        if x is None:
            print("Invalid")
        else:
            x = np.around(x, decimal)
            P = np.around(P, decimal)
            print(
                "Solution to the system of linear equations, Ax=b, using %s, where \nA = %s and \nb = %s with "
                "permutation matrix \nP = %s is \nx = %s" % (
                    methods[method], A, b, P, x))
            output_filepath = output_path(method, input_filename)
            out_ge_p(x, P, methods[method], output_filepath)
        print("---" * 45)
    elif method == 3:
        x = ge_sp(A, b)
        if x is None:
            print("Invalid")
        else:
            x = np.around(x, decimal)
            print(
                "Solution to the system of linear equations, Ax=b, using %s, where \nA = %s and \nb = %s  is \nx = %s" % (methods[method], A, b, x))
            output_filepath = output_path(method, input_filename)
            out_ge_sp(x, methods[method], output_filepath)
        print("---" * 45)
    elif method == 4:
        x, L, U = lu_ge_wop(A, b)
        if x is None:
            print("Division by zero will occur, currently without pivoting, this is not acceptable.")
        else:
            x = np.around(x, decimal)
            print(
                "Solution to the system of linear equations, Ax=b, using %s, where \nA = %s and \nb = %s is \nx = %s" % (
                    methods[method], A, b, x))
            print("LU decomposition for A, using %s, is \nL = %s \nU = %s" % (
                methods[method], L, U))
            output_filepath = output_path(method, input_filename)
            out_lu_ge_wop(x, L, U, methods[method], output_filepath)
        print("---" * 45)
    elif method == 5:
        x, P, L, U = lu_ge_p(A, b)
        if x is None:
            print("Division by zero will occur, currently without pivoting, this is not acceptable.")
        else:
            x = np.around(x, decimal)
            print(
                "Solution to the system of linear equations, Ax=b, using %s, where \nA = %s and \nb = %s is \nx = %s" % (
                    methods[method], A, b, x))
            print("Permutation matrix is: \nP = %s" % P)
            print("LU decomposition for A, using %s, is \nL = %s \nU = %s" % (
                methods[method], L, U))
            output_filepath = output_path(method, input_filename)
            out_lu_ge_p(x, P, L, U, methods[method], output_filepath)
        print("---" * 45)
    elif method == 6:
        x, L, U = lu_cm_wop(A, b)
        if x is None:
            print("Division by zero will occur, currently without pivoting, this is not acceptable.")
        else:
            x = np.around(x, decimal)
            print(
                "Solution to the system of linear equations, Ax=b, using %s, where \nA = %s and \nb = %s is \nx = %s" % (
                    methods[method], A, b, x))
            print("LU decomposition for A, using %s, is \nL = %s \nU = %s" % (
                methods[method], L, U))
            output_filepath = output_path(method, input_filename)
            out_lu_cm_wop(x, L, U, methods[method], output_filepath)
        print("---" * 45)
    elif method == 7:
        x, L = cd(A, b)
        if x is None:
            print("Invalid")
        else:
            x = np.around(x, decimal)
            L = np.around(L, decimal)
            print(
                "Solution to the system of linear equations, Ax=b, using %s, where \nA = %s and \nb = %s is \nx = %s" % (
                    methods[method], A, b, x))
            print("The cholesky factor for A, where \nA = %s  is \nL = %s" % (A, L))
            output_filepath = output_path(method, input_filename)
            out_cd(x, L, methods[method], output_filepath)
        print("---" * 45)
        print("---" * 45)
    elif method == 8:
        print("Thank you for using our program!!\nGoodbye!")
        print("---" * 45)
        break
    else:
        print("Invalid Selection, please select again")
