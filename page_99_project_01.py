"""
Author: Ngo Van Chien
Date: 18/09/2021

Problem:    Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is an equilateral
triangle.

Solution:

    ....
"""
canh1 = int(input("Nhập cạnh thứ nhất:"))
canh2 = int(input("Nhập cạnh thứ hai:"))
canh3 = int(input("Nhập cạnh thứ ba:"))
print("")
if canh1 == canh2 == canh3:
    print("Là tam giác đều")
else:
    print("Không là tam giác đều")