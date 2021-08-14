from matrix_p_class import *
import numpy as np

def RREF(tuple_ref_pivot_column,p):
    piv_col = tuple_ref_pivot_column[1]
    n_i = len(piv_col)
    mat = tuple_ref_pivot_column[0]
    obj_matrix = P_matrix(p,mat)
    for j in reversed(range(len(piv_col))):
        for i in reversed(range(n_i-1)): 
            if obj_matrix.get_matrix()[i][j] != 0: # if you find a non-zero 
                obj_matrix.add_row(n_i-1, i, -obj_matrix.get_matrix()[i][j]) # increase leading row by a factor
                # the non-zero variable and add leading row to current row in mod p.
        n_i -= 1
    return np.array(obj_matrix.get_matrix()).astype(int).tolist() , piv_col