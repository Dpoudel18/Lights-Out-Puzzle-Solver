from matrix_p_class import *
import numpy as np

def REF(matrix, m,n):
    """ A function that computes the Row Echelon Form of an m*n matrix.

    It take in an input of the matrix whose last column are the elements of the solution state vector
    and returns the matrix in an REF as a list of columns"""

    pivot_columns=[] # specifies the columns of the pivots(the leading variable of a row).
    # NB: the length of the pivot columns equals the number of rows with pivots

    for j in range((m*n)): # for each column in the matrix
        for i in range(len(pivot_columns), m*n): # for each row beginning from the row whose pivot is to be found
            if matrix.get_matrix()[i][j] != 0: # if the element is a non zero,
                # i is the row in column j with the leading variable.

                matrix.switch_row(i,len(pivot_columns)) # switch matrix[i] to the row whose leading variable is 
                # to be determined(number of pivot columns recorded thus far)

                matrix.multiply_row(len(pivot_columns),matrix.get_inverse()[matrix.get_matrix()[len(pivot_columns)][j]]) # multiply the row
                # with the leading variable by the inverse of the leading varible to make it one.

                pivot_columns.append(j) # store pivot in pivot column

                break # move to the next for loop

        for i in range(len(pivot_columns),m*n): # for all row below that of the leading variable
            if matrix.get_matrix()[i][j] != 0: # if you find a non-zero
                
                matrix.add_row(len(pivot_columns)-1, i, -matrix.get_matrix()[i][j]) # increase leading row by a factor
                # the non-zero variable and add leading row to current row in mod p.
    return np.array(matrix.get_matrix()).astype(int).tolist() , pivot_columns

    