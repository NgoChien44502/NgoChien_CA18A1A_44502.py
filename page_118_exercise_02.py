"""
Author: Ngo Van Chien
Date: 25/09/2021

Problem:Using the value of data from Exercise 1, write the values of the following
expressions:
a. data.endswith('i')
b. " totally ".join(data.split())

Solution:
    ....
"""

data = "Python rules!"
tokens = data.split(" ")
print(tokens)
upperCaseData = data.upper()
print(upperCaseData)
iIndexPos = data.index("rules")
print(iIndexPos)
tweakedData = data.replace("!","?")
print(tweakedData)
print(data.endswith("i"))
print(data.endswith("!"))
totally = " totally "
outbuff = totally.join(tokens)
print(outbuff)