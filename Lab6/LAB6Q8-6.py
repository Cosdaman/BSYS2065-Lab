# Modify the walking turtle program so that rather than a 90 degree left or right turn the
# angle of the turn is determined randomly at each step.
# Modify the turtle walk program so that you have two turtles each with a random starting location.
# Keep the turtles moving until one of them leaves the screen.
# Modify the previous turtle walk program so that the turtle turns around when it hits the wall or when one
# turtle collides with another turtle (when the positions of the two turtles are closer than some small number).

import random
import turtle


def moveRandom(wn, t):
    coin = random.randrange(0, 2)
    if coin == 0:
        t.left(random.randint(0, 361))
    else:
        t .right(random.randint(0, 361))

    t.forward(50)


def areColliding(t1, t2):
    if t1.distance(t2) < 2:
        return True
    else:
        return False


def isInScreen(w, t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False
    return stillIn


def wallcheck(toit):
    if toit.xcor() > rightBound-leeway:
        toit.setheading(toit.towards((0, 0)))
        toit.forward(10)
    elif toit.xcor() < leftBound + leeway:
        toit.setheading(toit.towards((0, 0)))
        toit.forward(10)
    elif toit.ycor() > topBound - leeway:
        toit.setheading(toit.towards((0, 0)))
        toit.forward(10)
    elif toit.ycor() < bottomBound + leeway:
        toit.setheading(toit.towards((0, 0)))
        toit.forward(10)
    else:
        moveRandom(wn, toit)


t1 = turtle.Turtle()
t2 = turtle.Turtle()
wn = turtle.Screen()

t1.shape('turtle')
t2.shape('circle')

leftBound = -wn.window_width() / 2
rightBound = wn.window_width() / 2
topBound = wn.window_height() / 2
bottomBound = -wn.window_height() / 2

leftBound = int(leftBound)
rightBound = int(rightBound)
topBound = int(topBound)
bottomBound = int(bottomBound)

t1.up()
t1.goto(random.randrange(leftBound, rightBound), random.randrange(bottomBound, topBound))
t1.setheading(random.randrange(1, 360))
t1.down()

t2.up()
t2.goto(random.randrange(leftBound, rightBound), random.randrange(bottomBound, topBound))
t2.setheading(random.randrange(1, 360))
t2.down()

t1.speed(0)
t2.speed(0)

leeway = int(10)
while 1:
    wallcheck(t1)
    wallcheck(t2)




wn.exitonclick()
