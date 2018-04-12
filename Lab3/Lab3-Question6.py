import turtle

numSides = int(input("Please enter the number of sides: "))
lenSides = int(input("Enter the length of each side: "))
lineColor = str(input("Enter the color of the sides: "))
fillColor = str(input("Enter the inner color of the shape: "))

angle = int(360 / numSides)
wn = turtle.Screen()
toit = turtle.Turtle()
toit.begin_fill()
toit.color(lineColor, fillColor)

for i in range(numSides):
    toit.forward(lenSides)
    toit.right(angle)

toit.end_fill()
wn.exitonclick()
