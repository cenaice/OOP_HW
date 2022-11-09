"""
Author: 
Module for Homework 4, Problem 2
Object Oriented Programming (50:198:113), Fall 2022

Insert module documentation for Problem #2 here
"""

## IMPLEMENT ALL FUNCTIONS FOR MATRICES BELOW.
## DOCUMENT ALL FUNCTIONS APPROPRIATELY 


## USE THE FOLLOWING TEST CODE TO TEST YOUR FUNCTION 
## IMPLEMENTATIONS ABOVE

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
