#Quadratic Equation Solver
import math
a = float(input("Enter coeffi a: "))
b = float(input("Enter coeffi b: "))
c = float(input("Enter coeffi c: "))
dis = b**2 - 4*a*c
if dis >= 0:
    x1 = (-b + math.sqrt(dis)) / (2*a)
    x2 = (-b - math.sqrt(dis)) / (2*a)
    print(f"Solution 1: {x1}")
    print(f"Solution 2: {x2}")
else:
    print("The equation has no real solutions.")
