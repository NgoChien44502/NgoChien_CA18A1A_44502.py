"""
Author: Ngo Van Chien
Date: 03/09/2021

Problem:   Write a program that takes the radius of a sphere (a floating-point number) as
input and then outputs the sphere’s diameter, circumference, surface area, and
volume

Solution:
    ....
"""
bankinh = float(input("Nhập bán kính:"))

duongkinh = 2* bankinh
pi = 3.14
chuvi = duongkinh*2
dientich = 4*pi*bankinh**2
thetich = (4*pi*bankinh**3)/3

print("Đường kinh:"+str(duongkinh))
print("Chu vi:"+str(chuvi))
print("Thể tich:"+str(thetich))




