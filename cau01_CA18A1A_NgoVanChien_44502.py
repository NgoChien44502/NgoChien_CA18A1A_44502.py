"""
Ôn tập 2
Date: 29/10/2000
Ngo Van Chien
"""
bitString = input("Nhập dãy : ")
decimal = 0
exponent = len(bitString) - 1
for digit in bitString:
    decimal = decimal + int(digit) * 2 ** exponent
    exponent = exponent - 1
print("Số thập phân là", decimal)
print("=="*20)