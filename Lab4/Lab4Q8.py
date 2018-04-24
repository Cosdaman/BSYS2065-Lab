# Write a function areaOfCircle(r) which returns the area of a circle of radius r.
# Make sure you use the math module in your solution.

import math

radius = input("Please input a radius: ")
radius = int(radius)
area = math.pi * radius**2
print("The area is: ", area)
input("Press enter to continue...")
