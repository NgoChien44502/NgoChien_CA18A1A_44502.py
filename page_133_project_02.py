"""
Author: Ngo Van Chien
Date: 25/09/2021

Problem:Write a script that inputs a line of encrypted text and a distance value and outputs
plaintext using a Caesar cipher. The script should work for any printable characters

Solution:

    ....
"""
codedText = input("Nhập văn bản đã mã hóa: ")
distanceValue = int(input("Nhập khoảng cách: "))
result = ""
for ch in codedText:
 result += chr(ord(ch)-distanceValue)
print("" + result)
