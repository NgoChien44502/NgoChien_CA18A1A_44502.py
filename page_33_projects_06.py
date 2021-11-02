"""
Author: Ngo Van Chien
Date: 28/08/2021

Problem:    Write and test a program that computes the area of a circle. This program should
request a number representing a radius as input from the user. It should use the formula
3.14 * radius ** 2 to compute the area and then output this result suitably labeled.

Solution:

    ....
"""
bankinh = int(input("Nhập bán kính:"))
pi = 3.14
dientich= pi*bankinh**2
print("Diện tích hình tron là",dientich,"vuong")