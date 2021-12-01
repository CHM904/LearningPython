import turtle
import random

print(random.random())



for i in range(1, 20):
    turtle.forward(int(random.random()*100))
    turtle.right(int(random.random()*100))


turtle.fillcolor("red")
turtle.begin_fill()

repeat=0

while repeat <360:
    turtle.forward(1)
    turtle.right(1)
    repeat = repeat +1

turtle.end_fill()

yourname = input("What's your name?")