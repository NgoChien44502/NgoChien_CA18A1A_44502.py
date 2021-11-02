"""
Author: Ngo Van Chien
Date: 18/09/2021

Problem:    The greatest common divisor of two positive integers, A and B, is the largest
number that can be evenly divided into both of them. Euclid’s algorithm can be
used to find the greatest common divisor (GCD) of two positive integers. You
can use this algorithm in the following manner:

Solution:

    ....
"""
nho = int(input("Nhập số nhỏ"))
lon = int(input("Nhập số lớn"))
for i in range(1, nho+1):
    if (nho % i==0)and (lon % i==0):
        gcd=i
        print("\nDivisor phổ biến {}".format(gcd))