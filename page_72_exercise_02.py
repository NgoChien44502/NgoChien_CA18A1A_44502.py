"""
Author: Ngo Van Chien
Date: 18/09/2021

Problem:   Write a code segment that displays the values of the integers x, y, and z on a single
line, such that each value is right-justified with a field width of 6.

Solution:

    ....
"""
x = int(input("nhap x:"))
y = int(input("nhap y:"))
z = int(input("nhap z:"))
print("%6d" % x)
print("%6d" % y)
print("%6d" % z)
