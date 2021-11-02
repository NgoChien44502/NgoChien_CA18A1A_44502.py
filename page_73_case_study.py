"""
Author: Ngo Van Chien
Date: 18/09/2021

Problem:   Request
Write a program that computes an investment report.
Analysis
The inputs to this program are the following:
• An initial amount to be invested (a floating-point number)
• A period of years (an integer)
• An interest rate (a percentage expressed as an integer)

Solution:

    ....
"""

sodubandau = float(input("Nhập số tiền đầu tư: "))
nam = int(input("Nhập số năm: "))
thue = int(input("Nhập tỉ lệ %: "))

thue = thue / 100

tonglai = 0.0

print("%4s%18s%10s%16s" % \
    ("Năm", "Bắt đầu ",
    "Lãi", "Kết thúc số dư"))

for nam in range(1, nam + 1):
    lai = sodubandau * thue
    soducuoi = sodubandau + lai
    print("%4d%18.2f%10.2f%16.2f" % \
        (nam, sodubandau,  lai, soducuoi))
    sodubandau = soducuoi
    tonglai += lai

print("Kết thúc số dư: $%0.2f" % soducuoi)
print("Tổng lãi nhận được: $%0.2f" % tonglai)

