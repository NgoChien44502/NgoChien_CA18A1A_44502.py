"""
Author: Ngô Văn Chiến
Date: 24/10/2021

Problem:
   Convert Newton’s method for approximating square roots in Project 1 to a recursive function named newton.
   (Hint: The estimate of the square root should be
passed as a second argument to the function.
Solution:
    ....
"""
import math

TOLERANCE = 0.000001


def newton(x, estimate):
    difference = abs(x - estimate ** 2)
    if difference <= TOLERANCE:
        return estimate
    else:
        return newton(x, (estimate + x / estimate) / 2)


def main():

    while True:
        x = input("Enter a positive number or enter return to quit: ")
        if x == "":
            break
        x = float(x)
        print("The program is estimate is", newton(x, 1))
        print("Python is estimate is    ", math.sqrt(x))
