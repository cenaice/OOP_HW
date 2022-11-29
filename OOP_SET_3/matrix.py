"""
Author: Victer Phiathep
Module for Homework 4, Problem 2
Object Oriented Programming (50:198:113), Fall 2022

Insert module documentation for Problem #2 here
"""

# IMPLEMENT ALL FUNCTIONS FOR MATRICES BELOW.
# DOCUMENT ALL FUNCTIONS APPROPRIATELY


def dimension(M):
    column = len(M)
    row = 0
    for x in M:
        row = len(x)
        return (column, row)


def row(M, i):
    """
    This function returns the i-th column in matrix M
    """
    rows = []
    for x in M:
        if i < 0 or i > len(x):
            raise IndexError("Out of range")
        rows.append(x[i-1])
    return rows


def column(M, j):
    """
    This function returns the j-th column in the matrix M
    """

    if j < 0 or j > len(M):
        raise IndexError("Out of range")
    return M[j-1]


def matrix_sum(A, B):
    """
    This function takes in two matrixes and adds them together to create a new
    matrix.
    """
    # Check for the same column and rows in matrix
    if len(A) != len(B):
        raise IndexError("Out of range")
    for x in range(len(A)): # Loops through matrix to make sure each List is equal
        if len(A[x]) != len(B[x]):
            raise IndexError("Out of range")
    
    new_matrix = [[A[i][j] + B[i][j]
                    for j in range(len(A[0]))] for i in range(len(A))]
    return new_matrix



def matrix_difference(A, B):
    """
    This function takes in two matrixes and subtracts them to create a new
    matrix.
    """
    # Check for the same column and rows in matrix
    if len(A) != len(B):
        raise IndexError("Out of range")
    for x in range(len(A)): # Loops through matrix to make sure each List is equal
        if len(A[x]) != len(B[x]):
            raise IndexError("Out of range")

    new_matrix = [[A[i][j] - B[i][j]
                    for j in range(len(A[0]))] for i in range(len(A))]
    return new_matrix


def matrix_product(A, B):
    """
    This function takes in two matrixes and multiplies them to create a new
    matrix.
    """
    # Check for the same column and rows in matrix
    if len(A) != len(B):
        raise IndexError("Out of range")
    for x in range(len(A)): # Loops through matrix to make sure each List is equal
        if len(A[x]) != len(B[x]):
            raise IndexError("Out of range")
    
    new_matrix = [[A[i][j] * B[i][j]
                    for j in range(len(A[0]))] for i in range(len(A))]
    return new_matrix


def reduce_matrix(M, i, j):
    # Check if i and j are valid inputs
    if len(M) < j:
        raise IndexError("Out of range")
    for x in M:
        if len(x) < i:
            raise IndexError("Out of range")

    # Creating new matrix
    new_matrix = []
    for arr in M:
        new_matrix.append(arr)
    del new_matrix[j-1][i-1] # Deleted the ith row and jth column

    return new_matrix



def determinant(M):
    # Check if it is a square matrix by checking if columns == row
    for x in M:
        if len(x) != len(M): # Checks if ROWS == COLUMNS
            raise Exception("Matrix is not a square")


def pretty_print(M):
    """
    This function prints our Matrix in a readable format.
    """
    for i in M:
        print('\t'.join(map(str, i)))


# USE THE FOLLOWING TEST CODE TO TEST YOUR FUNCTION
# IMPLEMENTATIONS ABOVE
if __name__ == "__main__":
    print("Testing module Problem 2, Homework 4: ")
    A = [[5, 3, -1], [9, 4, 12]]
    B = [[6, 9, 12], [-8, 6, -4], [7, 11, 13]]
    C = [[0, -21, -1], [11, 13, 17]]

    print("Three matrices have been created.")
    print("\nMatrix A equals \n")
    pretty_print(A)
    print("\nMatrix B equals \n")
    pretty_print(B)
    print("\nMatrix C equals \n")
    pretty_print(C)

    print("Matrix A has dimension ", dimension(A))
    print("Matrix B has dimension ", dimension(B))
    print("Matrix C has dimension ", dimension(C))

    print()
    print("The second row of matrix A is: ", row(A, 2))
    print("The third column of matrix B is: ", column(B, 3))
    print("The second column of matrix C is: ", column(C, 2))

    print()
    D = matrix_sum(A, C)
    print("The sum of matrices A and C is: \n")
    pretty_print(D)

    D = matrix_difference(C, A)
    print("The difference of matrices C and A is: \n")
    pretty_print(D)

    D = matrix_product(A, B)
    print("The product of  matrices A and B is: \n")
    pretty_print(D)

    D = matrix_product(A, C)
    print()

    D = reduce_matrix(A, 1, 1)
    print("Matrix obtained by removing row 1, column 1 of matrix A: \n")
    pretty_print(D)

    D = reduce_matrix(B, 3, 2)
    print("Matrix obtained by removing row 3, column 2 of matrix B: \n")
    pretty_print(D)

    D = determinant(B)
    print("The determinant of matrix B is: ", D)

    print("\nGoodbye!")
