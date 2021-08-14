import numpy as np
import pprint
import time
from matrix_p_class import *
from activation_matrix import *
from build_matrix_for_rref import *
from row_echelon_form import REF
from reduced_row_echelon_form import RREF
from nullity import *
from solution_noSolution import *

def puzzle_solve(rref, a, b):
    arr = []
    new = []
    if bool_sol_no_sol(rref, a, b) == 0:
        return 'No solution exists'
    else:
        for i in rref:
            arr.append(i[-1])
        arr = np.array_split(arr,a)
        for i in arr:
            new.append(i.tolist())
        return new

if __name__=="__main__":
    a = int(input('Specify the number of rows:\n'))
    b = int(input('Specify the number of columns:\n'))
    p = int(input('Specify the number of colors:\n'))
    my_matrix = build_matrix_for_rref(a,b)
    pp = pprint.PrettyPrinter(depth=6)
    A = P_matrix(p, my_matrix)
    ref=REF(A,a,b)
    rref = RREF(ref,p)[0]
    pp.pprint(puzzle_solve(rref, a, b))
 