"""
Author: Victer Phiathep
Module for Homework 4, Problem 3
Object Oriented Programming (50:198:113), Fall 2022

Insert module documentation for Problem #3 here
"""

class Matrix:
    def __init__(self, L):
        self.matrix = L
        

    def dimension(self):
        column = len(self.matrix)
        row = 0
        for x in self.matrix:
            row = len(x)
            return (column, row)

    def row(self, i):
        rows = []

        for x in self.matrix:
            if i < 0 or i > len(x):
                raise IndexError("Out of range")
            rows.append(x[i-1])
        return rows

    def column(self, j):
        if j < 0 or j > len(self.matrix):
            raise IndexError("Out of range")
        return self.matrix[j-1]

    def __add__(self, other):
        """
        This function adds two matrixes together
        """
        # Check for the same column and rows in matrix
        if len(self.matrix) != len(other):
            raise IndexError("Out of range")
        for x in range(len(self.matrix)): # Loops through matrix to make sure each List is equal
            if len(self.matrix[x]) != len(other[x]):
                raise IndexError("Out of range")



        new_matrix = [[self.matrix[i][j] + other[i][j]
                        for j in range(len(self.matrix[0]))] for i in range(len(other))]
        return new_matrix

    def __sub__(self, other):
        """
        This function subtracts two matrixes
        """
        # Check for the same column and rows in matrix
        if len(self.matrix) != len(other):
            raise IndexError("Out of range")
        for x in range(len(self.matrix)): # Loops through matrix to make sure each List is equal
            if len(self.matrix[x]) != len(other[x]):
                raise IndexError("Out of range")

        new_matrix = [[self.matrix[i][j] - other[i][j]
                        for j in range(len(self.matrix[0]))] for i in range(len(other))]
        return new_matrix

    def __mul__(self, other):
        """
        This function multiplies two matrixes
        """
        # Check for the same column and rows in matrix
        if len(self.matrix) != len(other):
            raise IndexError("Out of range")
        for x in range(len(self.matrix)): # Loops through matrix to make sure each List is equal
            if len(self.matrix[x]) != len(other[x]):
                raise IndexError("Out of range")


        new_matrix = [[self.matrix[i][j] * other[i][j]
                        for j in range(len(self.matrix[0]))] for i in range(len(other))]
        return Matrix(new_matrix)

    def reduce_matrix(self, i, j):
        # Check if i and j are valid inputs
        if len(self.matrix) < j:
            raise IndexError("Out of range")
        for x in self.matrix:
            if len(x) < i:
                raise IndexError("Out of range")

        # Creating new matrix
        new_matrix = []
        for arr in self.matrix:
            new_matrix.append(arr)
        del new_matrix[j-1][i-1] # Deleted the ith row and jth column

        return Matrix(new_matrix)

    def determinant(self):
        # Check if it is a square matrix by checking if columns == row
        # Check if it is a square matrix by checking if columns == row
        for x in self.matrix:
            if len(x) != len(self.matrix): # Checks if ROWS == COLUMNS
                raise Exception("Matrix is not a square")

    def __str__(self):
        new_s = ""
        for i in self.matrix:
            new_s+='\t'.join(map(str, i))
        return new_s

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self,key): # getitem method to be able to subscript through our matrix
        return self.matrix[key]

# Editted from matrx.py to support the Matrix() class
if __name__ == "__main__":
    print("Testing module Problem 3, Homework 4: ")
    A = Matrix([[5, 3, -1], [9, 4, 12]])
    B = Matrix([[6, 9, 12], [-8, 6, -4], [7, 11, 13]])
    C = Matrix([[0, -21, -1], [11, 13, 17]])

    print("Three matrices have been created.")
    print("\nMatrix A equals \n")
    print(A)
    print("\nMatrix B equals \n")
    print(B)
    print("\nMatrix C equals \n")
    print(C)

    print("Matrix A has dimension ", A.dimension())
    print("Matrix B has dimension ", B.dimension())
    print("Matrix C has dimension ", C.dimension())

    print()
    print("The second row of matrix A is: ", A.row(2))
    print("The third column of matrix B is: ", B.row(3))
    print("The second column of matrix C is: ", C.row(2))

    print()
    D = A + C
    print("The sum of matrices A and C is: \n")
    print(D)

    D = C - A
    print("The difference of matrices C and A is: \n")
    print(D)

    D = A*B
    print("The product of  matrices A and B is: \n")
    print(D)

    D = A*C
    print(D)

    D = A.reduce_matrix(1, 1)
    print("Matrix obtained by removing row 1, column 1 of matrix A: \n")
    print(D)

    D = B.reduce_matrix(3, 2)
    print("Matrix obtained by removing row 3, column 2 of matrix B: \n")
    print(D)

    D = B.determinant()
    print("The determinant of matrix B is: ", D)

    print("\nGoodbye!")
