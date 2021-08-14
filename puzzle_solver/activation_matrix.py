import numpy as np

def activation_matrix(m,n):
    """  This function forms an m*n activation matrix of an m by n lights out puzzle. 
    "m" is the puzzle row number, and "n" is the puzzle column number
    
    It returns a the matrix in a list of a list of columns"""

    matrix_A = np.identity(m*n) # generate an m*n identity matrix
    for p in range(n):
        for q in range(m):
            i = n*q + p   # p controls movement along puzzle column and q controls movement 
            # along puzzle row. i is the matrix row number 

            if q > 0:   # To fill out the identity matrix below the diagonal
              matrix_A[i][i-n] = 1

            if q < m-1: # To fill out the identity matrix above the diagonal
              matrix_A[i][i+n] = 1

            if p > 0:   # To cover 1's right below the diagonal
              matrix_A[i][i-1] = 1

            if p < n-1: # To cover 1's right above the diagonal
              matrix_A[i][i+1] = 1

    matrix_A = matrix_A.astype(int) # converting numpy float array to numpy int array
    matrix_A = matrix_A.tolist() # converting numpy array to list

    return matrix_A


