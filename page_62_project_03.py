"""
Author: Ngo Van Chien
Date: 03/09/2021

Problem:   Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who
    like to buy LP record albums. The store rents new videos for $3.00 a night, and
    oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video
    can use to calculate the total charge for a customer’s video rentals. The program
    should prompt the user for the number of each type of video and output the total
    cost

Solution:


    ....
"""
videomoi = int(input("Nhập số lượng video mới:"))
oldies = int(input("Nhập số lượng oldies:"))

giavideomoi = 3.00*videomoi
giaoldies = 2.00*oldies

tongchiphi = giaoldies+giaoldies
print("Tổng giá tiền là $:"+str(tongchiphi))

