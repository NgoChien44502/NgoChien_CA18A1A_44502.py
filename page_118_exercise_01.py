"""
Author: Ngo Van Chien
Date: 25/09/2021

Problem:Assume that the variable data refers to the string "Python rules!". Use a string
method from Table 4-2 to perform the following tasks:
a. Obtain a list of the words in the string.
b. Convert the string to uppercase.
c. Locate the position of the string "rules".
d. Replace the exclamation point with a question mark.

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


