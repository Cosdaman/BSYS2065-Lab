import turtle


def drawsquare(size):
    for y in range(4):
        toit.pendown()
        toit.forward(size)
        toit.left(90)


wn = turtle.Screen()
toit = turtle.Turtle()
wn.bgcolor("light green")
toit.color("pink")

toit.pensize(3)
toit.speed(1)

x = 20

for i in range(1, 6):
    drawsquare(x*i)
    toit.penup()
    toit.forward(-10)
    toit.right(90)
    toit.forward(x/2)
    toit.left(90)

wn.exitonclick()
