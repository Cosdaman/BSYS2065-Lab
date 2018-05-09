# Modify the walking turtle program so that rather than a 90 degree left or right turn the
# angle of the turn is determined randomly at each step.

import random
import turtle


def isinscreen(w, t):
    leftbound = - w.window_width() / 2
    rightbound = w.window_width() / 2
    topbound = w.window_height() / 2
    bottombound = -w.window_height() / 2

    turtlex = t.xcor()
    turtley = t.ycor()

    stillin = True
    if turtlex > rightbound or turtlex < leftbound:
        stillin = False
    if turtley > topbound or turtley < bottombound:
        stillin = False

    return stillin


toit = turtle.Turtle()
wn = turtle.Screen()

toit.shape('turtle')
while isinscreen(wn, toit):
    coin = random.randrange(0, 2)
    if coin == 0:
        toit.left(random.randint(0, 361))
    else:
        toit.right(random.randint(0, 361))

    toit.forward(50)

wn.exitonclick()
