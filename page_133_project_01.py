"""
Author: Ngo Van Chien
Date: 25/09/2021

Problem: Write a script that inputs a line of plaintext and a distance value and outputs an
encrypted text using a Caesar cipher. The script should work for any printable
characters.

Solution:
    ....
"""
message = input("Nhập văn bản: ")
distanceValue = int(input("Nhập khoảng cách: "))
result = ""
for x in message:
 result += chr(ord(x)+distanceValue)
print(""+result)
