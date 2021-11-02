"""
Author: Ngo Van Chien
Date: 18/09/2021

Problem:    Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is an equilateral
triangle.

Solution:

    ....
"""
a = float(input("Nhập cạnh thứ nhất:"))
b = float(input("Nhập cạnh thứ hai:"))
c = float(input("Nhập cạnh thứ ba:"))
print("")
if ((a*2 == b*2 + c*2) or (a*2 + b*2 == c*2) or (a*2 + c*2 == b*2)):
     print("La tgv")
else:
    print("Không là tgv")

