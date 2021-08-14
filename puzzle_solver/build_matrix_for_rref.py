from activation_matrix import *

def build_matrix_for_rref(m,n):
    """ This function takes inputs of m-number of rows and n-number of columns and forms a 
    matrix for computing the Gaus-Jordan elimination of a lights out puzzle whose lights 
    start all off and to be all switched on
    
    It returns the matrix as a list of columns with an element of the solution vector at the end"""

    soln_state_vec = [[1]]*m*n # Create an m*n long vector of all ones

    mat_for_rref = np.append(activation_matrix(m,n), soln_state_vec, axis=1) # Attach the solution state vector to the end of the matrix

    return mat_for_rref.tolist()