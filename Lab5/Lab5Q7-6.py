# Write a function findHypot. The function will be given the length of two sides of a right-angled triangle
# and it should return the length of the hypotenuse.
# (Hint: x ** 0.5 will return the square root, or use sqrt from the math module)

import math


def findHypot(xside, yside):

    hypotenuse = xside**2 + yside**2
    hypotenuse = math.sqrt(hypotenuse)

    return hypotenuse


x = int(input("Input the first side of the triangle: "))
y = int(input("Input the second side of the triangle: "))
print("The hypotenuse of the triangle is: ", findHypot(x, y))




