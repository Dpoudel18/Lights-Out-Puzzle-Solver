def sol_no_sol(matrix, m, n):
    """
    returns the |sollution space| if there is a solution and 
    "NO SOLUTION" if there is not

    """
    piv_column = matrix[1]
    rref_matrix = matrix[0]
    len_piv_columns = len(piv_column)
    # print("length of pivot column: ", len_piv_columns)
    col_dim = m*n
    nullity = col_dim - len_piv_columns    
    for i in range(len_piv_columns, nullity+len_piv_columns+1):
        if i == m*n:
            return nullity
        elif rref_matrix[i][-1] != 0:
            return 'NO SOLUTIONS'
        else:
            return nullity
        
def bool_sol_no_sol(matrix, m, n):
    if sol_no_sol(matrix, m, n) == 'NO SOLUTIONS':
        return 0
    else:
        return 1