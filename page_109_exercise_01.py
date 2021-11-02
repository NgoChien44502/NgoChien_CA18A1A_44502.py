"""
Author: Ngo Van Chien
Date: 25/09/2021

Problem:Write the encrypted text of each of the following words using a Caesar cipher with
a distance value of 3:
a. python
b. hacker
c. wow

Solution:
    ....
"""
distance = 3
x = ["python", "hacker", "wow"]
for plainText in x:
    code = ""
    for ch in plainText:
        ordvalue = ord(ch)
        ciphervalue = ordvalue + distance
        if ciphervalue > ord("z"):
            ciphervalue = ord("a") + distance - \
                          (ord("z") - ordvalue + 1)
        code += chr(ciphervalue)
    print(code)