"""
Author: Ngo Van Chien
Date: 25/09/2021

Problem:Octal numbers have a base of eight and the digits 0–7. Write the scripts octalToDecimal.py and
decimalToOctal.py, which convert numbers between the octal
and decimal representations of integers. These scripts use algorithms that are
similar to those of the binaryToDecimal and decimalToBinary scripts developed in Section 4-3.

Solution:

    ....
"""
"""
ten: decimalToOctal.py

"""
decimal = int(input('Nhập sô thập phân:'))
print('\nSố bát phân')
i = 1
octalNum = 0
num = ""
while (decimal !=0):
    rm = decimal % 8
    decimal//=8
    octalNum=octalNum+rm*i
    i*=10
    num=str(rm)+num
    print('%5d%8d%12s' % (decimal,rm,num))
    print('Biểu diễn bát giác ',octalNum)

"""
ten :octalToDecimal.py
"""
octalNum=int(input('Nhập chuỗi số bát giác:'))
i=1
decimal=0
while (octalNum!=0):
    rmd=octalNum % 10
    octalNum//=10
    decimal+=rmd*i
    i*=8
    print('\nGiá trị số nguyên là',decimal)