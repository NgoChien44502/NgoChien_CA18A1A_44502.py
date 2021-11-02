"""
Author: Ngo Van Chien
Date: 03/09/2021

Problem:   The tax calculator program of the case study outputs a floating-point number
that might show more than two digits of precision. Use the round function to
modify the program to display at most two digits of precision in the output
number

Solution:
            Tính thuế thu nhập của một người.
    1. Hằng số đáng kể
    thuế suất
    khấu trừ tiêu chuẩn
    khấu trừ cho mỗi người phụ thuộc
    2. Đầu vào là
    tổng thu nhập
    số lượng người phụ thuộc
    3. Tính toán:
    thu nhập chịu thuế = tổng thu nhập - khấu trừ tiêu chuẩn -
    khấu trừ cho từng người phụ thuộc
    thuế thu nhập = là một tỷ lệ phần trăm cố định của thu nhập chịu thuế
    4. Đầu ra là
    thuế thu nhập

    ....
"""
thuesuat = 0.2
khautrutieuchuan = 10000
khautrunguoiphuthuoc = 3000

tongthunhap = float(input("Nhập tổng thu nhập:"))
songuoiphuthuoc = int(input("Nhập số lượng người phụ thuộc:"))

thunhapchiuthue = tongthunhap-khautrutieuchuan-khautrunguoiphuthuoc*songuoiphuthuoc
thuethunhap = round(thunhapchiuthue*thuesuat,2)

print("Thuế thu nhập là $:"+str(thuethunhap))  #hiển thi


