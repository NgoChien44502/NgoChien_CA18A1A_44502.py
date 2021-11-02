"""
Author: Ngo Van Chien
Date: 03/09/2021

Problem:   The kinetic energy of a moving object is given by the formula KE 1 2/ mv 5 2 ( )
where m is the object’s mass and v is its velocity. Modify the program you created
in Project 5 so that it prints the object’s kinetic energy as well as its momentum.

Solution:
    ....
"""
khoiluong = float(input("Nhập khối lượng:"))
vantoc = float(input("Nhập vạn tốc:"))
dongluong = khoiluong*vantoc
dongnang = (khoiluong*vantoc**2)/2

print("Đong luong:"+str(dongluong))
print("dong nang:"+str(dongnang))




