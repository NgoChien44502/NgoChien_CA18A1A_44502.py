"""
Author: Ngô Văn Chiến
Date: 17/10/2021
 Problem: Define a function drawCircle. This function should expect a Turtle object,
    the coordinates of the circle’s center point, and the circle’s radius as arguments. The function should draw the specified circle. The algorithm should
    draw the circle’s circumference by turning 3 degrees and moving a given
    distance 120 times. Calculate the distance moved with the formula 2.0 * p *
    radius / 120.0.
Solution:

    ....
"""
import math
from turtle import Turtle
from time import sleep

def drawCircle(t, x, y, radius):

    t.up()
    t.goto(x + radius, y)
    t.setheading(90)
    t.down()
    for count in range(120):
        t.left(3)
        t.forward(2.0 * math.pi * radius / 120.0)

def main():

    x = int(input("Nhập tọa độ X: "))
    y = int(input("Nhập tọa độ Y: "))
    radius = int(input("Bán kính: "))
    drawCircle(Turtle(), x, y, radius)
    sleep(5)

if __name__ == '__main__':
    main()