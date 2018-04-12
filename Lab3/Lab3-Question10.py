import turtle

wn = turtle.Screen()
toit = turtle.Turtle()
wn.bgcolor("light green")
toit.shape("turtle")
toit.color("blue")
toit.pensize(5)
toit.penup()
toit.speed(0)

for i in range(12):
    toit.forward(75)
    toit.pendown()
    toit.forward(10)
    toit.penup()
    toit.forward(15)
    toit.stamp()
    toit.forward(-100)
    toit.left(30)

wn.exitonclick()
