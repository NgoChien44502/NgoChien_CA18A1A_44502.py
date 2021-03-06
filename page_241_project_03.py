"""
Author: Ngô Văn Chiến
Date: 17/10/2021
 Problem: The Koch snowflake is a fractal shape. At level 0, the shape is an equilateral triangle. At level 1,
  each line segment is split into four equal parts, producing an
equilateral bump in the middle of each segment
Solution:

    ....
"""

from turtle import Turtle

def drawKochFractal(width, height, size, level):
    """Draws a Koch fractal of the given level and size."""
    t = Turtle()
    t.hideturtle()
    t.up()
    t.goto(-width // 3, height // 4)
    t.down()
    drawFractalLine(t, size, 0, level)
    drawFractalLine(t, size, -120, level)
    drawFractalLine(t, size, 120, level)


def drawFractalLine(t, distance, theta, level):
    """Either draws a single line in a given direction

    or four fractal lines in new directions."""

    if (level == 0):
        drawPolarLine(t, distance, theta)
    else:
        drawFractalLine(t, distance // 3, theta, level - 1)
        drawFractalLine(t, distance // 3, theta + 60, level - 1)
        drawFractalLine(t, distance // 3, theta - 60, level - 1)
        drawFractalLine(t, distance // 3, theta, level - 1)


def drawPolarLine(t, distance, theta):
    """Moves the given distance in the given direction."""
    t.setheading(theta)
    t.forward(distance)


def main():
    level = int(input("Enter the level: "))
    drawKochFractal(200, 200, 150, level)


main()