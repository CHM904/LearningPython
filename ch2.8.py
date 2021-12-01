import turtle
import random

def drawShape(sides, length, color):
    angle = 360.0/sides
    turtle.fillcolor(color)
    turtle.begin_fill()
    for side in range(sides):
        turtle.forward(length)
        turtle.right(angle)
    turtle.end_fill()

def moveturtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def drawSquare(length, color):
    drawShape(4, length, color)

def drawTriangle(length, color):
    drawShape(3, length, color)

def drawCircle(length, color):
    drawShape(360, length, color)

def drawStar(length, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(length)
        turtle.right(144)
    turtle.end_fill()

def drawRandom():
    x = random.randrange(200)
    y = random.randrange(200)
    length = random.randrange(1,75)
    shape = random.randrange(1, 5)
    color_pick = random.randrange(1,5)

    if color_pick == 1:
        color = "Red"
    elif color_pick == 2:
        color = "Blue"
    elif color_pick == 3:
        color = "Green"
    else:
        color = "Brown"

    moveturtle(x, y)

    if shape == 1:
        drawSquare(length, color)
    elif shape == 2:
        drawTriangle(length, color)
    elif shape == 3:
        length = length % 4
        drawCircle(length, color)
    else:
        drawStar(length, color)

for shape in range(10):
    drawRandom()

turtle.done()  