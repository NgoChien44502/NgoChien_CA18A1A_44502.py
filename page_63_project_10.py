"""
Author: Ngo Van Chien
Date: 03/09/2021

Problem:   An employee’s total weekly pay equals the hourly wage multiplied by the total
number of regular hours plus any overtime pay. Overtime pay equals the total
overtime hours multiplied by 1.5 times the hourly wage. Write a program that
takes as inputs the hourly wage, total regular hours, and total overtime hours and
displays an employee’s total weekly pay

Solution:
    ....
"""
tienluong = float(input("Mhập tiền lương:$"))
giocodinh = float(input("Nhập giờ bình thường"))
giotangca = float(input("Nhập giờ tăng ca:"))

tientangca = tienluong*1.5
tientuan = tienluong*giocodinh+tientangca
print("Tổng tiên 1 tuần:"+str(tientuan)+"$")







