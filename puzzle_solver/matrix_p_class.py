class P_matrix:
    """ A class containing function that perform operations on a matrix in field of p.
    The class takes the field and the matrix as an input at the point of instantiation"""
    def __init__(self,p,matrix) :
        self._p = p
        self._matrix = matrix
        self._inverse = list(range(self._p))
        self.calc_inverse()

    def get_p(self):
        return self._p

    def get_matrix(self):
        return self._matrix

    def add_row(self, row_1, row_2, m = 1):
        """ adds row_1 to row_2. If m is specified, m is the factor you multiply row 1 with before 
        adding"""

        matrix_A = self.get_matrix() # matrix is a list of a list
        first_row = matrix_A[row_1]
        second_row = matrix_A[row_2]
        for i in range(len(first_row)):
            second_row[i] = (m * first_row[i] + second_row[i]) % self.get_p()      
        return 

    def get_inverse(self):
        return self._inverse

    def calc_inverse(self):
        p_val = self.get_p()
        for i in range(2,p_val):
            for j in range(2, p_val):
                if i*j % p_val == 1 :
                    self._inverse[i] = j
        return


    def switch_row(self, row_1, row_2):
        matrix_A = self.get_matrix()
        matrix_A[row_1], matrix_A[row_2] = matrix_A[row_2], matrix_A[row_1]
        return 

    def multiply_row(self, row, m): # takes row index and the scaler multiplier
        matrix_A = self.get_matrix()
        for i in range(len(matrix_A[row])):
            matrix_A[row][i] = (m * matrix_A[row][i]) % self.get_p() 
        return