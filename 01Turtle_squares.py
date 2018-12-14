# draw two squares, side by side, not touching

from turtle import *


def draw_square():
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)


draw_square()

penup()
forward(150)
pendown()

draw_square()

exitonclick()

print()
input("Press return to continue ...")
