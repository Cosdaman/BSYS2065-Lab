import turtle


def drawsquare(size):
    for y in range(4):
        toit.pendown()
        toit.forward(size)
        toit.left(90)


wn = turtle.Screen()
toit = turtle.Turtle()
wn.bgcolor("light green")
toit.color("blue")
toit.pensize(3)
toit.speed(0)

for i in range(20):
    drawsquare(80)
    toit.left(18)

wn.exitonclick()
