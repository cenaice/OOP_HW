from polys import *

import math

if __name__ == "__main__":
    print("\n*********************************************")
    print("This module provides some basic test code for ")
    print("the classes in Assignment 6.")    
    print("*********************************************")
    
    p1 = Point(1, 1)
    p2 = Point(3, 0)
    p3 = Point(4, 1)
    p4 = Point(3, 3)
    p5 = Point(2, 3)

    print("---------Testing the Point class---------\n")

    print("p1: ", p1)
    print("p2: ", p2)
    print("Distance b/w p1 and p2: ", p1.distance(p2))

    print(p1, end = " ")
    p1.rotate(45)
    print("rotated by 45 degrees: ", p1)
    print()

    print(p1, end = " ")
    p1.rotate(-45)
    print("rotated by -45 degrees: ", p1)
    print()

    print(p2, end = " ")
    p2.translate(-2, 3)
    print("translated by (-2, 3): ", p2)
    print()

    print(p2, end = " ")
    p2.translate(2, -3)
    print("translated back by (2, -3): ", p2)
    print()

    if p2.right_of(p1, p3):
        print(p1, p3, p2, " make a right turn. (CORRECT!)")
    else: 
        print(p1, p3, p2, " do not make a right turn. (INCORRECT!)")
    print()

    if p5.left_of(p1, p3):
        print(p1, p3, p5, " make a left turn. (CORRECT!)")
    else: 
        print(p1, p3, p5, " do not make a left turn. (INCORRECT!)")
    print()

    print("---------Testing the SimplePoly class---------\n")

    S = SimplePoly(p2, p3, p4, p5)
    print("Simple polygon S has been created as follows: ")
    print(S)

    print("The perimeter of S is ", S.perimeter())
    print()

    print("---------Testing the ConvPoly class---------")

    newp5 = Point(2, 1.75)
    try:
        P = ConvPoly(p1, p2, p3, p4, newp5)
    except:
        print("\nCORRECT: ConvPoly __init__ raises exception for violating convexity.\n")
    else:
        print("\nINCORRECT: ConvPoly __init__ NOT CHECKING FOR CONVEXITY.\n")

    P = ConvPoly(p1, p2, p3, p4, p5)
    print("Convex polygon P has been created as follows: ")
    print(P)
    print()

    print("The perimeter of P is ", P.perimeter())
    print()

    P.translate(-2, 3)
    print("\nP translated by (-2, 3): ")
    print(P)
    print()

    P.rotate(45)
    print("\nNow P is rotated by 45 degrees: ")
    print(P)
    print()

    print("\nThe perimeter of P is ", P.perimeter())
    print("(The answer should be the same as the previous one.)")

    print("\nThe vertices of P are (this checks __getitem__ and __len__): ")
    for i in range(len(P)):
        print(P[i])
    print()

    print("\nChecking iter and next: ")
    i = iter(P)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    try:
        print(next(i))
    except StopIteration: 
        print("A StopIteration was (correctly) caught.")

    print("\n----------------Testing RegularPoly-----------------")
    octagon = RegularPoly(8)
    print("A regular octagon (8 sided polygon) has been created:")
    print(octagon)

    print("The perimeter of the regular octagon is ", octagon.perimeter())
    print("The vertex angle of the regular octagon is ", octagon.vertexangle(),
          " degrees. (Correct answer is 135.0 degrees.)")
    print("The edge length of the regular octagon is ", round(octagon.edgelength(), 3),
          " units. (Correct answer is 0.765 units.)")

    print()
    octagon.scale(3)
    print("The octagon has been scaled by a factor of 3. It is now as follows:")
    print(octagon)

    print()
    print("---------Testing Triangle and EquiTriangle---------\n")

    T = Triangle(Point(1,2), Point(5,2), Point(1,5))
    print("A triangle T has been created: ")
    print(T)

    print("The perimeter of T is ", T.perimeter())
    print("The area of T is ", T.area())

    T.rotate(90)
    print("T, after it has been rotated by 90 degrees: ")
    print(T)

    try:
        T = Triangle(Point(1, 1), Point(2, 2), Point(3, 3))
    except:
        print("An exception was (correctly) raised when creating a triangle with collinear vertices")
    else:
        print("ERROR: An exception was not raised when creating a triangle with collinear vertices")
    

    print()
    E = EquiTriangle(4 * math.sqrt(3))
    print("An equilateral triangle E with side length 6.928 has been created: ")
    print("Its vertices are: ")
    for v in E:
        print(v)

    print()
    print("The perimeter of E is ", E.perimeter())
    print("The area of E is ", E.area())
    print("The vertex angle of E is ", E.vertexangle(), "(should be 60.0)")
    print("The edge length of E is ", round(E.edgelength(), 3), "(should be 6.928)")    

    E.rotate(90)
    print("E, after it has been rotated by 90 degrees: ")
    print(E)

    print()

    print()
    print("---------Testing Rectangle and Square---------\n")

    R = Rectangle(3, 4)
    print("A rectangle R with width 3 and height 4 has been created.")
    print("Its vertices are: ")
    for v in R:
        print(v)

    print("The perimeter of R is ", R.perimeter())
    print("The area of R is ", R.area())

    R.translate(-1, 2)
    print("R has been translated by (-1, 2). Its vertices are: ")
    for v in R:
        print(v)

    print()
    S = Square(5 * math.sqrt(2))
    print("A square S of side length 7.071 has been created: ")

    print("Its vertices are: ")
    for i in range(len(S)):
        print(S[i])

    print("The perimeter of S is ", S.perimeter())
    print("The area of S is ", S.area())
    print("The vertex angle of S is ", S.vertexangle(), "(should be 90.0)")
    print("The edge length of S is ", round(S.edgelength(), 3), "(should be 7.071)")    

    print()
    print("That's all for now. Goodbye!")
