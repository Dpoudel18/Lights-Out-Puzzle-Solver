def nullity(matrix, m, n):
    piv_column = matrix[1]
    rref_matrix = matrix[0]
    len_piv_columns = len(piv_column)
    col_dim = m*n
    nullity = col_dim - len_piv_columns   
    return nullity