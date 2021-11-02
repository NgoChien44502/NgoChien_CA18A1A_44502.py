"""
Author: Ngo Van Chien
Date: 03/09/2021

Problem:   Write a program that takes as input a number of kilometers and prints the corresponding number of nautical miles. Use the following approximations:
• A kilometer represents 1/10,000 of the distance between the North Pole and
the equator.
• There are 90 degrees, containing 60 minutes of arc each, between the North
Pole and the equator.
• A nautical mile is 1 minute of an arc

Solution:
    ....
"""
khoangcach = int(input("Nhập số km:"))
do = 60*90
motkm = do/1000
haili = motkm * khoangcach
print("Số hải lý là :"+str(haili))







